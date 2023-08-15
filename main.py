import datetime

def get_birthdays_per_week(users):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    current_day = datetime.datetime.now().date()
    next_week = current_day + datetime.timedelta(days=7)

    print("Ближчі дні народження:")

    for day in range(8):
        target_day = current_day + datetime.timedelta(days=day)
        day_name = days_of_week[target_day.weekday()]
        birthday_people = [user["name"] for user in users if user["birthday"].month == target_day.month and user["birthday"].day == target_day.day]

        if birthday_people:
            print(f"{day_name}:", ", ".join(birthday_people))

users = [
    {"name": "people1", "birthday": datetime.datetime(2000, 8, 16)},
    {"name": "people2", "birthday": datetime.datetime(1999, 8, 18)},
    {"name": "people3", "birthday": datetime.datetime(1998, 8, 20)},
    {"name": "people4", "birthday": datetime.datetime(1997, 8, 21)},
    {"name": "people5", "birthday": datetime.datetime(1996, 8, 24)},
    {"name": "people6", "birthday": datetime.datetime(2000, 8, 16)},
    {"name": "people7", "birthday": datetime.datetime(2001, 8, 22)},
]

get_birthdays_per_week(users)

