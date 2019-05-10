"""
邮件类。用来给指定用户发送邮件。可指定多个收件人，可带附件。
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from utils.log import logger
from utils.config import Config

class send_email(object):
    def __init__(self):
        config=Config("mail_config.yaml")
        self.addresser=config.get("addresser")   #发送人地址
        self.addressee=config.get("addressee")     #收件人地址
        self.smtp=config.get("smtp")               #smtp地址
        self.user=config.get("user")               #发送邮箱账号
        self.passwd=config.get("passwd")           #邮箱密码
        self.log=logger
    def email_init(self,report,reportName):
        with open(report,'rb')as f:
            mail_body = f.read()
        # 创建一个带附件的邮件实例
        msg = MIMEMultipart()
        report_file = MIMEApplication(mail_body)
        # 定义附件名称（附件的名称可以随便定义，你写的是什么邮件里面显示的就是什么）
        report_file.add_header ('Content-Disposition', 'attachment', filename=reportName)
        msg.attach(report_file) # 添加附件
        msg['Subject'] = '自动化测试报告: '+reportName # 邮件标题
        msg['From'] = self.addresser  #发件人
        msg['To'] = ",".join(self.addressee) #收件人列表
        try:
            server = smtplib.SMTP(self.smtp)
            server.login(self.user,self.passwd)
            server.sendmail(self.addresser,self.addressee,msg.as_string())
            server.quit()
            self.log.info("----邮件发送成功,如果没有收到邮件，请检查垃圾箱，同时检查收件人地址是否正确----")
        except smtplib.SMTPException as e:
            self.log.info("邮件发送失败,失败原因：{}".format(e))
if __name__ == '__main__':
    email=send_email()
    email.email_init(r"E:\python_project\meetyou_automation\report\report.html","密友圈自动化测试.html")
