"""

Exercise: Loop
result :
    1
    *
    2
    *
    **
    3
    *
    **
    ***

"""
while True:
    times = int(input(""))
    for i in range(times):
        print("*"* (i+1))