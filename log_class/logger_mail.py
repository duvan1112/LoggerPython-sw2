import log_class.log_mail as log_mail
import log_class.logger as log_class

receiver_email_address = 'destino@uptc.edu.co'


class LoggerMail(log_class.Logger):

    def print_info(self, message, object):
        self.__printMail(receiver_email_address, 'INFO', message, object)

    def print_warning(self, message, object):
        self.__printMail(receiver_email_address, 'WARNING', message, object)

    def print_error(self, message, object):
        self.__printMail(receiver_email_address, 'ERROR', message, object)

    def print_debug(self, message, object):
        self.__printMail(receiver_email_address, 'DEBUG', message, object)

    def __printMail(self, receiver_email_address, nivel, message, object):
        mail_log = log_mail.LogMail(receiver_email_address, nivel, message, object)
        mail_log.send_email()
