import smtplib
from email.mime.text import MIMEText

def send_email(subject,body):
    sender_email="mansoorikaif365@gmail.com"
    reciever_email="mansoorimohdkaif786@gmail.com"
    password="egri bxzp rhxl otja"

    msg=MIMEText(body)
    msg["subject"]=subject
    msg["From"]=sender_email
    msg["To"]=reciever_email

    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls()
        server.login(sender_email,password)
        server.send_message(msg)

send_email("Backup Completed","Backup created successfully")

'''
###########################################################################
smtplib → SMTP = Simple Mail Transfer Protocol. Yeh library email bhejne ke 
          liye use hoti hai (Gmail ke server se connect karti hai)
MIMEText → MIME = Multipurpose Internet Mail Extensions. Yeh email ka format 
           banata hai (subject, body, sender, receiver sab set karta hai)

############################################################################
def → Function banana ke liye keyword
send_email → Function ka naam
subject, body → Parameters — jo bahar se doge woh andar aayenge

############################################################################

sender_email → Kaun bhej raha hai
receiver_email → Kise bheja jaayega
password → Yeh normal Gmail password nahi hai — yeh App Password hai jo 
           Gmail settings se generate hota hai (2-step verification ke baad)

############################################################################
           
Line                Kya karta 
haiMIMEText(body)   Email ka body/content set karo
msg["Subject"]      Email ka subject set karo
msg["From"]         Sender ka address set karo
msg["To"]           Receiver ka address set karo

Line                                        Explanation
with ... as server:                         Server se connection kholo, kaam ho jaaye to automatically band karo
smtplib.SMTP("smtp.gmail.com", 587)         Gmail ke SMTP server se port 587 pe connect karo
server.starttls()                           TLS encryption shuru karo — connection secure ho jaata hai (data encrypt hota hai)
server.login(...)                           Gmail account mein login karo   
server.send_message(msg)                    Email bhejo

##############################################################################

Yahan function ko actually call kiya gaya hai
"Backup Completed" → subject mein jaayega
"Backup created successfully" → body mein jaayega

'''