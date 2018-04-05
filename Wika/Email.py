import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
 
fromaddr = "wikabangunangedung@gmail.com"
toaddr = "bagustyo92@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Test"
 
body = "YOUR MESSAGE HERE"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 465)
server.starttls()
server.login(fromaddr, "w1k4gedung")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()