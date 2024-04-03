#Mercado's work

book_library = {
    'The Stranger' : {'stock' : 125, 'price' : 24},
    'Saudade' : {'stock' : 137, 'price' : 15},
    'Taste Of Sky' : {'stock' : 10, 'price' : 39},
    'Little Women' : {'stock' : 103, 'price' : 50}
}

user_acc = {}


def register(user_acc):
    username = input("Enter your desired username:")
    passw = input("Enter your desired password:")
    if username in user_acc:
        print('This user already exist.')
    else:
        user_acc[username] = passw

        print(f'Welcome, {username}')

def login(user_acc):
    print("Login to your account.")
    username = input("Enter your username: ")
    passw = input('Enter your password: ')
    if passw in user_acc[username]:
        print(f'You have logged in to your account, {username}')
    else:
        print('Invalid account.')



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