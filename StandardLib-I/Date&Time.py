#dates are easily constructed and formatted
from datetime import date
now = date.today()
print(now)

print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

#dates support calender arithmatic
birthday = date(1998,1,8)
age = now - birthday
print(age.days)