import re


def normalize_phone(phone_number: str) -> str:
    """
    Очищує та нормалізує номер телефону до формату +380.
    """
    # 1. Очищуємо рядок від усіх символів, крім цифр та знака '+'
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


if __name__ == "__main__":
    raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
    ]
    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери:", sanitized_numbers)
