menuList = {}
def showBill():
    final_price = 0
    print("---- My Food----")
    for i in menuList:
        print(i,menuList[i])
        final_price += menuList[i]
    print("Totol : ", final_price)

while True:
    menuName = input("Enter your menu :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price : "))
        menuList[menuName] = menuPrice
showBill()

