import smtplib,codecs,os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

load_dotenv()

def readHtml():
    file = ""
    with open("amazon_scam.html",'r') as f:
        file = f.read()
        f.close()
    return file
styles = {"font_family":"font-family: Arial, Helvetica, sans-serif;","color":"color: rgb(255,133,0)","amazon_page":"https://lit-lowlands-12540.herokuapp.com/"}

msg = MIMEMultipart('related')
password = os.getenv("PASS")
msg['Subject'] = "Amazon Scam"
msg['From'] = os.getenv("EMAIL")
msg['To'] = "jose45321@outlook.com"

html = readHtml().format_map(styles)
msgBody = MIMEText(html,"html")
msg.attach(msgBody)

logo = open("./logo.png",'rb')
msgImage = MIMEImage(logo.read())
logo.close()
msgImage.add_header("Content-ID","<logo>")
msg.attach(msgImage)
servidor=smtplib.SMTP('smtp.gmail.com:587')
servidor.starttls()
servidor.login(msg["From"], password)
servidor.sendmail(msg["From"],msg["To"],msg.as_string())
servidor.quit()

