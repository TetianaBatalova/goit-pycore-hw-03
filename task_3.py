import re


def normalize_phone(phone_number):
    # 1. Очищуємо рядок від усіх символів, крім цифр (і залишаємо плюс, якщо він є)

    cleaned_number = re.sub(r"[^\d+]", "", phone_number.strip())

    # 2. Перевіряємо префікси та нормалізуємо
    if cleaned_number.startswith("+380"):
        # Вже є правильний код країни
        normalized = cleaned_number
    elif cleaned_number.startswith("380"):
        # Є код країни, але немає плюса
        normalized = "+" + cleaned_number
    else:
        # Немає коду країни (наприклад, 050...), додаємо +38
        normalized = "+38" + cleaned_number

    return normalized


# Перевірка:
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
