def verify_email(email):
    if not email[0].isalpha():
        return False
    pos_dot = email.rfind('.')
    pos_at = email.find('@')

    if pos_at == -1 or pos_dot == -1 or pos_dot < pos_at:
        return False
    if pos_dot == len(email) - 1:
        return False
    return True


email = input("email ")
if verify_email(email) == True:
    print("Valid")
else:
    print("Invalid")
