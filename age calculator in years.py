from datetime import date
import datetime
import math

# age calculator function
def age_calculator(date_of_birth):
    # getting today's date
    today = date.today()
    age_in_years = (
        today.year
        - date_of_birth.year
        - ((today.month, today.day) < (today.month, today.day))
    )
    return age_in_years


# main program or driver program

calculated_age = age_calculator(date(2001, 2, 3))

print(calculated_age, "years")
