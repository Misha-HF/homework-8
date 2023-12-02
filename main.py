from datetime import datetime, timedelta, date


def get_birthdays_per_week(users):
    if not users:  # в разі якщо список користувачів порожній....
        return {}  # повертає порожній словник
    now = date.today()  # поточна дата береться з системного часу компьютора
#    today = date.today()
#    current_day = today.weekday()
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    # Оновлений словник для зберігання днів народження
    birthdays_per_week = {day: [] for day in days_of_week}
    for user in users:
        name = user['name']
        birthday = user['birthday']
        new_birthday = birthday.replace(year=now.year)
        if new_birthday < now:
            new_birthday = new_birthday.replace(
                year=now.year + 1)
        # Перевіряємо, чи дата народження потрапляє в наступний тиждень
        if now <= new_birthday <= now + timedelta(
                days=7):
            day_week = new_birthday.weekday()
            if day_week not in (5, 6):
                day_name = days_of_week[day_week]
            else:
                day_name = 'Monday'
            # Перевірка, чи день народження потрапляє на вихідний
            if day_name in ['Saturday', 'Sunday']:
                day_name = 'Monday'
            birthdays_per_week[day_name].append(
                name)

    print(birthdays_per_week)
    return {key: value for key, value in birthdays_per_week.items() if value}


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()},
        {"name": "Kim", "birthday": datetime(1990, 5, 15).date()},
    ]
    result = get_birthdays_per_week(users)
    if any(result.values()):
        print(result)
    else:
        print("Немає користувачів для привітання на цьому тижні.")
