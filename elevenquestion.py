def q11():
    num = int(input("enter a number : "))
    firstNum = 0
    secNum = 1
    print("0\n1")
    for i in range(2,num):
        fiboonaci = firstNum + secNum
        print(fiboonaci)
        firstNum = secNum
        secNum = fiboonaci
