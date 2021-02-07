import pymysql
import datetime
from termcolor import colored
from json import load


class Shark(object):
    """
    Class Shark serves as a description of all tables for the database.
    Here you create tables based on the description and return a dictionary with the connection, the connection cursor.
    A class of a small ORM system that implements simple CRUD queries and create table's.
    It is desirable to inherit this class, for more flexible use.
    """

    def __init__(self):
        """
        Initialize the fields in the connection settings to the database.
        Defining and writing an array of superusers.
        """
        self.path = "/home/cosmobot/Freelance/apartment_renovation/"
        self.db_connect = load(open(file=f"{self.path}shark/data_connect.json", mode="r", encoding="UTF-8"))
        self.host = self.db_connect['host']
        self.port = int(self.db_connect['port'])
        self.unix_socket = self.db_connect['unix_socket']
        self.db = self.db_connect['db']
        self.user = self.db_connect['user']
        self.password = self.db_connect['password']
        self.log_db = self.db_connect['log_db']


    def connect(self) -> dict:
        """
        Method of connecting to the database.
        Returns: return=>connect, :return=>cursor
        """
        try:
            connect = pymysql.connect(host=self.host, port=self.port, unix_socket=self.unix_socket,
                                                db=self.db, user=self.user ,password=self.password)
            cursor = connect.cursor()
            return {'connect': connect, 'cursor': cursor}
        except ValueError as error:
            print(f"{colored('[BOT]', 'yellow')}: {error}")
            fb = open(self.log_db, "a")
            return fb.write(f"[{datetime.datetime.now()}: {error}]\n")
        except TypeError as error:
            print(f"{colored('[BOT]', 'yellow')}: {error}")
            fb = open(self.log_db, "a")
            return fb.write(f"[{datetime.datetime.now()}: {error}]\n")
        except pymysql.err.OperationalError as error:
            print(f"{colored('[BOT]', 'yellow')}: {error}")
            fb = open(self.log_db, "a")
            return fb.write(f"[{datetime.datetime.now()}: {error}]\n")



    def installation_encoding(self,tablename=None, encode=['utf8', 'utf8_general_ci']):
        """
            Convertation encode for tables
            :param encode -> dict
            :param tablename -> str
        """
        connect = self.connect()
        try:
            sql = f"ALTER TABLE {tablename} CONVERT TO CHARACTER SET {encode[0]} COLLATE {encode[1]};"
            connect['cursor'].execute(sql)
            return connect['connect'].commit() # Пока так изменить на обработчик ошибок
        except ValueError as error:
            print(f"{colored('[BOT]', 'yellow')}: {error}")
            fb = open(self.log_db, "a")
            return fb.write(f"[{datetime.datetime.now()}: {error}]\n")


    def create_table(self,  sql=None):
        # Creating a single table
        # :param sql -> str
        try:
            print(f"{colored('[Ok]', 'blue')}")
            connect = self.connect()
            connect['cursor'].execute(sql)
            return connect['connect'].commit() # Пока так изменить на обработчик ошибок
        except KeyError as error:
            print(f"{colored('[BOT]', 'yellow')}: {error}")
            fb = open(self.log_db, "a")
            return fb.write(f"[{datetime.datetime.now()}: {error}]\n")
        except pymysql.err.OperationalError as error:
            print(f"{colored('[BOT]', 'yellow')}: {error}")
            fb = open(self.log_db, "a")
            return fb.write(f"[{datetime.datetime.now()}: {error}]\n")


    """
    Description of CRUD methods. Each method is responsible for a single operation 
    and needs to pass the connection session to the database, by passing keys to the 
    method arguments.
    """

    def insert(self, connect, cursor, table, **kwargs):
        """
        Method for writing data to a table.
            :param connect -> key session:
            :param cursor -> param session:
            :param table -> where to write it down:
            :param kwargs -> the data dictionary:
        """
        sql = f"INSERT INTO {table}("
        # Collection of array keys
        for k in kwargs.keys():
            sql += f"{k}, "
        sql += ") VALUES("
        # Collection of array values
        for v in kwargs.values():
            sql += f"'{v}', "
        sql += ");"
        print(sql.replace(', )', ')'))
        try:
            cursor.execute(sql.replace(', )', ')'))
            return connect.commit()
        except pymysql.err.IntegrityError as error:
            print(f"{colored('[BOT]', 'yellow')}: {error}")
            fb = open(self.log_db, "a")
            return fb.write(f"[{datetime.datetime.now()}: {error}]\n")
        except AttributeError as error:
            print(f"{colored('[BOT]', 'yellow')}: {error}")
            fb = open(self.log_db, "a")
            return fb.write(f"[{datetime.datetime.now()}: {error}]\n")


    def select_all(self, cursor=None, table=None, param_search=None):
        """
        A method of comparing search data
            :param cursor -> key session:
            :param table -> search table:
            :param param_search -> Desired value, can be several:
        """

        cursor.execute(f"SELECT {param_search} FROM {table};")
        return cursor.fetchall()


    def select(self, cursor=None, table=None, param_search=None, value_key=None, value=None, k=None, v=None, data=None):
        """
        A method of comparing search data
            :param cursor -> key session:
            :param table -> search table:
            :param param_search -> Desired value, can be several :
            :param value_key -> search key:
            :param, value -> search for the value:
            :param k -> advanced key:
            :param v -> additional value:
            :param data -> Accepts 3 types at the moment (tuple, number, string):
        """
        data_all = []  # List for writing data

        if data == 'str':
            cursor.execute(f"SELECT {param_search} FROM {table} WHERE {value_key}='{value}';")
            return str(cursor.fetchone()).replace("('", "").replace("',)", "")

        elif data == 'str' and k and v:
            cursor.execute(f"SELECT {param_search} FROM {table} WHERE {value_key}='{value}' AND {k}='{v}';")
            print(str(cursor.fetchone()).replace("('", "").replace("',)", ""))
            return str(cursor.fetchone()).replace("('", "").replace("',)", "")

        elif data == 'int':
            cursor.execute(f"SELECT {param_search} FROM {table} WHERE {value_key}='{value}';")
            return str(cursor.fetchone()).replace("('", "").replace("',)", "")

        elif data == 'tuple':
            cursor.execute(f"SELECT {param_search} FROM {table} WHERE {value_key}='{value}';")
            for f in cursor.fetchall():
                data_all.append(f)
            return data_all


    def no_select(self, cursor=None, table=None, param_search=None, no_value_key=None,
                    no_value=None, value_key=None, value=None, desc=None, if_value=None):
        """
        Data selection by logical condition.
            :param cursor -> cursor key session:
            :param table -> name table to select:
            :param param_search -> search parameters:
            :param value_key -> search key:
            :param no_value -> value up to:
        """
        data_all = []  # List for writing data
        if no_value or no_value_key:
            cursor.execute(f"SELECT {param_search} FROM {table} WHERE {no_value_key} != '{no_value}';")
            for f in cursor.fetchall():
                data_all.append(f)
            return data_all
        elif no_value and no_value_key and value and value_key and desc and if_value:
            cursor.execute(
                f"""SELECT {param_search} FROM {table} 
                        WHERE {no_value_key} != '{no_value}' AND {value_key}  == '{value}' AND {if_value.keys()} == '{if_value.values()}'
                        ORDER BY {desc} DESC;""")
            for f in cursor.fetchall():
                data_all.append(f)
            return data_all


    def update(self, connect=None, cursor=None, table=None, k=None, v=None,
               value_key=None, value=None, and_value_key=None, and_value=None):
        """
        Update the data
            :param -> connect key session:
            :param cursor -> cursor key session:
            :param table -> name table to update:
            :param k -> replacement key:
            :param v -> new parameter:
            :param value_key -> search key:
            :param value -> value up to:
            :param and_value_key -> add search key:
            :param and_value -> add value up to:
        """
        if value_key and value:
            cursor.execute(f"UPDATE {table} SET {k}='{v}' WHERE {value_key}='{value}';")
            return connect.commit()
        elif value_key and value and and_value_key and and_value:
            cursor.execute(
                f"UPDATE {table} SET {k}='{v}' WHERE {value_key}='{value}' AND {and_value_key}='{and_value}';")
            return connect.commit()
        else:
            cursor.execute(f"UPDATE {table} SET {k}='{v}';")
            return connect.commit()

    def delete(self, connect=None, cursor=None, table=None, value_key=None, value=None):
        """
        Deleting data.
            :param connect -> connect key session:
            :param cursor -> cursor key session:
            :param table -> name table to delete:
            :param value_key -> search key:
            :param value -> the value removal:
        """
        cursor.execute(f"DELETE FROM {table} WHERE {value_key}='{value}';")
        return connect.commit()