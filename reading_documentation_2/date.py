# Using the datetime module in Python, how would you obtain the current date and time?

import datetime

current_date_time = datetime.datetime.now()

print('The current date and time is: ', current_date_time)

# or

formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date_time)
