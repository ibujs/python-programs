import smtplib
from email.mime.text import MIMEText

print("Note that your email provider should support SMTP.")
print("Please type your email in a text editor and save it.")
msg = MIMEText(open(input("Enter the location of the file you saved:- ")).read())
print("The text in your file is now the body of your email.")

msg['Subject'] = input("Type the subject of the email:- ")
from_email = input("Enter your email address:- ")
msg['From'] = from_email
to_email = input("Type the email address to send the email to:- ")
msg['To'] = to_email
server = input("Enter the SMTP server of your email provider:- ")
password = input("Enter your password:- ")

try:
    server = smtplib.SMTP(server)
    server.starttls()
    server.login(to_email, password)
    server.sendmail(from_email, to_email, msg)
    server.quit()
    print("Email successfully sent.")
except:
    print("An error occurred.")