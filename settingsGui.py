# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appSettingsGui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(629, 243)
        Settings.setStyleSheet("*:disabled {\n"
"    background-color:rgb(30, 30, 30);    \n"
"    color: rgb(127, 127, 127);\n"
"}\n"
"*{\n"
"    background-color: rgb(90, 90, 90);\n"
"    color: white;\n"
"}\n"
"QLabel:disabled {\n"
"    background-color: rgb(90, 90, 90);\n"
"}\n"
"QGroupBox{\n"
"    border: 1px solid rgb(70, 70, 70);\n"
"    margin-top: 1em;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QGroupBox:disabled {\n"
"    background-color: rgb(90, 90, 90);\n"
"}\n"
"QGroupBox::title {\n"
"    background-color: rgb(90, 90, 90);\n"
"        top: -0.8em;\n"
"        left: 1em;\n"
"}\n"
"QMenu::item{\n"
"    background-color: rgb(90, 90, 90);\n"
"    color: white;\n"
"}\n"
"\n"
"QMenuBar::item:selected{\n"
"    color: cyan;\n"
"}\n"
"QMenu::item:selected {\n"
"    color: cyan;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(Settings)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.lblInput = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblInput.setFont(font)
        self.lblInput.setObjectName("lblInput")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblInput)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditInput = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditInput.setFont(font)
        self.lineEditInput.setFrame(True)
        self.lineEditInput.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEditInput.setReadOnly(True)
        self.lineEditInput.setObjectName("lineEditInput")
        self.horizontalLayout_2.addWidget(self.lineEditInput)
        self.btnChgInput = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnChgInput.sizePolicy().hasHeightForWidth())
        self.btnChgInput.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnChgInput.setFont(font)
        self.btnChgInput.setObjectName("btnChgInput")
        self.horizontalLayout_2.addWidget(self.btnChgInput)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.lblOutput = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblOutput.setFont(font)
        self.lblOutput.setObjectName("lblOutput")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblOutput)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEditOutput = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditOutput.setFont(font)
        self.lineEditOutput.setFrame(True)
        self.lineEditOutput.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEditOutput.setReadOnly(True)
        self.lineEditOutput.setObjectName("lineEditOutput")
        self.horizontalLayout_3.addWidget(self.lineEditOutput)
        self.btnChgOutput = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnChgOutput.sizePolicy().hasHeightForWidth())
        self.btnChgOutput.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnChgOutput.setFont(font)
        self.btnChgOutput.setObjectName("btnChgOutput")
        self.horizontalLayout_3.addWidget(self.btnChgOutput)
        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnSavePrefs = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSavePrefs.sizePolicy().hasHeightForWidth())
        self.btnSavePrefs.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnSavePrefs.setFont(font)
        self.btnSavePrefs.setObjectName("btnSavePrefs")
        self.horizontalLayout.addWidget(self.btnSavePrefs)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        Settings.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Settings)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 629, 21))
        self.menubar.setObjectName("menubar")
        Settings.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Settings)
        self.statusbar.setObjectName("statusbar")
        Settings.setStatusBar(self.statusbar)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "PDF Splitter: App Settings"))
        self.lblInput.setText(_translate("Settings", "Default input folder:"))
        self.lineEditInput.setText(_translate("Settings", "./pdfize-Gui/input"))
        self.btnChgInput.setText(_translate("Settings", "Change..."))
        self.lblOutput.setText(_translate("Settings", "Output folder:"))
        self.lineEditOutput.setText(_translate("Settings", "./pdfize-Gui/output"))
        self.btnChgOutput.setText(_translate("Settings", "Change..."))
        self.btnSavePrefs.setText(_translate("Settings", "Save Preferences"))
