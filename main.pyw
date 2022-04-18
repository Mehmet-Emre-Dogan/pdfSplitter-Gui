# My files
from ast import dump
from mainGui import Ui_MainWindow
from settingsGui import Ui_Settings

# For GUI
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtCore 
from PyQt5 import QtGui

import sys

# Other libraries
import os
import datetime
from pathlib import Path
from json import load, dump

from PyPDF2 import PdfFileWriter, PdfFileReader

##########################################################################################
DEBUG = False
STYLE_SHEET_STR = """
*:disabled {
	background-color:rgb(30, 30, 30);	
	color: rgb(127, 127, 127);
}
*{
	background-color: rgb(90, 90, 90);
	color: white;
}
"""
validExtensions = [".pdf", ".PDF"]
settingsFile = "settings.json"
directory = os.path.dirname(os.path.dirname(__file__))  # For more info about parent directories, visit the link. 
                                                        # https://stackoverflow.com/questions/58778625/how-to-get-the-path-of-the-parent-directory-in-python

##########################################################################################
def loadSettings():
    global settingsFile
    with open(settingsFile, "r", encoding="utf-8") as fil:
        dictToReturn = load(fil)
    return dictToReturn

def dumpSettings(settingsDict):
    global settingsFile
    with open(settingsFile, "w", encoding="utf-8") as fil:
        dump(settingsDict, fil)


def main(*args):
    if DEBUG:
        print(args)
    try:
        inFil, start, end = args[0], int(args[1]), int(args[2])
        outName = args[3]
    except:
        raise Exception("Invalid arguments!")
    input_pdf = PdfFileReader(inFil)
    if start <= 0 or end <= 0:
        raise Exception("Enter positive start and end page numbers!")
    if input_pdf.getNumPages() < end:
        raise Exception("End page cannot be greater than overall page number!")
    output = PdfFileWriter()
    for i in range(start-1, end):
        output.addPage(input_pdf.getPage(i))
    with open(outName, "wb") as fil:
        output.write(fil)
    return outName

class worker(QThread):
    sigOutFilename = pyqtSignal(str) # Emit output filename
    sigError = pyqtSignal(str) # Carrier for error message
    def __init__(self, argArr):
        super(worker, self).__init__()
        self.argArr = argArr
    def run(self):
        try:
            # print("started to run")
            self.sigOutFilename.emit(main(*self.argArr))
            
        except (Exception, ValueError, OSError, FileNotFoundError, IndexError) as err:
            self.sigError.emit(str(err))

class emergencyMessage(object):
    def infoMessage(self, title="Info", text="Text text"):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def errorMessage(self, title="Error", text="An error occured"):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        btnOk = msg.button(QMessageBox.Ok)
        msg.exec_()

    def confirmationMsg(self, title="Question", text="Are you sure doing xyz?"):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        answer = msg.exec_()
        return answer == QMessageBox.Yes

class mySettingsWindow(QtWidgets.QMainWindow):
    sigSettingsSaved = pyqtSignal(bool)
    def __init__(self):
        super(mySettingsWindow, self).__init__()
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('img.png'))
        
        self.settings = loadSettings()

        self.ui.lineEditOutput.setText(self.settings["defaultOutputFolder"])
        self.ui.lineEditInput.setText(self.settings["defaultInputFolder"])

        # Btn connections
        self.ui.btnChgInput.clicked.connect(self.onBtnChgInput)
        self.ui.btnChgOutput.clicked.connect(self.onBtnChgOutput)
        self.ui.btnSavePrefs.clicked.connect(self.onBtnSavePrefs)

    def onBtnChgInput(self):
        txt = self.getDirectoryDialog(title="Select Directory")
        if DEBUG:
            print(f"Selected folder: {txt}")
        if txt:
            self.settings["defaultInputFolder"] = txt
            self.ui.lineEditInput.setText(txt)

    def onBtnChgOutput(self):
        txt = self.getDirectoryDialog(title="Select Directory")
        if txt:
            self.settings["defaultOutputFolder"] = txt
            self.ui.lineEditOutput.setText(txt)

    def onBtnSavePrefs(self):
        dumpSettings(self.settings)
        self.sigSettingsSaved.emit(True)
    
    def getDirectoryDialog(self, title="Select folder"):
        response = QFileDialog.getExistingDirectory(self, caption=title)
        return response

class myWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('img.png'))
        self.initSettings()
        self.files = []
        self.ui.btnSplit.setEnabled(False)
        
        # Btn connections
        self.ui.btnSplit.clicked.connect(self.onSplitClicked)
        self.ui.btnOOF.clicked.connect(self.openOutputDir)
        self.setAcceptDrops(True)
        self.ui.menubar.triggered.connect(self.whoGotSelected)

        # Menu bar selection 
    def whoGotSelected(self, selection):
        txt = selection.text()
        if DEBUG:
            print(f"Selection from menubar: {txt}")
        if txt == "App settings" or "Uygulama ayarları":
            self.setSettings()

    def initSettings(self):
        self.settings = loadSettings()
        self.ui.labelOutPath.setText(self.settings["defaultOutputFolder"])

    def setSettings(self):
        self.settingsWindow = mySettingsWindow()
        self.settingsWindow.show()
        self.settingsWindow.sigSettingsSaved.connect(self.initSettings)

    # Drag and drop. See the link below for more info
    # https://gist.github.com/peace098beat/db8ef7161508e6500ebe
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [item.toLocalFile() for item in event.mimeData().urls() if  any(str(item.toLocalFile()).endswith(extension) for extension in validExtensions)]
        if len(files):
            self.files = files
            self.ui.btnSplit.setEnabled(True)
            self.ui.labelFilename.setText(self.files[0])
        if DEBUG:
            for item in event.mimeData().urls():
                print(item.toLocalFile())

    def onSplitClicked(self):
        if self.ui.lineEdit.text(): # if filename is null, create a timestamp filename
            outName = self.ui.lineEdit.text()
        else:
            outName = f"Splitted__{datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S')}.pdf"

        filepath = self.settings["defaultOutputFolder"] + "/" + outName
        if os.path.exists(filepath):
            if self.confirmationMsg(text=f"{filepath}\n file exists. Dou yo want to overwrite?"):
                pass
            else:
                return
        self.ui.btnSplit.setEnabled(False)
        self.worker = worker([self.files[0], self.ui.spinBoxStart.value(), self.ui.spinBoxEnd.value(), filepath])
        self.worker.sigError.connect(self.onError)
        self.worker.sigOutFilename.connect(self.onSuccess)
        self.worker.start()

    def onError(self, msg):
        self.errorMessage(text=msg)
        self.ui.btnSplit.setEnabled(True)
    
    def onSuccess(self, filename):
        self.infoMessage("Success", f"PDF splitted successfully\n{filename}")
        self.ui.btnSplit.setEnabled(True)

    def openOutputDir(self):
        try:
            # Detect the latest created file, see link below for more info
            # https://stackoverflow.com/questions/168409/how-do-you-get-a-directory-listing-sorted-by-creation-date-in-python
            filesWithAbsPaths = sorted(Path(self.settings["defaultOutputFolder"]).iterdir(), key=os.path.getctime, reverse=True)
            if DEBUG:
                for filename in filesWithAbsPaths:
                    print(filename)
            if len(filesWithAbsPaths):
                os.system(f"""start explorer.exe  /select, "{filesWithAbsPaths[0]}" """)
            else:
                os.system(f"""start explorer.exe  "{self.settings["defaultOutputFolder"]}" """)
        except (Exception, ValueError, OSError, FileNotFoundError, IndexError) as err:
            self.errorMessage(text=str(err)) 

    # Message boxes
    def infoMessage(self, title="Info", text="Text text"):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setWindowIcon(QtGui.QIcon('img.png'))
        msg.setText(text)
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        btnOk = msg.button(QMessageBox.Ok)
        btnOk.setText("Ok")
        msg.setStyleSheet(STYLE_SHEET_STR)
        msg.exec_()

    def warningMessage(self, title="Info", text="Text text"):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setWindowIcon(QtGui.QIcon('img.png'))
        msg.setText(text)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        btnOk = msg.button(QMessageBox.Ok)
        btnOk.setText("Ok")
        msg.setStyleSheet(STYLE_SHEET_STR)
        msg.exec_()

    def errorMessage(self, title="Error", text="An error occured"):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setWindowIcon(QtGui.QIcon('img.png'))
        msg.setText(text)
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        btnOk = msg.button(QMessageBox.Ok)
        btnOk.setText("Ok")
        msg.setStyleSheet(STYLE_SHEET_STR)
        msg.exec_()

    def confirmationMsg(self, title="Question", text="Are you sure doing xyz?"):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setWindowIcon(QtGui.QIcon('img.png'))
        msg.setText(text)
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        btnYes = msg.button(QMessageBox.Yes)
        btnYes.setText("Yes")
        btnNo = msg.button(QMessageBox.No)
        btnNo.setText("No")
        msg.setStyleSheet(STYLE_SHEET_STR)
        answer = msg.exec_()
        return answer == QMessageBox.Yes

    
def app():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    emrgMsg = emergencyMessage()
    try:
        win = myWindow()
        # app.aboutToQuit.connect(win.onAboutToQuit)
        try:
            win.show()
            sys.exit(app.exec_())
        except (Exception, ValueError, OSError, FileNotFoundError, IndexError) as err:
            win.errorMessage(title=win.msgBoxStrs[win.lang]["errorOccured"], text=str(err))
    except (Exception, ValueError, OSError, FileNotFoundError, IndexError) as err:
        emrgMsg.errorMessage(title="Very fatal error occured", text=str(err))


if __name__ == "__main__":
    app()