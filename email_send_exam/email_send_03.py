import requests
#import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

url = r'https://free-api.heweather.net/s6/weather/forecast?location=����&key=c39a12e36f2b4b16b3116c1cb735e78e'
current_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))

def get_weather_data():
    res = requests.get(url).json()
    result = res['HeWeather6'][0]['daily_forecast']
    location = res['HeWeather6'][0]['basic']
    city = location['parent_city']
    names = ['����', 'ʱ��', '����״��', '�����', '�����', '�ճ�', '����']
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
    # ������������
    HOST = 'smtp.qq.com'
    # �����������
    SUBJECT = f'{current_date}����Ԥ����Ϣ�������'
    # ���÷�����
    FROM = '1223771248@qq.com'
    # �����ռ���
    TO = '337323012@qq.com, c2928567@163.com' #ͬʱ���Ͷ���ռ���
    message = MIMEMultipart('related')

    # �����ʼ�����
    message_html = MIMEText(f'{current_date}����Ԥ����Ϣ�������\n'
                            f'���У�{city}\n'
                            f'����״����{cond}\n'
                            f'����£�{max}��\n'
                            f'����£�{min}��\n'
                            f'�ճ���{sr}\n'
                            f'���䣺{ss}\n', 'plain', 'utf-8')
    message.attach(message_html)

    # ��Ӹ���
    #message_xlsx = MIMEText(open('today_weather.csv', 'rb').read(), 'base64', 'utf-8')
    # �����ļ��ڸ���������
    #message_xlsx['Content-Disposition'] = 'attachment;filename="today_weather.csv"'
    #message.attach(message_xlsx)


    # �����ʼ�������
    message['From'] = FROM
    # �����ʼ��ռ���
    message['To'] = TO
    # �����������
    message['Subject'] = SUBJECT


    # ��ȡ���ʼ�����Э��֤��
    email_client = smtplib.SMTP_SSL(host='smtp.qq.com')
    # ���÷���������������Ͷ˿�
    email_client.connect(HOST, '465')

    # ������Ȩ��
    result = email_client.login(FROM, 'wovbdmwfcsotjejj')
    print(f'��¼���{result}')
    email_client.sendmail(from_addr=FROM, to_addrs=TO.split(','), msg=message.as_string())

    # �ر��ʼ����Ϳͻ���
    email_client.close()

get_weather_data()