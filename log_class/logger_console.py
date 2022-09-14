import datetime as date

from colorama import init, Fore

import log_class.logger as log_class

init(autoreset=True)


class LoggerConsole(log_class.Logger):

    def print_info(self, message, object):
        print(f'{Fore.BLUE}{date.datetime.now()} [INFO] {message, object}')

    def print_warning(self, message, object):
        print(f'{Fore.YELLOW}{date.datetime.now()} [WARNING] {message, object}')

    def print_error(self, message, object):
        print(f'{Fore.RED}{date.datetime.now()} [ERROR] {message, object}')

    def print_debug(self, message, object):
        print(f'{Fore.MAGENTA}{date.datetime.now()} [DEBUG] {message, object}')
