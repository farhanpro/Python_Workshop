from datetime import datetime

day = datetime.today()

if  day in 'Saturday':
    print('Party')
elif day in 'Sunday':
    print('Recover')
else:
    print('Work')
