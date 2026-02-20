import random

def get_numbers_ticket(min, max, quantity):
    # 1. Перевірка вхідних даних
   
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []

    # 2. Генерація унікальних випадкових чисел
 
    lottery_list = random.sample(range(min, max + 1), quantity)

    # 3. Сортування списку
    lottery_list.sort()

    return lottery_list

# Приклад використання функції:
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
