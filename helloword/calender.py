import calendar
#other things to study is datetime and time

import datetime
import time

#a python function to print the names of the day
print(calendar.weekheader(3))
print()

#a python code to identify the first day of the week
print(calendar.firstweekday())
print()

print(calendar.month(2020, 4))

#a python function to print the month required
print(calendar.monthcalendar(2020, 4))


#a python function to display the calender of a given year
print(calendar.calendar(2020))

#a python function to check for the day
day_of_week = calendar.weekday(2020,4,27)

print(day_of_week)


#a python function to check if the year is leap or not
is_leap = calendar.isleap(2003)
print(is_leap)


#a python function to check for the leap days btn a range of years
how_many_leap_day = calendar.leapdays(2020,2021)
print(how_many_leap_day)