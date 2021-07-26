# BMI calculations
# Get weight in kg - int
# Get height in m - float
# Get BMI in integer

weight = int(input("weight(kg) = "))
height = float(input("height(m) = "))

bmi = weight / height ** 2   
bmi = int(bmi)

# using power operator. try without using power operator

print("Your BMI for weight",weight, "kg and height",height,"m is ..",bmi)

# using f-string
print(f"Your BMI for weight {weight} kg and height {height} m is .. {bmi}")   
