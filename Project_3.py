# To find out the years, months, weeks and days remaining
# input your present life
# use F-string

age = input("Your present age please")
age_in_int = int(age)
years_remaining = 90 - age_in_int
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365

print(f"you have {months_remaining} months {weeks_remaining} weeks and {days_remaining} days left") 