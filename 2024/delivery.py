takeaway_menu = ["1. Pad Thai","2. Chicken Tikka Masala","3. Pepperoni Pizza","4. Veggie Burger with Fries","5. Burrito Bowl"]
takeaway_prices = [12.99, 14.50,  9.99,  15.99,  11.50]
delivery_fee = 5.00
free_delivery_price = 30.00

def get_bill_total(b,d):
    return b+d
print("Welcome to the takeaway delivery service.")
name = input("Please enter your name:   ")
print("Here's our menu.")
for item in takeaway_menu:
    print(item)

quantity = int(input("How many items would you like to purchase?"))
order = []
for i in range(quantity):
    choice = int(input("Enter the menu number of the item you wish to add to your order: "))
    order.append(choice)
print(f"Thank you {name}, your order is as follows")
total = 0
for item in order:
    total += takeaway_prices[item-1]
    print(takeaway_menu[item-1])
delv = 0
if total < free_delivery_price:
    delv = delivery_fee
print(f"Food Cost: €{total}\nDelivery Fee: €{delv}\nTotal: €{get_bill_total(delv,total)}")