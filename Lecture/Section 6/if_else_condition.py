UsernameInput = input ("Username: ")
PasswordInput = input ("Password: ")
if UsernameInput == "admin" and PasswordInput == "admin":
    print ("Hello Admin")
    print ("***************")
    print ("1. vat calculator")
    print ("2. price calculator")
    UserSelected = int(input(">>"))
    if UserSelected == 1:
        price = int(input("Price : "))
        vat = 7
        result = price + (price*vat/100)
        print (result)
    elif UserSelected == 2:
        price1 = int(input("First Product Price : "))
        price2 = int(input("Second Product Price : "))
        print (price1+price2)