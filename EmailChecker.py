import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
mail = input("Enter your mail : ")
if re.search(email_condition,mail):
    print("Correct mail ")
else:
    print("Incorrect mail")