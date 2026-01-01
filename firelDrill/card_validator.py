credit_card_number = input("Enter your Credit card number: ")

length_of_card_number = len(credit_card_number)
sum_of_even = 0
sum_of_odd = 0
card_type = "Invalid card"
validity_status = "Invalid"


for count in range(length_of_card_number - 2, -1, -2):
    number = ord(credit_card_number[count]) - ord('0')
    number += number
    if number > 9:
        number -= 9
    sum_of_even += number

for count in range(length_of_card_number - 1, 0, -2):
    number = ord(credit_card_number[count]) - ord('0')
    sum_of_odd += number

total_sum = sum_of_even + sum_of_odd

if total_sum % 10 == 0:
    validity_status = "Valid"


if credit_card_number[0] == '4':
    card_type = "Visa Card"
elif credit_card_number[0] == '5':
    card_type = "Master Card"
elif credit_card_number[0] == '6':
    card_type = "Discover Card"
elif credit_card_number.startswith("37"):
    card_type = "American Express Card"

print("Credit Card Type:", card_type)
print("Credit Card Number:", credit_card_number)
print("Credit Card Length:", length_of_card_number)
print("Credit Card Validity Status:", validity_status)
s
