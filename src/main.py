run = True

while run:
    print("Welcome to the Console Games!")
    print("What would you like to do?")
    print("1. Tic tac toe\n2. Snake\n3. Tetris\n4. Quit")

    choice = input("Your choice: ")

    if choice == "1":
        print("Tic tac toe")

    elif choice == "2":
        print("Snake")

    elif choice == "3":
        print("Tetris")

    elif choice == "4":
        run = False

    else:
        print("Wrong input")
