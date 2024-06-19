def calculate_sum(num1, num2):
    return num1 + num2

if __name__ == "__main__":
    
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    
    result = calculate_sum(number1, number2)
    
    print(f"The sum of {number1} and {number2} is {result}.")
