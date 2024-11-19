import hashlib
import getpass

password_manager = {}

def create_account():
    username = input("Enter you desired username: ")
    password = getpass.getpass("Enter you desired password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Account created successfully")

def login():
    username = input("Enter you desired username: ")
    password = getpass.getpass("Enter you desired password:")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login successful")
    else:
        print("Incorrect username or password, try again")

def view_accounts():
    if password_manager:
        print("List of accounts:")
        for username in password_manager.keys():
            print(f"- {username}")
    else:
        print("No accounts have been created yet.")


def main():
    while True:
        choice = input("Enter 1 to create an account, 2 to login, 3 to view accounts, or 0 to exit: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            view_accounts()
        elif choice == "0":
            break
        else:
            print("Invalid operation.")


if __name__ == "__main__":
    main()
