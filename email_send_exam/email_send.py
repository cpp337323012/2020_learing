import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
import requests
import ast

def get_url_comment(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400"
    }
    try:
        r = requests.get(url ,headers = headers, timeout = 30)#获得url的相关参数
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print ("网页获取成功",r.status_code )
        return r.text
    except Exception as e :
        return "网页爬取异常" , r.status_code ,e#返回状态码
def weather():
    a = get_url_comment("https://tianqiapi.com/api?version=v6&appid=15186356&appsecret=swW9lQmQ")
    b = ast.literal_eval(a)
    c = b["date"] + "\t" + b["week"] + "\t" + b["city"] + "\n" + b["wea"] + "\n最高气温 " + b["tem1"] + "℃" \
        + "  --最低气温 " + b["tem2"] + "℃\n" + b["win"] + b["win_speed"] + "\n空气质量 " + b["air"] + "\t空气PM2.5指数 " \
        + b["air_pm25"] + "\t空气水平 " + b["air_level"] + "\t" + b["air_tips"]
    if int(b["tem2"]) <= 0 and int(b["tem1"]) >= 10:
        d = "\n早安宝贝，早晨傍晚会比较冷，昼夜温差大，记得早晚添衣保暖哦！"
    elif int(b["tem2"]) >= 0 and int(b["tem2"]) <= 6 and int(b["tem1"]) >= 10:
        d = "\n早安宝贝，早晚都不算太冷，但记得添衣哦！"
    elif int(b["tem2"]) >= 6 and int(b["tem1"]) >= 10:
        d = "\n早安宝贝，天气转暖，宝贝，开心的一天啊！☺"
    elif int(b["tem2"]) <= -5 and int(b["tem1"]) <= 10:
        d = "\n早安宝贝，天气有点凉，注意保暖哦！❤"
    return c+d

def set_pic_file(text):
    print ("邮件发送中")
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "1223771248@qq.com"  # 用户名
    mail_pass = "wovbdmwfcsotjejj"  # 口令,QQ邮箱是输入授权码，在qq邮箱设置 里用验证过的手机发送短信获得，不含空格
    sender = '1223771248@qq.com'
    receivers = ['337323012@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    message = MIMEText(text, 'plain', 'utf-8')
    message['From'] = Header("1223771248@qq.com", 'utf-8')
    message['To'] = Header("337323012qq.com", 'utf-8')
    subject ='今天依然爱你哦'#标题
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print ("邮件发送成功")
    except smtplib.SMTPException as e:
        print (e)


if __name__ == '__main__':
    c, d = 9, 0
    while True:  # 设置循环，在服务器后台运行
        a, b = time.localtime(time.time()).tm_hour, time.localtime(time.time()).tm_min
        if a == c and b == d:
            e = weather()
            set_pic_file(e)
            print(time.localtime(time.time()).tm_year, "年--", time.localtime(time.time()).tm_mon,"月",time.localtime(time.time()).tm_mday,"日--",a,"：",b)
            time.sleep(24*3600-120)