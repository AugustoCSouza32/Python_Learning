item = input("What item would you like to buy? ")
price = float(input("Whats is the price? "))
quantity = int(input("How many would you like? "))

total = price * quantity

print(f"Total to pay: ${total:.2f}")