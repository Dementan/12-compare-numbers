#compare two numbers using True or False

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
result_compare = number1 > number2
if result_compare == True:
    print("The first number is larger than the second number")
else:
    print("The first number is smaller than the second number")
