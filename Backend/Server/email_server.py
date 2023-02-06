import logging

from Model import EmailModel
from Utils import ConfigType, WawuConfig

from smtplib import SMTP, SMTPException
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

class EmailServer:
    
    def __init__(self) -> None:
        self.email_model: EmailModel = EmailModel(WawuConfig("./Data/EmailConfig.json", ConfigType.json).get_config())
        
    def send(self, subject: str, raw_msg: dict[str, str], picture: dict[str, str]) -> None:
        msg = MIMEMultipart("related")
        msg["From"] = Header(self.email_model.send_name, "utf-8")
        msg["To"] = self.email_model.get_email
        msg["Subject"] = subject
        
        content = MIMEText(self.email_model.render_template(raw_msg), "html", "utf-8")
        msg.attach(content)
        
        if picture is not None:
            for key, value in picture.items():
                with open(f"./Resources/Images/{value}.png", "rb") as image:
                    msgImage = MIMEImage(image.read())
                msgImage.add_header("Content-ID", f"{key}")
                msg.attach(msgImage)
        
        try:
            smtp = SMTP()
            smtp.connect("smtp.qq.com")
            smtp.login(self.email_model.send_email, self.email_model.author_code)
            smtp.sendmail(self.email_model.send_email, self.email_model.get_email, msg.as_string())
            logging.info("邮件发送成功")
            logging.getLogger("server").info("邮件发送成功")
        except SMTPException:
            logging.warning("邮件发送失败")
            logging.getLogger("server").warning("邮件发送失败")
        finally:
            smtp.quit()
