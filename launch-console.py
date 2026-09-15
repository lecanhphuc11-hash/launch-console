name = "Canhphuc Le"
print("Welcome to " + name + "'s Launch Console!")

running = True
while running:
    print("1) About me")
    print("2) My goals")
    print("3) Exit")
    choice = input("Pick 1-3: ")
    if choice == "1":
        print("I'm VP of My BEST Robotics Club and Intern in-training in C2C")
    elif choice == "2":
        print("My goal: ship my first real project this term and go to state for BEST Robotics")
    elif choice == "3":
        print("Goodbye!")
        running = False
    else:
        print("Please pick 1, 2, or 3.")