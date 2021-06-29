month1=["january","march","may","july","august","october","december"]
month2=["april","june","september","november"]
month=input("enter the month:")
if month=="february":
    print("no. of days = 29(non leap year) or 28(leap year)")
elif month in month1:
    print("no. of days are 31")
elif month in month2:
    print("no. of days are 30")
else:
    print("invalid month")
