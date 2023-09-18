import math

def compute_circle_area(radius):
    area = math.pi * radius**2
    return area

r = float(input('Enter radius: '))
area = compute_circle_area(r)
print('r =',r)
print('Area = ',area)

#-------------------------------


def compute_n_n_nnn():
    n = int(input("Enter an integer (n): "))
    nn = int(str(n) * 2)
    nnn = int(str(n) * 3)
    result = n + nn + nnn
    return result


result = compute_n_n_nnn()
print('value of n+nn+nnn is: ',result)


#-------------------------------

from datetime import date

def calculate_days_between_dates():
    year1 = int(input("Enter year for date 1: "))
    month1 = int(input("Enter month for date 1: "))
    day1 = int(input("Enter day for date 1: "))
    date1 = date(year1, month1, day1)

    year2 = int(input("Enter year for date 2: "))
    month2 = int(input("Enter month for date 2: "))
    day2 = int(input("Enter day for date 2: "))
    date2 = date(year2, month2, day2)

    delta = date2 - date1
    return abs(delta.days)

days_between = calculate_days_between_dates()
print(f'Number of days between two days: {days_between} days')
