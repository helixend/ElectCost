import datetime

rub = 4.46

vvt = int(input('Enter the wattage of the device '))
while vvt < 1:
    vvt = int(input('Enter the wattage of the device '))
hrs = float(input('How many hours per day is the device turned on? '))
while hrs > 24 or hrs < 1:
    hrs = float(input('How many hours per day is the device turned on? '))

kvd = (vvt * hrs) / 1000

day = kvd * rub
week = (kvd * 7) * rub
year = (kvd * 365) * rub
y5 = year * 5
y10 = year * 10

if True:
    d = datetime.datetime.now()
    t = d.strftime("%m")
    if t == '02':
        vdd = 28
    mth = ['04', '06', '09', '11']
    if t in mth:
        vdd = 30
    else:
        vdd = 31
    month = (kvd * vdd) * rub

print()
print('Day - {} rub'.format(day))
print('Week - {} rub'.format(week))
print('Month - {} rub'.format(month))
print('Year - {} rub'.format(year))
print('5 Years - {} rub'.format(y5))
print('10 Years - {} rub'.format(y10))