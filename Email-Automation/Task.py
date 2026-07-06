import os,shutil,smtplib                 # import os:- Operating System se baat karna — file paths, folders ke liye
from datetime import datetime            # import shutil:- Files/folders copy, move, zip karne ke liye
from email.mime.text import MIMEText     # import smtplib:- Email bhejne ke liye (Gmail server se connect)

def check_logs(filepath):                # filepath:- konsi log file check karni hai -- bahar se denge
    errors=[]                            # []:- khali list banao-- errors yaha store honge
    with open(filepath,"r") as f:        # with:- file kaam ke baad automatically band ho jaaye
        for line in f:                   # open() → File kholo        #filepath → Konsi file — jo parameter mein aya
            if "ERROR" in line:          # "r" → r = read mode — sirf padhna hai, likhna nahi          # as f → File ko f naam do (shortcut)
                errors.append(line.strip())         # errors.append() → List mein nayi cheez daalo
                                 # line.strip() → Line ke aage peeche ke spaces aur \n hatao           #.strip() → Clean karna
        return errors                    # return → Function se bahar bhejo — jo errors mile woh wapas do

def backup_data(source,backup_dir):      # source → Konsa folder backup karna hai
                                         # backup_dir → Backup kahan save karna hai

    #source="/mnt/d/important_data" #for windows use: "D:/test_folder"
    #backup_dir="/mnt/d/backups" # for windows use: "D:/backups"
    timestamp=datetime.now().strftime("%Y%m%d%H%M%S")     #(year,month,day,hour,minutes,second)
    backup_file=os.path.join(backup_dir,f"backup_{timestamp}.zip")     # os.path.join() → Folder + filename ko sahi se jodo
    shutil.make_archive(backup_file.replace('.zip',''),'zip',source)   # shutil.make_archive() → ZIP file banao
    return backup_file                      # Backup file ka poora path wapas bhejo

def send_email(subject,body):
    send_email="mansoorikaif365@gmail.com"
    reciever_email="mansoorimohdkaif786@gmail.com"
    password="egri bxzp rhxl otja"

    msg=MIMEText(body)
    msg["subject"]=subject
    msg["From"]=send_email
    msg["To"]=reciever_email

    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls()
        server.login(send_email,password)
        server.send_message(msg)


# Main Program — Sab Kuch Chalta Hai Yahan
                                     # check_logs() function chalaao
                                     # Jo errors mile woh errors variable mein aa jaayenge
errors= check_logs("system.log")     # "system.log" → Yeh file padhni hai
if errors:                           # if errors: → Agar list khali nahi hai toh andar jaao
                                     # Agar errors = [] (khali) → condition False
                                     # Agar errors = ["ERROR: disk full"] → condition True
    backup_path=backup_data("/mnt/d/important_data","/mnt/d/backups")
    send_email("! Error Detected- Backup Done", f"Errors:\n {chr(10).join(errors)}\n Backup: {backup_path}")
    print("Task Done with Error Notification")  # "! Error Detected- Backup Done"
else:                                           # ! → Attention ke liye — urgent dikhta hai
    print("No Errors Detected")