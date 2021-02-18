import smtplib
import getpass
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
print(smtp_object.ehlo())
print(smtp_object.starttls())

email = input("Enter your E-mail id:  ")
password = getpass.getpass("Enter Password :  ")
smtp_object.login(email, password)

from_address = input("Enter your email: ")
to_address = input("Enter the email of the recipient: ")
subject = input("Enter the subject line: ")
message = input("Type out the message you want to send: ")

msg = 'Subject:' + subject + '\n' + message

smtp_object.sendmail(from_address, to_address, msg)

print(smtp_object.quit())