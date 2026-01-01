num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))

largest = num1

if(num2 > largest):
largest = num2
if(num3 > largest):
largest = num3
    print(largest, "is the largest number in the list")
