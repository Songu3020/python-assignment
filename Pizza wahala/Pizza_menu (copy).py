import math

table = """
Pizza type  Number of Slices     Price per Box
Sapa Size            4               2,000
Small Money          6               2,400
Big Boys             8               3,000
Odogwu              12               4,200
"""


 
number_of_people = int(input("Enter number of people: "))
pizza_type = input("Enter pizza type (Sapa Size, Small Money, Big Boys, Odogwu):")


 
match pizza_type:
    case "Sapa Size":
        slices_per_box = 4
        price_per_box = 2000

    case "Small Money":
        slices_per_box = 6
        price_per_box = 2400

    case "Big Boys":
        slices_per_box = 8
        price_per_box = 3000


    case "Odogwu":
        slices_per_box = 12
        price_per_box = 4200

    case _:
        print("Invalid pizza type selected!")
        exit()

 
boxes_needed = math.ceil(number_of_people / slices_per_box)

total_slices = boxes_needed * slices_per_box

leftover_slices = total_slices - number_of_people

total_price = boxes_needed * price_per_box

 
print("\n--- Order Summary ---")
print(f"Number of boxes of pizza to buy = {boxes_needed} boxes")
print(f"Number of leftover slices after serving = {leftover_slices} slices")
print(f"Total price = ₦{total_price}")

