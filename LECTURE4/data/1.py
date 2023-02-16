import datetime

x = datetime.datetime.now()
print(x)

u = x.day -5
#x.day = u
x2 = datetime.date(x.year, x.month, u)
print(x2)