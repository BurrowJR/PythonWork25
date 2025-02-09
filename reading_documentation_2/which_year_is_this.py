from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()[0]

# What is the difference between the year attribute and the isocalendar method?

print(today)
print(today_year)
print(iso_year)
print(today.isocalendar())

# year attribute returns the year part of the date.

# isocalendar method returns a tuple containing the ISO calendar year, ISO week number, and ISO weekday.  (International Organization for Standardization) ISO is a calender system that is used to standardized the way weeks are numbered and dated.