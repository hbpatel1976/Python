# To Calculate pizza order bill

print("Welcome to Pizza Shop")

pizza_size = input("Which size of pizza you want S, M Or L").upper()
add_pepperoni = input("Do you want to add prpperoni? Y/N").upper()
add_cheese = input("Do you want to add extra cheese? Y/N").upper()

if pizza_size == "L":
    bill = 12
elif pizza_size == "M":
    bill = 7
else:
    bill = 5

if add_pepperoni == "Y":
    if pizza_size == "S":
        bill += 2
    else:
        bill += 3

if add_cheese == "Y":
    bill += 1
    
print(f"Your total bill is ${bill}")
    
    