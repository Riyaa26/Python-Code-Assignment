def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

choice = input("Enter 1 to convert Celsius to Fahrenheit, 2 to convert Fahrenheit to Celsius: ")

if choice == '1':
    celsius_temp = float(input("Enter temperature in Celsius: "))
    fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
    print(f"{celsius_temp} degrees Celsius is equal to {fahrenheit_temp} degrees Fahrenheit.")
elif choice == '2':
    fahrenheit_temp = float(input("Enter temperature in Fahrenheit: "))
    celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
    print(f"{fahrenheit_temp} degrees Fahrenheit is equal to {celsius_temp} degrees Celsius.")
else:
    print("Invalid choice.")
