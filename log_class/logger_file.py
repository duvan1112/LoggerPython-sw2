import datetime as date

import log_class.logger as log_class

log_file = 'file.log'


class LoggerFile(log_class.Logger):
    def print_info(self, message, object):
        self.__printFile('INFO', message, object)

    def print_warning(self, message, object):
        self.__printFile('WARNING', message, object)

    def print_error(self, message, object):
        self.__printFile('ERROR', message, object)

    def print_debug(self, message, object):
        self.__printFile('DEBUG', message, object)

    def __printFile(self, nivel, message, object):
        with open(log_file, 'a') as file:
            data = f'{str(date.datetime.now())} [{nivel}] {message, str(object)}\n'
            file.writelines(data)
