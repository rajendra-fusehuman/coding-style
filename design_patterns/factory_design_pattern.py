from abc import ABC, abstractmethod
import logging
import sqlite3


class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass


class FileLogger(Logger):
    def __init__(self, filename):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
        file_handler = logging.FileHandler(filename)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def log(self, message):
        self.logger.info(message)


class ConsoleLogger(Logger):
    def log(self, message):
        print(message)


class DatabaseLogger(Logger):
    def __init__(self, dbname):
        self.connection = sqlite3.connect(dbname)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS logs (id INTEGER
                            PRIMARY KEY, message TEXT)''')
        self.connection.commit()

    def log(self, message):
        self.cursor.execute('''INSERT INTO logs (message) VALUES (?)''',
                            (message,))
        self.connection.commit()

    def __del__(self):
        self.connection.close()


class LoggerFactory:
    @staticmethod
    def get_logger(logger_type, filename=None):
        if logger_type == 'file':
            return FileLogger(filename)
        elif logger_type == 'console':
            return ConsoleLogger()
        elif logger_type == 'database':
            return DatabaseLogger(filename)
        else:
            raise ValueError('Invalid logger type')


if __name__ == "__main__":
    filename = "file-logger.logs"
    file_logger = LoggerFactory.get_logger('file', filename)
    file_logger.log('This is a file log message')

    console_logger = LoggerFactory.get_logger('console')
    console_logger.log('This is a console log message')

    dbname = 'database_logger.db'
    database_logger = LoggerFactory.get_logger('database', dbname)
    database_logger.log('This is a database log message')
