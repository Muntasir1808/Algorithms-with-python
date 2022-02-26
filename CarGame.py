settings = input("< ")
print("""
start -- To start the car
stop -- To stop the car 
quit -- To exit
""")
is_start = False
is_stop = False
Quit = False
while not Quit:
    if settings.lower() == 'help':
        choice = input("< ").lower()

        if choice == "start":
            is_stop = False
            if is_start:
                # is_start = True
                print("The car is already started...")
            else:
                is_start = True
                print("The car is started...Ready to go!")

        elif choice == "stop":
            is_start = False
            if is_stop:
                # is_stop = True
                print("Hey! the car is already stopped!!")
            else:
                is_stop = True
                print("The car is stopped!!")
        elif choice == "quit":
            print("Program terminated")
            Quit = True

        else:
            print("I don't understand that")
            