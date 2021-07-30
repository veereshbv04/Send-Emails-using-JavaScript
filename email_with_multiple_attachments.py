import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
fromaddr = "veereshbvvee@gmail.com"
password="" #this is the password of senders email id

email_list =["vebv18cs@cmrit.ac.in","veereshbv04@gmail.com"]
file_list = ["email1.pdf","email2.pdf"]

for emailidtosend,filetosend in zip(email_list,file_list):
    

    toaddr = emailidtosend
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Test email attachment multi"
    body = "This is test mail"
    msg.attach(MIMEText(body, 'plain'))
    
    folder=r"C:\Users\Veeresh B V\Downloads\emailtest"
    path_of_file = os.path.join(folder,filetosend)
    attachment = open(path_of_file, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filetosend)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, password)
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)

print("all email sent succesfully")

s.quit()
print("ending")
