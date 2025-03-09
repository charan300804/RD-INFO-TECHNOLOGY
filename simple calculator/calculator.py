def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def modulus(x, y):
    return x % y

def exponentiation(x, y):
    return x ** y

def floor_division(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x // y

print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")
print("6. Exponentiation (**)")
print("7. Floor Division (//)")

while True:
    choice = input("Enter choice (1/2/3/4/5/6/7): ")

    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print(f"Result: {num1} % {num2} = {modulus(num1, num2)}")
        elif choice == '6':
            print(f"Result: {num1} ** {num2} = {exponentiation(num1, num2)}")
        elif choice == '7':
            print(f"Result: {num1} // {num2} = {floor_division(num1, num2)}")

        next_calc = input("Do you want to perform another calculation? (yes/no): ")
        if next_calc.lower() != 'yes':
            print("Thanks for using the calculator!")
            break
    else:
        print("Invalid Input. Please enter a valid choice.")
