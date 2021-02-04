import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from json import load


class LibMail(object):
    """
    Модуль предназначин для различных операций с электронной почтой.
    
    """
    
    def __init__(self):
        self.data = load(open("data.json", mode="r", encoding="UTF-8"))


    def send_mail(self, title,  msg_send, user_email):
        """
        Sending an email, the email contains a link to the account confirmation page.
        The link is only valid for 3 days. After three days, the link will be invalid.
        """

        addr_from = self.data["email"]
        addr_to = user_email
        password = self.data["password"]

        msg = MIMEMultipart()
        msg['From'] = addr_from
        msg['To'] = addr_to
        msg['Subject'] = title

        html=msg_send

        part = MIMEText(html, "html")
        msg.attach(part)

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(addr_from, password)
        server.send_message(msg=msg, from_addr=addr_from, to_addrs=addr_to)
        server.quit()