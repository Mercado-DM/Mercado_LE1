#Mercado's work

book_library = {
    'The Stranger' : {'stock' : 125, 'price' : 24},
    'Saudade' : {'stock' : 137, 'price' : 15},
    'Taste Of Sky' : {'stock' : 10, 'price' : 39},
    'Little Women' : {'stock' : 103, 'price' : 50}
}

user_acc = {}


def register(user_acc):
    regname = input("Enter your desired username:")
    regpassw = input("Enter your desired password:")
    if regname in user_acc:
        print('This user already exist.')
    else:
        user_acc[regname] = regpassw
        print(f'Welcome, {regname}')

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
        elif choice == 5:
            exit()
        else:
            print ("Invalid Input")

main()