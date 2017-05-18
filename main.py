from PyQt4 import QtSql, QtGui, QtCore
from PyQt4.QtCore import *
import sys
from DB_UI_main import Ui_Dialog
from DB_manager import DatabaseClass


class Window(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.db = DatabaseClass('zzp_project')
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.close_application)
        self.combo_box_init()
        self.selected_table = self.ui.comboBox.currentText()
        self.ui.label.setText(self.selected_table)
        self.table_init()
        self.edit_mode_init()

    def combo_box_init(self):
        tables = db.get_tables()
        print tables
        for i in range(len(tables)):
            self.ui.comboBox.addItem('%s ' % tables[i])
        self.ui.comboBox.currentIndexChanged.connect(self.selection_change)

    def update_label(self):
        self.ui.label.setText(self.ui.comboBox.currentText())

    def selection_change(self):
        self.update_label()
        self.update_table()

    def table_init(self):
        self.update_table()
        # self.ui.tableWidget.itemSelectionChanged.connect(self.delete)

    def update_table(self):
        cols = self.db.get_column(self.ui.comboBox.currentText())
        rows = self.db.get_rows(self.ui.comboBox.currentText())
        self.ui.tableWidget.setRowCount(0)  # Resetowanie tabeli
        self.ui.tableWidget.setColumnCount(0)  # Resetowanie tabeli
        self.ui.tableWidget.setColumnCount(len(cols))
        self.ui.tableWidget.setRowCount(len(rows)+1)
        self.set_data(self.db.get_data(self.ui.comboBox.currentText()))

    def set_data(self,data):
        horHeaders = []
        for n, key in enumerate(sorted(data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(data[key]):
                newitem = QtGui.QTableWidgetItem(item)
                self.ui.tableWidget.setItem(m, n, newitem)
        self.ui.tableWidget.setHorizontalHeaderLabels(horHeaders)
        self.read_data_from_qtable()

    def read_data_from_qtable(self):
        model = self.ui.tableWidget.model()
        data = []
        for row in range(model.rowCount()):
            data.append([])
            for column in range(model.columnCount()):
                index = model.index(row, column)
                # We suppose data are strings
                data[row].append(str(model.data(index).toString()))
        return data

    def insert_row(self):
        data = self.read_data_from_qtable()
        data = data[-1]
        for i in range(len(data)):
            # if isinstance(data[i], basestring):
            data[i] =  (data[i])
        print data
        self.db.insert_row(data=data, table_name=self.ui.comboBox.currentText())
        self.update_table()
        self.old_ver = (self.read_data_from_qtable())  # To make possible editing inserted row

    def delete_row(self):
        choice = QtGui.QMessageBox.question(self, "Quit",
                                            'Are you sure you want to'
                                            ' delete highlighted row?',
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            row = self.db.get_rows(self.ui.comboBox.currentText())
            col = self.db.get_column(self.ui.comboBox.currentText())
            for currentQTableWidgetItem in self.ui.tableWidget.selectedItems():
                i = currentQTableWidgetItem.row()
                j = currentQTableWidgetItem.column()
                txt = currentQTableWidgetItem.text()
            self.db.delete_row(str(col[j][0]), txt, str(self.ui.comboBox.currentText()))
            self.old_ver = (self.read_data_from_qtable())  # To make possible editing inserted row
            self.update_table()
        else:
            pass

    def enter_edit_mode(self):
        self.old_ver = (self.read_data_from_qtable())
        if self.ui.radioButton.isChecked():
            self.ui.pushButton_3.setVisible(False)
            self.ui.comboBox.setVisible(True)
        else:
            self.ui.pushButton_3.setVisible(True)
            self.ui.comboBox.setVisible(False)

    def edit_mode_init(self):
        if self.ui.radioButton.isChecked():
            self.ui.pushButton_3.setVisible(True)
            self.ui.comboBox.setVisible(False)
        else:
            self.ui.pushButton_3.setVisible(False)
            self.ui.comboBox.setVisible(True)

    def edit_row(self):
        for currentQTableWidgetItem in self.ui.tableWidget.selectedItems():
            i = currentQTableWidgetItem.row()
            j = currentQTableWidgetItem.column()
            txt = currentQTableWidgetItem.text()
            print i, j, txt
        print(self.read_data_from_qtable())
        col = self.db.get_column(self.ui.comboBox.currentText())
        self.db.edit_row(self.ui.comboBox.currentText(), 'id', self.old_ver[i][0], col[j][0],txt)
        self.old_ver = (self.read_data_from_qtable())  # To make possible editing inserted row

        self.update_table()

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, "Quit", 'Are you sure',
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Quiting...\n")
            sys.exit()
        else:
            pass



if __name__ == '__main__':
    db_name = 'zzp_project'
    db = DatabaseClass(db_name)

    app = QtGui.QApplication(sys.argv)
    ex = Window()
    ex.show()
    x = app.exec_()
    sys.exit(x)
