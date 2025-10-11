# Age Calculator--

# datetime module --
import datetime

# user input-
print('welcome To Age calculator')
name = input("Enter your name here :-")
birth_year = int(input("Enter your birth year :-"))
birth_month = int(input("Enter your birth month :-"))
birth_day = int(input("Enter a birth day :-"))

# get today date -
today = datetime.date.today()

birth_date = datetime.date(birth_year , birth_month , birth_day)
age = today.year - birth_date.year

if (today.month , today.day) < (birth_date.month , birth_date.day): age -= 1

# --output -
print(f"you are {age} year old ")
print(f"🎉Thanks {name} for using age calculator 😍:-")
