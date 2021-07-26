# To calculate leap year:
# A leap year is a year which is divisible by 4 but ...
# if it is divisible by 100, it must be divisible by 400.
# indentation matters - take care of it

year = int(input("Give the year to be checked for leap year"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The year {year} is a leap year")
        else:
            print(f"The year {year} is not a leap year")
    else:
        print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is not a leap year")

