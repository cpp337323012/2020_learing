import requests
#import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

url = r'https://free-api.heweather.net/s6/weather/forecast?location=永州&key=c39a12e36f2b4b16b3116c1cb735e78e'
current_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))

def get_weather_data():
    res = requests.get(url).json()
    result = res['HeWeather6'][0]['daily_forecast']
    location = res['HeWeather6'][0]['basic']
    city = location['parent_city']
    names = ['城市', '时间', '天气状况', '最高温', '最低温', '日出', '日落']
    #with open('today_weather.csv', 'w', newline='') as f:
        #writer = csv.writer(f)
        #writer.writerow(names)
    for data in result:
        date = data['date']
        cond = data['cond_txt_d']
        max = data['tmp_max']
        min = data['tmp_min']
        sr = data['sr']
        ss = data['ss']
            #writer.writerows([(city, date, cond, max, min, sr, ss)])
    send_email(city,cond,max,min,sr,ss)

def send_email(city,cond,max,min,sr,ss):
    # 设置邮箱域名
    HOST = 'smtp.qq.com'
    # 设置邮箱标题
    SUBJECT = f'{current_date}天气预报信息，请查收'
    # 设置发件人
    FROM = '1223771248@qq.com'
    # 设置收件人
    TO = '337323012@qq.com, c2928567@163.com' #同时发送多个收件人
    message = MIMEMultipart('related')

    # 发送邮件正文
    message_html = MIMEText(f'{current_date}天气预告信息，请查收\n'
                            f'城市：{city}\n'
                            f'天气状况：{cond}\n'
                            f'最高温：{max}℃\n'
                            f'最低温：{min}℃\n'
                            f'日出：{sr}\n'
                            f'日落：{ss}\n', 'plain', 'utf-8')
    message.attach(message_html)

    # 添加附件
    #message_xlsx = MIMEText(open('today_weather.csv', 'rb').read(), 'base64', 'utf-8')
    # 设置文件在附件中名字
    #message_xlsx['Content-Disposition'] = 'attachment;filename="today_weather.csv"'
    #message.attach(message_xlsx)


    # 设置邮件发件人
    message['From'] = FROM
    # 设置邮件收件人
    message['To'] = TO
    # 设置邮箱标题
    message['Subject'] = SUBJECT


    # 获取简单邮件传输协议证书
    email_client = smtplib.SMTP_SSL(host='smtp.qq.com')
    # 设置发件人邮箱的域名和端口
    email_client.connect(HOST, '465')

    # 邮箱授权码
    result = email_client.login(FROM, 'wovbdmwfcsotjejj')
    print(f'登录结果{result}')
    email_client.sendmail(from_addr=FROM, to_addrs=TO.split(','), msg=message.as_string())

    # 关闭邮件发送客户端
    email_client.close()

get_weather_data()