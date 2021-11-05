def emailchecker(mail):
    if mail.count("@") == 1 and mail.count(".") >= 1 in mail:
        return True
    else:
        return False
try_mail = str(input("Please type your mail:"))
if emailchecker(try_mail) == True:
    print("You can use this mail :)")
else:
    print("Try another one :(")







