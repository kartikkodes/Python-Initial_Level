import datetime

x1 = int(input("Enter the year for fromer date"))
x2 = int(input("enter the month for fromer date"))
x3 = int(input("Enter the day for fromer date"))

y1 = int(input("Enter the year for latterr date"))
y2 = int(input("enter the month for latterr date"))
y3 = int(input("Enter the day for latterr date"))

firt_date = datetime.date(x1,x2,x3)
second_date = datetime.date(y1,y2,y3)
days = second_date - firt_date
print(days)
