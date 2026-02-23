from datetime import date, timedelta, datetime
#1
"""
dt = date.today() - timedelta(5)

print(date.today())
print(dt)
"""
#2
"""
print(date.today() - timedelta(1))
print(date.today())
print(date.today() + timedelta(1))
"""
#3
"""
dt = datetime.now()
no_microseconds = dt.replace(microsecond=0)

print("Original:", dt)
print("Without microseconds:", no_microseconds)
"""
#4
"""
date1 = input("Enter first date: ")
date2 = input("Enter second date: ")

dt1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
dt2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")

diff = dt2 - dt1

seconds = diff.total_seconds()

print("Difference in seconds:", seconds)
"""