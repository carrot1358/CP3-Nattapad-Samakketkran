def vat_Calculation(price):
    vat = 7
    return print(price + (price * vat / 100))
vat_Calculation(int(input("Enter price: ")))