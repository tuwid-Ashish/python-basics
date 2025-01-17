# 1. take user input as password
# 2. check method to check the password
# 4. It should be 8 characters lenght
# 5. It should have atleast one uppercase letter
# 6. It should have atleast one lowercase letter
# 7. Special characters are optional

def check_password(password):
    if len(password)< 8:
        return f"Password is too short"
    if not any(char.isupper() for char in password):
        return f"Password should have atleast one uppercase letter"
    if not any(char.islower() for char in password):
        return f"Password should have atleast one lowercase letter"
    if not any(char in '!@#$%^&*()-_[]{}|;:,.<>?/' for char in password):
        return f"Password should have atleast one special character"
    return f"Password is valid"


password = input("Enter the password: ")
print(check_password(password))