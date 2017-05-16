
import mysql.connector
from mysql.connector import errorcode
from collections import OrderedDict

class DatabaseClass:
    def __init__(self, database):
        self.name = database
        self.connect = mysql.connector.connect(user='root',
                                               password='admin',
                                               host='127.0.0.1')
        self.cursor = self.connect.cursor()


        self.connect_2_databsae()

    def connect_2_databsae(self):
        try:
            self.connect.database = self.name
        except mysql.connector.Error as err:
            print(err.msg)

    def create_table(self, table_name='Default', entry="Id int(5) Auto increment primary key('id')"):
        cmd = (" CREATE TABLE IF NOT EXISTS " + table_name + " (" +
                entry + ") ENGINE=InnoDB;")
        self.cursor.execute(cmd)

    def get_column(self, table_name):
        return self.run_command("SHOW COLUMNS FROM %s;" % table_name)

    def get_rows(self, table_name):
        return self.run_command("Select *  FROM %s;" % table_name)

    def get_tables(self):
        return self.run_command("show tables;")

    def get_table(self, name='nazwa1'):
        return self.run_command("select * from " + name + ';')

    def insert_row(self, data, table_name='nazwa1'):
        values = data[0]
        for i in range(1, len(data)):
            values += ' ,' + "'" + (data[i])+"'"
        print values
        return self.run_command("Insert into " + str(table_name) + ' values ( ' + values + ');' )

    def delete_row(self, key, value, table_name):
        return self.run_command("DELETE FROM " + str(table_name) + 'WHERE ' + str(key) + "= '" + str(value) + "';")

    def get_data(self,nazwa):
        rows = self.get_rows(nazwa)
        cols = self.get_column(nazwa)
        dict = OrderedDict()
        for j in range(len(cols)):
            list = []
            for i in range(len(rows)):
                list.append(str(rows[i][j]))
            dict[str(cols[j][0])] = list
        return dict

    def run_command(self, cmd):

        print("RUNNING COMMAND: " + cmd)
        try:
            self.cursor.execute(cmd)
        except mysql.connector.Error as err:
            print('ERROR MESSAGE: ' + str(err.msg))
            print('WITH ' + cmd)
        try:
            msg = self.cursor.fetchall()
        except:
            msg = self.cursor.fetchone()
        # self.cursor.close()
        return msg

    def __del__(self):
        self.connect.commit()
        self.cursor.close()
        self.connect.close()


if __name__ == '__main__':

    db_name = 'zzp_project'
    db = DatabaseClass(db_name)
    # db.create_table('nazwa1')
    # print (db.get_column('nazwa1'))
    rows = db.get_rows('nazwa1')
    cols = db.get_column('nazwa1')
    db.insert_row(['56','asdf'])

    # print rows
    # print cols[0][0]
    # dict = OrderedDict()
    # for j in range(len(cols)):
    #     list = []
    #     for i in range(len(rows)):
    #         list.append(str(rows[i][j]))
    #     dict[str(cols[j][0])] = list
    # # print rows[0][0]
    # print dict
    # print a[1]
    # print db.get_column(a[1])
    # dbu.AddEntryToTable ('testing')
    # dbu.AddEntryToTable ('testing2')
    # print (dbu.GetColumns())
    # print (dbu.GetTable())
