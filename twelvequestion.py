def q12():
    num = int(input("enter a number : "))
    sum = 0 
    while num!=0 :
        digit = num % 10 
        num //= 10
        sum += digit
    
    print(sum)
