# To calculate the charge for ridding the rollercoaster
# Give proper message if cannot ride

print("Welcome to rollercoaster")
height = int(input("What is your height in cm?"))

# keywords if, else and : and indentation are part of syntax
# statements written with same indent is called a block of code
# Nested if - if age > 18 pay $12 else pay $ 7
total_charge = 0
if height > 120:
    print("you can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Child tickets are $2")
        total_charge += 2
    elif age <= 18:
        print("youth tickets are $4")
        total_charge += 4
    elif age <= 60:
        print("Adult tickets are $7")
        total_charge += 7
    else:
        print("Senior citizen can ride free")
    want_photo = input("Do you want a photo? Y/N").upper()
    if want_photo == "Y":
        total_charge += 3
    print(f"your total bill is ${total_charge}")
else:
    print("sorry, you have to grow taller before you can ride")


  
  