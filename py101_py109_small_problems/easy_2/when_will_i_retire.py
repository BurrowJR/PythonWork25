from datetime import datetime

current_year = datetime.now().year
age = int(input("What is your age?  "))
retirement_age = int(input("At what age would you like to retire?  "))
retirement_year = (retirement_age - age) + current_year
years = retirement_year - current_year

print(f"It's {current_year}. You will retire in {retirement_year}")
print(f"You have only {years} years of work to go!")
