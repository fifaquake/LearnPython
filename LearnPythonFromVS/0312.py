from datetime import timedelta
a = timedelta(days = 2, hours = 6)
b = timedelta(hours = 4.5)
c= a+ b
print(c.days)
print(c.seconds)
print(c.total_seconds())

from datetime import datetime
a = datetime(2012, 9, 23)
print(a + timedelta(days = 10))
now = datetime.today()
print(now)
birthday = datetime(2014, 5, 10)
print(birthday - now)