# Function 1: add to stock function
def add_to_stock(stock_list):
    stock_list.append(75) # adds a fixed value of 75 in the list
    print("Inside function (stock):", stock_list)

# Function 2: update price function
def update_price(price):
    new_price = price + (price * 0.10) # adds a 10% markup on base price
    print("Inside function (price):", new_price)

inventory = [100, 200, 150]
add_to_stock(inventory) 
print("Outside function (stock):", inventory)

base_price = 250.0
update_price(base_price)
print("Outside function (price):", base_price)