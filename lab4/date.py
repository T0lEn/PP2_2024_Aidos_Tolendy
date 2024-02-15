#ex1
import datetime

x = datetime.datetime.now()
print(x)


#ex2
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

#ex3

import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

#Ex4

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))



#exercise github
#ex1
import datetime


current_date = datetime.datetime.now()


five_days_ago = current_date - datetime.timedelta(days=5)

print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("Five days ago:", five_days_ago.strftime("%Y-%m-%d"))

#ex2
import datetime


today = datetime.date.today()


yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)


print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", today.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))

#ex3

import datetime


current_datetime = datetime.datetime.now()

current_datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Original datetime:", current_datetime)
print("Datetime without microseconds:", current_datetime_without_microseconds)


#ex4

import datetime


date1 = datetime.datetime(2024, 2, 15, 12, 0, 0)  
date2 = datetime.datetime(2024, 2, 16, 12, 0, 0)  


difference = date2 - date1


difference_seconds = difference.total_seconds()

print("Difference between the two dates in seconds:", difference_seconds)