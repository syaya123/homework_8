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
    
    birthday_list = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
    }
   
    current_datetime = datetime.now()
    for user in users:
        birth_date = user.get('birthday')
        # пошук днів народження в поточному місяці
        if birth_date.month == current_datetime.month: 
            birth_delta =  birth_date.day - current_datetime.day
            # вибір днів народжень, які відбудуться протягом наступних 7 днів
            if birth_delta <= 7 and birth_delta > 0:
                # перевірка на 29 лютого
                if birth_date.day == 29 and birth_date.month == 2:
                    birth_date = datetime(current_datetime.year, 3, 1)
                    birth_delta =  birth_date.day - current_datetime.day
                # визначення дня вітання
                birth_date_new = current_datetime + timedelta(days=birth_delta)
                if birth_date_new.weekday() == 0 or birth_date_new.weekday() == 5 or birth_date_new.weekday() == 6:
                    birthday_list.get('Monday').append(user.get('name'))  
                elif birth_date_new.weekday() in range(1,4):
                    day_week = birth_date_new.strftime('%A')    
                    birthday_list.get(day_week).append(user.get('name'))     
   
    print_birthday_list(birthday_list)          
   # функція виводу списку іменинників
def print_birthday_list(birthday_list: dict):
    for key, val in birthday_list.items():
        if val:
            print(f"{key}: {', '.join(val)}")
    

print(get_birthdays_per_week(users))