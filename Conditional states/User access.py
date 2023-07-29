# User Login

def authenticate_user(sys_username, sys_password):
    # Ask for the username and password from the user
    username = input("Username: ")
    password = input("Password: ")

    if sys_username == username and sys_password != password:
        return "Incorrect password"  # Return this message if the password is incorrect
    elif sys_username != username and sys_password == password:
        return "Incorrect username"  # Return this message if the username is incorrect
    elif sys_username != username and sys_password != password:
        return "Incorrect username and password"  # Return this message if both the username and password are incorrect
    else:
        return "Successfully logged in"  # Return this message if the login is successful

def main():
    print("""
    ****************************
    USER LOGIN
    ****************************
    """)

    sys_username = "emrah"  
    sys_password = "12345"  

    result = authenticate_user(sys_username, sys_password)
    print(result)

if __name__ == "__main__":
    main()
