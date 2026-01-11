# email sending with python --


# pip install secure-smtplib    -> install this module

# module import--
import smtplib

# user input--
email = input("sender Email")
reciver = input("reciver Email") 

subject = input("subject..")
massage = input("massage..")


text = (f"subject {subject} \n \n {massage}")
server = smtplib.SMTP()