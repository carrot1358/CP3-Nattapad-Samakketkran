"""
Exercise 11 (Nattapad S.)
    The challenge is :
    input       output
    5             *             ----> Line 1 (* x 1)
                 ***            ----> Line 2 (* x 3)
                *****           ----> Line 3 (* x 5)
               *******          ----> Line 4 (* x 7)
              *********         ----> Line 5 (* x 9)
"""
while True:
    input_1 = int(input("Enter a number: "))
    for i in range(input_1):
        print(" "*(input_1-(i+1)) + "*"*((i+1)+(i*1)))