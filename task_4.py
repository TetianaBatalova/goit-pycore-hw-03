from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    # 1. Отримуємо поточну дату
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # 2. Конвертуємо рядок дати у об'єкт date
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # 3. Підставляємо поточний рік у дату народження
        birthday_this_year = birthday.replace(year=today.year)

        # 4. Якщо день народження вже минув цього року, переносимо його на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # 5. Рахуємо різницю в днях
        days_until_birthday = (birthday_this_year - today).days

        # 6. Перевіряємо, чи день народження випадає на цей тиждень (0-7 днів)
        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year
            
            # 7. Переносимо на понеділок, якщо випадає на вихідні (субота або неділя)
            day_of_week = congratulation_date.weekday()
            if day_of_week == 5:  # Субота
                congratulation_date += timedelta(days=2)
            elif day_of_week == 6:  # Неділя
                congratulation_date += timedelta(days=1)

            # 8. Додаємо результат у список у потрібному форматі рядка
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# Приклад використання функції:
users = [
    {"name": "John Doe", "birthday": "1985.02.20"},
    {"name": "Jane Smith", "birthday": "1990.02.27"}
]

print("Список привітань на цьому тижні:", get_upcoming_birthdays(users))
