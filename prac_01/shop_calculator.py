number_of_items = -1

while number_of_items < 0:
    number_of_items = int(input("Number of items: "))
    if number_of_items < 0:
        print("Invalid number of items!")

total_price = 0.0

for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price += price_of_item

if total_price > 100:
    total_price *= 0.9  # Apply a 10% discount

print(f"Total price for {number_of_items} items is ${total_price:.2f}")
