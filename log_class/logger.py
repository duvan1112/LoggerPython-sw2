from abc import ABC, abstractmethod


class Logger(ABC):

    @abstractmethod
    def print_info(self, message, object): pass

    @abstractmethod
    def print_warning(self, message, object): pass

    @abstractmethod
    def print_error(self, message, object): pass

    @abstractmethod
    def print_debug(self, message, object): pass
