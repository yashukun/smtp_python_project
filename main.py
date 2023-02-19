# import smtplib
# import pandas
#
# # dt = pandas.read_csv("mails.csv")
# #
# #
# # for mail in dt.iterrows():
# #     print(mail)
# #
#
#
# def function(the_mail: str):
#     my_email = "yashagarwaltest96@gmail.com"
#     password = "vtdjimprqlzkskjw"
#     with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr=my_email, to_addrs=the_mail,
#                             msg=f"Subject:no-reply")
#
#
# with open("mails2.csv") as dt:
#     data = dt.readlines()
#
#
# for mail in data:
#     mail = mail.strip("\n")
#     print(mail)
#     if mail == "Emails":
#         pass
#     else:
#         function(mail)
#

#
# my_email = "yashagarwaltest96@gmail.com"
# password = "vtdjimprqlzkskjw"
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs=the_mails,
#                         msg=f"Subject:no-reply")
#

import pyperclip
pyperclip.copy("yash")
p = pyperclip.paste()
