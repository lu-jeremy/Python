import sqlite3
import logging

logging.basicConfig(filename = 'DataBase_logs.txt', level = 'DEBUG')

class DataBase:
    def __init__(self, name):
        self.conn = sqlite3.connect(name)
        self.c = self.conn.cursor()
        logging.debug('Created database')
    def createTable(self, name, columns, data_types):
        self.columns = columns
        query = 'create table if not exists {}('.format(name)
        for var in range(len(columns)):
            query = query + self.columns[var] +  ' ' + data_types[var]
            if var < len(self.columns) - 1:
                query = query + ','
        query = query + ');'
        logging.debug('{}'.format(query))
        
        self.c.execute(query)
        logging.debug('Created table')
    def insert(self, table_name, values):
        # self.c.execute('insert to student values (\'Chicken\', 200, 25289035)') 
        query = 'insert into {} ('.format(table_name)
        for var in range(len(self.columns)):
            query = query + self.columns[var]
            if var < len(self.columns) - 1:
                query += ','
        query +=  ') values ('
        for var in range(len(values)):
            query = query + "'" + values[var] + "'"
            if var < len(values) - 1:
                query += ','
        query += ');'
        logging.debug('{}'.format(query))
        self.c.execute(query)
        
        logging.debug('Inserted information')  
    def readTable(self, table_name):
        self.c.execute('select * from {}'.format(table_name))
        for rows in self.c.fetchall():
            logging.debug('{}'.format(rows))
        logging.debug('Read table')
    def read(self, table_name, column, value, read_column = '*'):
        query = "select {} from {} where {} = '{}'".format(read_column, table_name, column, value)
        print(query)
        self.c.execute(query)
        for rows in self.c.fetchall():
            logging.debug('{}'.format(rows))
        
        logging.debug('Read specific part of table')
    def update(self, table_name, column, value, search_column, search_value):
        query = "UPDATE {} SET {} = {} WHERE {} = '{}';".format(table_name, column, value, search_column, search_value)
        # print(query)
        self.c.execute(query)
        logging.debug('Updated table')
    def delete(self, table_name, column, value):
        logging.debug('Deleting part of table')
        self.c.execute("DELETE FROM {} WHERE {} = '{}'".format(table_name, column, value))
        self.conn.commit()
    def deleteTable(self, table_name):
        logging.debug('Deleting table')
        self.c.execute('drop table if exists ' + table_name)
    def close(self):
        logging.debug('Closing program')
        self.conn.commit()
        self.c.close()

# main = DataBase('main')

# main.deleteTable('player')

# main.createTable('player', columns = ['player_name', 'score', 'time', 'batting_avg'], data_types = ['STRING', 'INTEGER', 'INTEGER', 'INTEGER'])

# main.insert('player', values = ['Person1', '1000', '100000', '123890'])
# main.insert('player', values = ['Bob', '0', '0', '0'])

# main.readTable('player')
# main.read('player', 'score', '1000')

# main.update('player', 'score', '0', 'player_name', 'Bob')

# main.read('player', 'player_name', 'Bob')
# main.read('player', 'player_name', 'Bob', 'score')

# main.delete('player', 'player_name', 'Bob')

# main.readTable('player')