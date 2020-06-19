"""
                         DATE TIME MODULE WITH PYTHON
Qn:how to work with date time

@@@@@the benefits of learning Date time module
--------->>>Calculate the difference btn today and your birthday
-------->>>>App that can send emails automatically based on date
-------->>>>Instagram clone that can say things like"posted 3 days ago"


"""
import  datetime

#a piece of code to display the day of today
today = datetime.date.today()
print(today)

#a piece of code to displaay my bday date
birthday = datetime.date(1998, 2, 1)
print(birthday)

days_since_birthday = (today - birthday).days

#it displays the days  i have spent since i was born
print(days_since_birthday)
print()

#it minus 10 days from today
tdelta = datetime.timedelta(days=10)
print(today - tdelta)

print()
#it prints the  month of today
print(today.month)
print(today.weekday())#display the day of the week
#where monday==0 and  sunday ==6
print()

print(datetime.time(6,3,37,24))# display the time of the day
"""
THINGS TO NOTE:::
datetime.date(year,month,day)
datetime.time(hour,minute,second,microsecond)
datetime.datetime(year,month,day,hour,min,sec,microsec)


"""
print()

hour_delta = datetime.timedelta(hours = 5)
print(datetime.datetime.now() + hour_delta)
"""
#in order for the below command s to operate you have
#to first install pytz
#........>>>pip install pytz
print(datetime.datetime.now(tz=pytz.UTC))







"""