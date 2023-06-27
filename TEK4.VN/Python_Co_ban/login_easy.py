login = False
while login == False:
    login_username = input("Username: ")
    if login_username != 'root':
        print('Username invalid!')
    else:
        login_password = input("Password: ")
        if login_password == 'pass':
            print('Success!')
            login = True
        else:
            print('Login password incorrect!')
            