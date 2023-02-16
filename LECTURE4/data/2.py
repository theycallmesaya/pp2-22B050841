import datetime

x= datetime.datetime.now()
u = x.day-1
z= x.day +1

x1 = datetime.date(x.year, x.month,u )

x2 = datetime.date(x.year, x.month,z )

print(x1)
print(x)
print(x2)
