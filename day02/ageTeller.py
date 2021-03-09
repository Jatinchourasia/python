from datetime import date 
todays_date = date.today()
birth_year = input("what is your birth year : ",)
your_age = int(todays_date.year) - int(birth_year)
print(your_age)
