def user_login():
    # Presumed Username and Password stored in the system
    sys_username = "emrah"
    sys_password = "12345678"

    login_attempts = 3
    while login_attempts > 0:
        username = input("Username: ")  # Prompting for username
        password = input("Password: ")  # Prompting for password

        if username != sys_username and password == sys_password:
            print("Incorrect Username...")  # Incorrect username, correct password
        elif username == sys_username and password != sys_password:
            print("Incorrect Password...")  # Correct username, incorrect password
        elif username != sys_username and password != sys_password:
            print("Incorrect Username and Password...")  # Incorrect username and password
        else:
            print("Login Successful...")  # Successful login
            return

        login_attempts -= 1
        print("Login Attempts Remaining:", login_attempts)  # Display remaining login attempts

    print("Login attempts exhausted. Exiting...")  # All login attempts used

if __name__ == "__main__":
    print("**********\nUser Login\n**********\n")
    user_login()
