#Mercado's work

book_library = {
    'The Stranger' : {'stock' : 125, 'price' : 24},
    'Saudade' : {'stock' : 137, 'price' : 15},
    'Taste Of Sky' : {'stock' : 10, 'price' : 39},
    'Little Women' : {'stock' : 103, 'price' : 50}
}

user_acc = {}

balance = 0

def register(user_acc):
    username = input("Enter your desired username:")
    passw = input("Enter your desired password:")
    if username in user_acc:
        print('This user already exist.')
    else:
        user_acc[username] = {'password' : passw, 'balance': balance}

        print(f'Welcome, {username}')
        print(user_acc)

def login(user_acc):
    print("Login to your account.")
    username = input("Enter your username: ")
    passw = input('Enter your password: ')
    if passw in user_acc[username]['password']:
        print(f'You have logged in to your account, {username}')
        login_menu(user_acc, username)
    else:
        print('Invalid account.')

def login_menu(user_acc, username):
    while True:
        print("What would you like to do?")
        print("1. Check balance")
        print('2. Check Inventory')
        print('3. Top-up balance')
        print('4. Buy a book')
        print('5. Log out')

        choice = int(input('Type the number of your choice.'))

        if choice == 1:
            print(f'Your balance is: {balance}')
        elif choice == 2:
            pass
        elif choice == 3:
            topUp_balance(user_acc, username)
        elif choice == 4:
            rent_book(user_acc, username, balance)
        elif choice == 5:
            main()
        else:
            try:
                print('Invalid input.')
            except TypeError as err:
                print(err)

def topUp_balance (user_acc, username, balance):
    topUp = int(input('How much would you like to add to your balance?: '))

    balance = user_acc[username][balance] + topUp
    print(f'Your current balance is: {balance}')
    return login_menu(user_acc, username)

def rent_book (user_acc, username, balance):
    print('Which book would you like to rent?:')
    print(book_library)
    print('KEEP IN MIND THAT THIS PROGRAM IS CASE-SENSITIVE')
    choice = input('Enter your choice from above')

    if choice in book_library:
        print(book_library[choice])
        confirm = input('Did you choose the right one?: ')

        if confirm == 'Y' or 'y':
            if user_acc[username][balance] > book_library[choice]['price']:
                print('You have successfully added to your inventory.')
                newBalance = user_acc[username][balance] - book_library[choice]['price']
                print(f'Your remaining balance is {newBalance}')
            else: 
                print('You have insufficient balance.')
        elif confirm == 'N' or 'n':
            pass
        else:
            try:
                print('Invalid Input')
            except:
                print('An error has occured')
    else:
        print('That book is currently not available.')
        


def main():
    while True:
        print('Welcome to the Bookstore')
        print('What would you like to do?')
        print('1. Display available books.')
        print('2. Register User')
        print('3. Login')
        print('4. Admin Login')
        print('5. Exit')
        choice = int(input('What would you like to do?: '))
        
        if choice == 1:
            print(book_library)
        elif choice == 2:
            register(user_acc)
        elif choice == 3:
            login(user_acc)
        elif choice == 5:
            exit()
        else:
            print ("Invalid Input")

main()