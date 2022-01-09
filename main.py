import os
import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header


parameters = {
    "access-key" : os.environ.get("ACCESS_KEY"),
    "secret-key" : os.environ.get("SECTET_KEY"),
    "size" : 10
}

response = requests.get("http://www.coderutil.com/api/resou/v1/weibo",params=parameters)
response.raise_for_status()
data = response.json()["data"]
data_rank = []
data_title = []
data_url = []
data_msg_dict = {}
finalmessage = []
i = 0
for data_index in data:
    data_rank.append(data_index["rank"])
    data_title.append(data_index["keyword"])
    data_url.append(data_index["url"])
    if i < 20:
        data_msg_dict.update({
            f"排名{i+1}" : data_rank[i],
            f"热搜标题{i+1}": data_title[i],
            f"网址{i+1}": data_url[i],

        })
        i += 1
    # data_msg_turple = (data_rank,data_title,data_url)
    # data_msg.append(data_msg_turple)
for key, value in data_msg_dict.items():
    finalmessage.append(value)
    finalmessage_format = []
    for i in range(10):
        exec ("finalmessage_value%s=finalmessage[i*3:(i+1)*3]"%(i+1))
    # finalmessage_value1 = finalmessage[0:3]
    # finalmessage_value2 = finalmessage[3:6]
    # finalmessage_value3 = finalmessage[6:9]
    # finalmessage_value4 = finalmessage[9:12]
    # finalmessage_value5 = finalmessage[12:15]
    # finalmessage_value6 = finalmessage[15:18]
    # finalmessage_value7 = finalmessage[18:21]
    # finalmessage_value8 = finalmessage[21:24]
    # finalmessage_value9 = finalmessage[24:27]
    # finalmessage_value10 = finalmessage[27:30]

def send_email():
    from_email = os.environ.get("FROM_EMAIL")
    password = os.environ.get("PASSWORD")
    to_email = os.environ.get("TO_EMAIL")
    conection = smtplib.SMTP("smtp.qq.com")
    conection.starttls()
    conection.login(user=from_email,password=password)
    msg = MIMEText(f"{str(finalmessage_value1)}\n{str(finalmessage_value2)}\n{str(finalmessage_value3)}\n{str(finalmessage_value4)}\n{str(finalmessage_value5)}\n{str(finalmessage_value6)}\n{str(finalmessage_value7)}\n{str(finalmessage_value8)}\n{str(finalmessage_value9)}\n{str(finalmessage_value10)}\n","plain","utf-8")
    msg["Subject"] = Header("微博热搜", 'utf-8')
    msg["From"] = from_email
    msg["To"] = from_email
    conection.sendmail(from_addr=from_email,to_addrs=to_email,msg=msg.as_string())
    conection.close()

send_email()