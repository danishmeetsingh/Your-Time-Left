age = input("What is your age?")
# No. of years left
rem_years = 90 - int(age)
# No. of months left
rem_months = rem_years * 12
# No. of weeks left
rem_weeks = rem_years * 52
#No. of days left
rem_days = rem_months * 365
print(f"You have {rem_years} years, {rem_weeks} weeks, {rem_months} months and {rem_days} days left to live")
