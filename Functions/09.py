def password_validator(password: str) -> None:
    is_valid = True
    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    is_alphanumeric = password.isalnum()
    if not is_alphanumeric:
        print("Password must consist only of letters and digits")
        is_valid = False
    digits = 0
    for char in password:
        if char.isdigit():
            digits += 1
    if digits < 2:
        print("Password must have at least 2 digits")
        is_valid = False

    if is_valid:
        print("Password is valid")

password1 = input()
password_validator(password1)
