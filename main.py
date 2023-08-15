import datetime

def get_birthdays_per_week(users):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    current_day = datetime.datetime.now().date()
    next_week = current_day + datetime.timedelta(days=7)

    print("Ближчі дні народження:")

    for day in range(7):
        target_day = current_day + datetime.timedelta(days=day)
        day_name = days_of_week[target_day.weekday()]
        birthday_people = [user["name"] for user in users if user["birthday"].month == target_day.month and user["birthday"].day == target_day.day]

        if birthday_people:
            print(f"{day_name}:", ", ".join(birthday_people))

users = [
    {"name": "Bill", "birthday": datetime.datetime(2000, 8, 16)},
    {"name": "Jill", "birthday": datetime.datetime(1995, 8, 18)},
    {"name": "Kim", "birthday": datetime.datetime(1987, 8, 20)},
    {"name": "Jan", "birthday": datetime.datetime(1990, 8, 21)},
]

get_birthdays_per_week(users)

