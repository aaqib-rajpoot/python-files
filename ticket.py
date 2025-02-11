price_list = [5,7,12,6]
age = int(input('Enter your age: '))
discount = int(input("Add a discount value:"))
if age <= 12:
    print(f"Hey Children: Your ticket price is ${price_list[0]}.")
elif age <= 17:
    price_list[1] = price_list[1] - discount
    print(f"hey Teenager: your ticket price is ${price_list[1]}. with discount of ${discount}")
elif age <=64:
    price_list[2] = price_list[2] - discount
    print(f"Hey Adult: your ticket price is ${price_list[2]}. with discount of ${discount}")
elif age > 65:
    print(f"hey Senior: your ticket price is ${price_list[3]}")