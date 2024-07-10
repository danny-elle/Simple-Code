import sys
from datetime import datetime

if len(sys.argv) != 2:
    print("Usage: python3 birth_year.py <age>")

age = int(sys.argv[1])
year_today = datetime.now().year
birth_year = year_today - age

current_month = datetime.now().month
current_day = datetime.now().day

# NEED TO FIX
if current_month < 1 or (current_month == 1 and current_day < 1):
    birth_year -=1
    print(f"{birth_year}")
print(f"Your birth year is {birth_year} and you are {age} years old!")
