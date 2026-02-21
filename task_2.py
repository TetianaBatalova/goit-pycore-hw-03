import random
from typing import List


def get_numbers_ticket(min_val: int, max_val: int, quantity: int) -> List[int]:
    """
    Генерує унікальні випадкові числа для лотерейного квитка.
    """
    # 1. Перевірка вхідних даних
    if min_val < 1 or max_val > 1000 or quantity < 1 or quantity > (max_val - min_val + 1):
        return []

    # 2. Генерація унікальних випадкових чисел
    lottery_list = random.sample(range(min_val, max_val + 1), quantity)

    # 3. Сортування списку
    lottery_list.sort()

    return lottery_list


if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)
