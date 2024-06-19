def q3():
    num = int(input("enter any number for factorial : "))
    factorial = 1 
    for i in range(1,num+1) :
        factorial *= i 
    print("factorial of {} is {}".format(num,factorial))
