#Ćwiczenie1
price = 69.99
discount = 0.1
wynik = price - (price * discount)

print(f"The item costs {wynik:.2f} PLN")

#Ćwiczenie2
product_name = 'Shoe'
price = 49.99
in_stock = True

print(f"Product name: {product_name}")
print(f"Price: ${price}")
print(f"Is Available: {in_stock}")

#Ćwiczenie3
units_used = 150
cost_per_unit = 0.15
cost = units_used * cost_per_unit

print(f"units used: {units_used}")
print(f"cos per unit: {cost_per_unit}")
print(f"total cost: ${cost}")

#Ćwiczenie4
print("-"*40)
print("VERSION 1.01")
print("-"*40)

#Ćwiczenie5
print("="*40)
print("author: twoje_imie@poczta.com")
print("date: 01-09-2023")
print("="*40)

#Ćwiczenie6
store_name = "Shopshoe"
item_name = "Running shoes"
item_price = 100.00
item_discount = 0.30
total_price = item_price - (item_price*item_discount)

print(f"Welcome to {store_name}!")
print("-"*50)
print(f"Today's special is {item_name}, which normally cost ${item_price:.2f}\n"
      f"But for a limited time, you can get it for ${total_price:.2f} ({item_discount:.0%} off)!")
