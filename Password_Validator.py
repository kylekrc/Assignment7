#        Program 2: Password validator

# The program will check if the entered password is valid

# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc)


def intro():
    print("Good day! The program will ask for a password and will determine whether it is valid or not.")
    print("Upon inputting, please follow the criteria below.")
    print("CRITERIA:\na. Greater than 15 letters\nb. Have at least one capital letter\nc. Have at least one number\nd. Have at least one special char (!@#$%^&*()_+ etc.)")

intro()

def pass_validity():
    Input_pass = str(input("Enter password: "))
    return Input_pass

validity = pass_validity()

criteria_1_req, criteria_2_req, criteria_3_req, criteria_4_req = 0, 0, 0, 0

for inp in validity:
    if (len(validity) >= 15):
        criteria_1_req += 1
    else:
        criteria_1_req += 0
    
if any(inp.isupper() for inp in validity):
    criteria_2_req += 1
else:
    criteria_2_req += 0
    
if any(inp.isdigit() for inp in validity):
    criteria_3_req += 1
else:
    criteria_3_req += 0

if any (inp in "!”#$%&'()*+,-./:;<=>?@[\]^_`{|}~" for inp in validity):
    criteria_4_req += 1
else:
    criteria_4_req += 0

if criteria_1_req >= 1 and criteria_2_req >= 1 and criteria_3_req >= 1 and criteria_4_req >= 1:
    print("Valid Password.")
    
elif criteria_1_req < 1 and criteria_2_req >= 1 and criteria_3_req >= 1 and criteria_4_req >= 1:
    print("Invalid Password.\nMust be greater than 15 letters.")
elif criteria_1_req >= 1 and criteria_2_req < 1 and criteria_3_req >= 1 and criteria_4_req >= 1:
    print("Invalid Password.\nMust have at least one capital letter.")
elif criteria_1_req >= 1 and criteria_2_req >= 1 and criteria_3_req < 1 and criteria_4_req >= 1:
    print("Invalid Password.\nMust have at least one number.")
elif criteria_1_req >= 1 and criteria_2_req >= 1 and criteria_3_req >= 1 and criteria_4_req < 1:
    print("Invalid Password.\nMust have at least one special character.")
    
elif criteria_1_req < 1 and criteria_2_req < 1 and criteria_3_req >= 1 and criteria_4_req >= 1:
    print("Invalid Password.\nMust be greater than 15 letters.\nMust have at least one capital letter.")
elif criteria_1_req < 1 and criteria_2_req < 1 and criteria_3_req < 1 and criteria_4_req >= 1:
    print("Invalid Pasword.\nMust be greater than 15 letters.\nMust have at least one capital letter.\nMust have at least one number.")
elif criteria_1_req < 1 and criteria_2_req < 1 and criteria_3_req < 1 and criteria_4_req < 1:
    print("Invalid Password.\nThe criteria was not applied upon inputting.")

elif criteria_1_req >= 1 and criteria_2_req >= 1 and criteria_3_req < 1 and criteria_4_req < 1:
    print("Invalid Password.\nMust have at least one number.\nMust have at least one special character.")
elif criteria_1_req >= 1 and criteria_2_req < 1 and criteria_3_req >= 1 and criteria_4_req < 1:
    print("Invalid Password.\nMust have at least one number.\nMust have at least one capital letter.\nMust have at least one special character.")
elif criteria_1_req >= 1 and criteria_2_req < 1 and criteria_3_req < 1 and criteria_4_req >= 1:
    print("Invalid Password.\nMust have at least one capital letter.\nMust have at least one number.")
    
elif criteria_1_req >= 1 and criteria_2_req < 1 and criteria_3_req < 1 and criteria_4_req < 1:
    print("Invalid Password.\nMust have at least one capital letter.\nMust have at least one number.\nMust have at least one special character.")
elif criteria_1_req < 1 and criteria_2_req >= 1 and criteria_3_req < 1 and criteria_4_req < 1:
    print("Invalid Password.\nMust be greater than 15 letters.\nMust have at least one number.\nMust have at least one special character.")
elif criteria_1_req < 1 and criteria_2_req < 1 and criteria_3_req >= 1 and criteria_4_req < 1:
    print("Invalid Password.\nMust be greater than 15 letters.\nMust have at least one capital letter.\nMust have at least one special character.")
elif criteria_1_req < 1 and criteria_2_req < 1 and criteria_3_req < 1 and criteria_4_req >= 1:
    print("Invalid Password.\nMust be greater than 15 letters.\nMust have at least one capital letter.\nMust have at least one number.")

elif criteria_1_req < 1 and criteria_2_req >= 1 and criteria_3_req >= 1 and criteria_4_req < 1:
    print("Invalid Password.\nMust be greater than 15 letters.\nMust have at least one special character.")
elif criteria_1_req < 1 and criteria_2_req >= 1 and criteria_3_req < 1 and criteria_4_req >= 1:
    print("Invalid Password.\nMust be greater than 15 letters.\nMust have at least one capital letter.\nMust have at least one number.\n")
elif criteria_1_req < 1 and criteria_2_req < 1 and criteria_3_req >= 1 and criteria_4_req >= 1:
    print("Invalid Password.\nMust be greater than 15 letters.\nMust have at least one capital letter.")

else:
    print("Invalid Password. Please follow the criteria upon inputting.")