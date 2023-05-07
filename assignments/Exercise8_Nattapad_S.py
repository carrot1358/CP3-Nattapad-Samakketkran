Username = input("Username: ")
Password = input("Password: ")
if Username == "admin" and Password == "1234":
    print("=== Welcome to Nattapad Shop ===")
    print("1. Apple  10 THB")
    print("2. Banana 20 THB")
    print("3. Orange 30 THB")
    print("4. Watermelon 40 THB")
    UserSelected = int(input("What you'd like to buy >> "))
    howmany = int(input("How many >> "))
    if UserSelected == 1:
        Price = 10*howmany
        print(f"Total price is {Price} THB")
    elif UserSelected == 2:
        Price = 20*howmany
        print(f"Total price is {Price} THB")
    elif UserSelected == 3:
        Price = 30*howmany
        print(f"Total price is {Price} THB")
    elif UserSelected == 4:
        Price = 40*howmany
        print(f"Total price is {Price} THB")