# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from HTMLTestRunner import HTMLTestRunner
from email.header import Header 
import smtplib,unittest,os,time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#=====定义发送邮件====
def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header(u"自动化测试报告","utf-8")
    smtp = smtplib.SMTP()
    smtp.connect("smtp.mxhichina.com")
    smtp.login("leichengliang@kuaiqiangche.com","Lei214811")
    smtp.sendmail("leichengliang@kuaiqiangche.com","lei214811@163.com",msg.as_string())
    smtp.quit()
    print('send success')

#====查找最新生成的测试报告====
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':
	
    test_dir = 'D:\\new_web\\test_case\\'
    testreport = 'D:\\new_web\\test_case\\report'

    discover = unittest.defaultTestLoader.discover(test_dir,pattern='kqc_*.py')
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = testreport + '\\' + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况')

    runner.run(discover) 
    fp.close()

    report = new_report(testreport)
    send_mail(report)  #发送测试报告   	

