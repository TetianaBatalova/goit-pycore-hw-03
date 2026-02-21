from datetime import datetime


def get_days_from_today(date: str) -> int:
    """
    Розраховує кількість днів між сьогоднішньою датою та заданою.

    Використовує метод toordinal() для отримання цілочисельного представлення дат.
    """
    # Перевірка типу вхідних даних (як у твоєму прикладі)
    if not isinstance(date, str):
        raise ValueError("Input must be a string in the format 'YYYY-MM-DD'")

    # Перевірка формату (довжина та дефіси)
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
    result = ordinal_today - ordinal_target

    return result


if __name__ == "__main__":
    # Тепер виклик для перевірки знаходиться в спеціальному блоці
    try:
        days_diff = get_days_from_today("2026-03-01")
        print(f"Різниця в днях: {days_diff}")
    except ValueError as e:
        print(f"Помилка: {e}")
