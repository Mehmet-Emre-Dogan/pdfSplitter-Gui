# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maingui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(608, 446)
        MainWindow.setStyleSheet("*:disabled {\n"
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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.labelFilename = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelFilename.setFont(font)
        self.labelFilename.setObjectName("labelFilename")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelFilename)
        self.verticalLayout.addLayout(self.formLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.spinBoxStart = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.spinBoxStart.setFont(font)
        self.spinBoxStart.setMinimum(1)
        self.spinBoxStart.setMaximum(999999999)
        self.spinBoxStart.setObjectName("spinBoxStart")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.spinBoxStart)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.spinBoxEnd = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.spinBoxEnd.setFont(font)
        self.spinBoxEnd.setMinimum(1)
        self.spinBoxEnd.setMaximum(999999999)
        self.spinBoxEnd.setObjectName("spinBoxEnd")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.spinBoxEnd)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.labelOutPath = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelOutPath.setFont(font)
        self.labelOutPath.setObjectName("labelOutPath")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.labelOutPath)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.btnSplit = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.btnSplit.setFont(font)
        self.btnSplit.setObjectName("btnSplit")
        self.horizontalLayout.addWidget(self.btnSplit)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.btnOOF = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnOOF.setFont(font)
        self.btnOOF.setObjectName("btnOOF")
        self.horizontalLayout_2.addWidget(self.btnOOF)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 608, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionApp_Settings = QtWidgets.QAction(MainWindow)
        self.actionApp_Settings.setObjectName("actionApp_Settings")
        self.menuMenu.addAction(self.actionApp_Settings)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PDF Splitter"))
        self.label_5.setText(_translate("MainWindow", "Input File:"))
        self.labelFilename.setText(_translate("MainWindow", "Drag and drop a PDF file to split"))
        self.label.setText(_translate("MainWindow", "Output Filename: "))
        self.lineEdit.setToolTip(_translate("MainWindow", "Leave empty for timestamped filename"))
        self.label_2.setText(_translate("MainWindow", "Start Page: "))
        self.label_3.setText(_translate("MainWindow", "End Page: "))
        self.label_4.setText(_translate("MainWindow", "Output Path: "))
        self.labelOutPath.setText(_translate("MainWindow", ".\\"))
        self.btnSplit.setText(_translate("MainWindow", " Split "))
        self.btnOOF.setText(_translate("MainWindow", "Open Output Folder"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionApp_Settings.setText(_translate("MainWindow", "App Settings"))
