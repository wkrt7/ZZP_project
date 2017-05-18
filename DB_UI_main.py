# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DB_UI_main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(614, 334)
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 280, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(9, 266, 46, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.radioButton = QtGui.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(340, 50, 88, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.splitter = QtGui.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(9, 10, 256, 212))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.comboBox = QtGui.QComboBox(self.splitter)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.tableWidget = QtGui.QTableWidget(self.splitter)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.splitter_2 = QtGui.QSplitter(Dialog)
        self.splitter_2.setGeometry(QtCore.QRect(271, 9, 225, 23))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.pushButton_2 = QtGui.QPushButton(self.splitter_2)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton = QtGui.QPushButton(self.splitter_2)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_3 = QtGui.QPushButton(self.splitter_2)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.insert_row)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.delete_row)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("pressed()")), Dialog.enter_edit_mode)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton_4.setText(_translate("Dialog", "Quit", None))
        self.label.setText(_translate("Dialog", "TextLabel", None))
        self.radioButton.setText(_translate("Dialog", "Want to edit?", None))
        self.pushButton_2.setText(_translate("Dialog", "Delete Row", None))
        self.pushButton.setText(_translate("Dialog", "Insert Row", None))
        self.pushButton_3.setText(_translate("Dialog", "Edit", None))

