from datetime import datetime, timedelta

users = [
    {
        "name": "Jimm",
        "birthday": datetime(1994, 11, 12),
    },
    {
       "name": "Jane",
        "birthday": datetime(1963, 11, 12),
    },
    {
        "name": "Anna",
        "birthday": datetime(1996, 12, 9),
    },
    {
        "name": "Luk",
        "birthday": datetime(1985, 12, 20),
    },
    {
        "name": "Olya",
        "birthday": datetime(1974, 11, 14),
    },
    {
        "name": "Olena",
        "birthday": datetime(1976, 11, 4),
    },
    {
        "name": "Oleg",
        "birthday": datetime(1997, 12, 14),
    },
    {
        "name": "Ira",
        "birthday": datetime(1997, 11, 9),
    },
    {
        "name": "Nic",
        "birthday": datetime(2016, 2, 29),
    },
]

def get_birthdays_per_week(users):
    monday = []
    tuesday = []
    wednesday = []
    thursday = []
    friday = []
    current_datetime = datetime.now()
    for user in users:
        birth_date = user.get('birthday')
        if birth_date.month == current_datetime.month:
            birth_delta =  birth_date.day - current_datetime.day
            if birth_delta <= 7 and birth_delta > 0:
                if birth_date.day == 29 and birth_date.month == 2:
                    birth_date = datetime(current_datetime.year, 3, 1)
                    birth_delta =  birth_date.day - current_datetime.day
                birth_date_new = current_datetime + timedelta(days=birth_delta)
                if birth_date_new.weekday() == 0 or birth_date_new.weekday() == 5 or birth_date_new.weekday() == 6:
                    monday.append(user.get('name'))
                elif birth_date_new.weekday() == 1:
                    tuesday.append(user.get('name'))
                elif birth_date_new.weekday() == 2:
                    wednesday.append(user.get('name'))
                elif birth_date_new.weekday() == 3:
                    thursday.append(user.get('name'))
                elif birth_date_new.weekday() == 4:
                    friday.append(user.get('name'))
    if len(monday)>0: 
        print('Monday:', ', '.join(map(str, monday)))
    if len(tuesday)>0:
        print('Tuesday:', ', '.join(map(str, tuesday)))
    if len(wednesday)>0:
        print('Wednesday:', ', '.join(map(str, wednesday)))
    if len(thursday)>0:
        print('Thursday:', ', '.join(map(str, thursday)))
    if len(friday)>0:
        print(f'Friday:', ', '.join(map(str, friday)))
    
    

print(get_birthdays_per_week(users))