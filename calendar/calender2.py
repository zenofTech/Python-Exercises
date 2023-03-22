# Python program to display calendar
import calendar
# Accept the year and month
yy = int(input("Enter the year: "))
mm = int(input("Enter the month: "))

print('\n',calendar.month(yy,mm))