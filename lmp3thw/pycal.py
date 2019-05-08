#!/usr/bin/python3

# pycal imitates cal - shows a calendar for either the current month of the current year highlighting today.

import sys, os
import datetime

### __subs__ ###

def display_mon(Day, show_day):
    """ displays the current month """

    temp_day = Day - datetime.timedelta(days=Day.day-1)
    temp_month = temp_day.month

    Result = []
    Result.append(''.join(['\n ',str(Day.year),' ',Day.strftime('%B'),'\n Пн Вт Ср Чт Пт Сб Вс']))

    temp_str = '   ' * temp_day.weekday()    

    while temp_month == temp_day.month:

        if temp_day.day == Day.day and temp_day.day < 10 and show_day:
            temp_str += ' ·'
        elif temp_day.day == Day.day and temp_day.day >= 10 and show_day:
            temp_str += '·'
        elif temp_day.day < 10:
            temp_str += '  '
        else:
            temp_str += ' '
        temp_str += str(temp_day.day)
        if temp_day.weekday() == 6:
            Result.append(temp_str)
            temp_str = ''
        temp_day += datetime.timedelta(days=1)

    Result.append(temp_str)
    return '\n'.join(Result)

def display_year(Day):
    """ displays the whole year """

    year = str(Day.year)
    for i in range(1,13,1):
        if i == Day.month:
            print(display_mon(datetime.datetime.strptime(year+'-'+str(i)+'-'+str(Day.day), '%Y-%m-%d'), True))
        else:
            print(display_mon(datetime.datetime.strptime(year+'-'+str(i)+'-'+str(Day.day), '%Y-%m-%d'), False))

    return

### __main__ ###

if len(sys.argv) > 1:
    params = sys.argv[1:]
else:
    params = []

show_year = False
show_mon  = True

for i in params:
    if i.lower() == '-y' or i.lower() == '--year':
        show_year = True
        show_mon  = False
        break
    if i.lower() == '-m' or i.lower() == '--month':
        show_year = False
        show_mon  = True
        break

today = datetime.datetime.now()

if   show_year:
    display_year(today)
elif show_mon:
    print(display_mon(today, True))
else:
    print('Oops!')