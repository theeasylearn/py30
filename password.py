#exe:password detaction:detects the strong password

# (str.isalnum())
# (str.islower())
# (str.isspace())
# len(str)


def check_password(password):
    if len(password)>8:
        return "Please enter the password less than 8"
    if password.isspace()==True:
        return "Password should not contain any space"
    if password.isalnum()!=True:
        return "Please enter only alphanumeric characters"
    if password.islower()!=True:
        return "Use only lowercase"
    return "You have strong password"


password=input("Enter your password: ")
result=check_password(password)
print(result)