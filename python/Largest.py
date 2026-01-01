number1 = int(input("Enter first number: "))
number2 = int(input("second number: "))
number3 = int(input("third number: "))

largest_number = number1
if number2 >= largest_number:
    largest_number = number2 

elif number3 >= largest_number:
    largest_number = number3

print("largest: ", largest_number)

