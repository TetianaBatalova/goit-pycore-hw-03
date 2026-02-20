from datetime import datetime

def get_days_from_today(date):
    if not isinstance(date, str):
        raise ValueError("Input must be a string in the format 'YYYY-MM-DD'")
    if len(date) != 10 or date[4] != '-' or date[7] != '-':
        raise ValueError("Input must be in the format 'YYYY-MM-DD'")
    # 1. Перетворюємо рядок у об'єкт datetime
    target_date = datetime.strptime(date, "%Y-%m-%d")
    
    # 2. Отримуємо поточну дату
    today = datetime.today()
    
    # 3. Перетворюємо обидві дати в порядкові номери (цілі числа)
    ordinal_today = today.toordinal()
    ordinal_target = target_date.toordinal()
    
    # 4. Знаходимо різницю
    # Якщо target_date у майбутньому, результат буде від'ємним
    result = ordinal_today - ordinal_target
    
    return result

# Перевірка:
print(get_days_from_today("2026-03-01"))
