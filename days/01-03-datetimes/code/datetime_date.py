#!python3

from datetime import datetime
from datetime import date

datetime.today()
#datetime.datetime(2018, 2, 19, 14, 38, 52, 133483)

today = datetime.today()


print (type(today))
#<class 'datetime.datetime'>


todaydate = date.today()

print ('today:',todaydate)
#datetime.date(2018, 2, 19)

type(todaydate)
#<class 'datetime.date'>

print ('month:',todaydate.month)
#2

print('year:',todaydate.year)
#2018

print ('day:',todaydate.day)
#19


christmas = date(2020, 12, 25)
print ('chr:',christmas)
#datetime.date(2018, 12, 25)

if christmas is not todaydate:
    print("Sorry there are still " + str((christmas - todaydate).days) + " until Christmas!")
else:
    print("Yay it's Christmas!")
