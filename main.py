import add, subtract, multiply, divide


print("Welcome to Calculator")
#options
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

#input
choice = input("Enter choice(1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice in ('1', '2', '3', '4'):
    if choice == '1':
        print(add(num1, num2))

    elif choice == '2':
        print(subtract(num1, num2))

    elif choice == '3':
        print(multiply(num1, num2))

    elif choice == '4':
        if num2 != 0:
            print(divide(num1, num2))
        else:
            print("Error! Division by zero.")
