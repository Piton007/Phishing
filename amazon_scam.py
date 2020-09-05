import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

styles = {"font_family":"font-family: Arial, Helvetica, sans-serif;","color":"color: rgb(255,133,0)"}

msg = MIMEMultipart('related')
password = "Joseluis123qwe"
msg['Subject'] = "Amazon Scam"
msg['From'] = "josemowa@gmail.com"
msg['To'] = "jose45321@outlook.com"

html = """\
<html >
<head>
</head>
<body>
    <header style="border-bottom: 2px solid gray;">
        <img src="cid:logo" alt="Amazon Logo" >
    </header>
    <main>
        <h2 style="{color}; font-family: {font_family} font-weight: lighter;">Your Amazon account has been locked</h2>
        <p style="{font_family}">Dear customer</p>
        <p style="{font_family}">Lorem ipsum dolor sit amet consectetur adipisicing elit. Sit ipsum eaque exercitationem quibusdam commodi ea dicta qui? Cupiditate esse quia consectetur repudiandae repellat labore repellendus! Dolore deserunt magni similique et.</p>
        <p style="{font_family}">Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus modi recusandae saepe nulla molestiae iste vero officia rem nihil autem possimus quas eius est assumenda, non facere id eum qui.</p>
        <p style="{font_family}">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Tenetur provident accusantium consequatur, corrupti, soluta quo dolor debitis quis blanditiis saepe odio officiis ipsam? Facilis, explicabo. Accusamus asperiores quo deserunt architecto.</p>
        <a style="{color};text-decoration: none;font-size: 1.5rem;font-family: Arial, Helvetica, sans-serif; "  href="http://google.com" target="_blank">How do I unlock my account?</a>
        <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Qui veritatis amet nesciunt sapiente nam molestias temporibus! Cum eveniet in vel, ab nam maxime beatae quas eius quos sit repellendus minima.</p>
        <a href="http://google.com" target="_blank" style="display: block;width: 10rem; height: 2.5rem;line-height: 3.0; margin: 0 auto; text-decoration: none;color: white;background: rgb(255,133,0); text-align:center; font-family: Arial, Helvetica, sans-serif;"> Verify your Account</a>
    </main>
    <footer style="margin-top:2rem">
        Amazon Services &copy; 2020 | All Rights Reserved
    </footer>
</body>
</html> 
""".format_map(styles)
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

