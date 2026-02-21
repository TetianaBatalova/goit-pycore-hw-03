from datetime import datetime, timedelta
from typing import List, Dict


def get_upcoming_birthdays(users: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Повертає список користувачів, яких потрібно привітати протягом 7 днів.
    """
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # Конвертуємо рядок у об'єкт date
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Підставляємо поточний рік у дату народження з обробкою 29 лютого
        try:
            birthday_this_year = birthday.replace(year=today.year)
        except ValueError:
            # Якщо 29.02 не існує в цьому році, використовуємо 1 березня
            birthday_this_year = birthday.replace(
                year=today.year, month=3, day=1)

        # Якщо день народження вже минув цього року, переносимо на наступний
        if birthday_this_year < today:
            try:
                birthday_this_year = birthday_this_year.replace(
                    year=today.year + 1)
            except ValueError:
                birthday_this_year = birthday_this_year.replace(
                    year=today.year + 1, month=3, day=1)

        # Рахуємо різницю в днях
        days_until_birthday = (birthday_this_year - today).days

        # Перевіряємо, чи день народження випадає на цей тиждень (0-7 днів)
        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year
            day_of_week = congratulation_date.weekday()

            # Переносимо на понеділок, якщо випадає на суботу (5) або неділю (6)
            if day_of_week == 5:
                congratulation_date += timedelta(days=2)
            elif day_of_week == 6:
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.02.21"},  # Наприклад, сьогодні
        {"name": "Leap Baby", "birthday": "1996.02.29"},  # Кейс 29 лютого
        {"name": "Jane Smith", "birthday": "1990.02.23"}  # Вихідний
    ]
    print("Список привітань на цьому тижні:", get_upcoming_birthdays(users))
