day = int(input('Input your date of Birth, start with day: '))
mon = int(input('Input the month: '))
year = int(input('Input the year: '))
age = 2023 - year
month = 2 - mon
days = 22 - day

if month >= mon:
    print('You can have drivers license!')
elif month < mon:
    print('you can´t have your drivers license!')


if days >= day:
    print('You can have your drivers license!')
elif days < day:
    print('you can´t have your drivers license ')

if age == 18:
    print('You can have your drivers license!')
elif age < 18:
    print('You can´t have your drivers license, but not long')
else:
    print('ate')








