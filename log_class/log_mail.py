import smtplib
from email.message import EmailMessage
import datetime


class LogMail:

    def __init__(self, receiver_email_address, level, message, object):
        self.receiver_email_address = receiver_email_address
        self.level = level
        self.message = message
        self.object = object
        self.sender_email_address = "su_correo@gmail.com"

    def send_email(self):
        message = EmailMessage()

        message['Subject'] = 'Log aplicación ...'
        message['From'] = self.sender_email_address
        message['To'] = self.receiver_email_address
        email_smtp = "smtp.gmail.com"
        email_password = "clavequegeneragmail"

        now = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")

        background = 'RED'
        color = 'BLUE'

        if self.level == 'INFO':
            background = 'RED'
            color = 'BLUE'
        elif self.level == 'WARNING':
            background = 'BLCK'
            color = 'YELLOW'
        elif self.level == 'ERROR':
            background = 'BLUE'
            color = 'RED'
        elif self.level == 'DEBUG':
            background = 'BLACK'
            color = 'MAGENTA'

        wrapper = """
      <!DOCTYPE html> 
      <head> 
      </head>    
         <body>        
            <h1>Log Aplicación</h1>        
            <p style="background-color:%s; color:%s;">%s %s %s %s</p>        
         </body> 
      </html>
      """
        file_content = wrapper % (background, color, now, self.level, self.message, self.object)

        message.set_content(file_content, subtype='html')

        server = smtplib.SMTP(email_smtp, '587')
        server.ehlo()
        server.starttls()
        server.login(self.sender_email_address, email_password)
        server.send_message(message)
        server.quit()
