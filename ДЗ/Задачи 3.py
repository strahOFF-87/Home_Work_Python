# Упражнение 1.
# Дан список из чисел.
# Определите их НОК (наименьшее общее кратное) и НОД (наибольший общий делитель).
# from typing import List
# from functools import reduce
# import math
#
#
# def calculate_pair_nod(a: int, b: int) -> int:
#     while a != 0 and b != 0:
#         if a > b:
#             a %= b
#         else:
#             b %= a
#     return a + b
#
#
# def calculate_nod(numbers: List[int]) -> int:
#     result = numbers[0]
#     for number in numbers[1:]:
#         result = calculate_pair_nod(result, number)
#     return result
#
#
# def calculate_nok(numbers: List[int]) -> int:
#     nok = 1
#     for number in numbers:
#         nok = (nok * number) // calculate_pair_nod(nok, number)
#     return nok
#
#
# if __name__ == '__main__':
#     test_numbers = [36, 48, 2, 124, 12, 2]
#     assert math.gcd(*test_numbers) == calculate_nod(test_numbers)
#     assert math.lcm(*test_numbers) == calculate_nok(test_numbers)

# Вариант 2
from functools import reduce
# from math import gcd
#
# def nod(x, y):
#     return gcd(x, y) if x else y
#
# def nok(x, y):
#     return x * y // nod(x, y)
#
# numbers = [int(item) for item in input("Введите числа через пробел: ").split()]
#
# if len(numbers) > 1:
#     result_nod = reduce(nod, numbers)
#     result_nok = reduce(nok, numbers)
# else:
#     print("Введите только одно число!")
#
# print(f"НОД: {result_nod}\nНОК: {result_nok}")


# Вариант 3
import math
from unittest import result


def gcd_lcm_loop(numbers):
    result_gcd = 0
    result_lcm = 0

    for number in numbers:
        gcd_number = math.gcd(number, result_gcd)
        result_gcd *= gcd_number if gcd_number > result_gcd else result_gcd

        lcm_number = number * result_lcm // result_gcd
        result_lcm *= lcm_number if lcm_number > result_lcm else result_lcm

    return result_gcd, result_lcm
print()

# Упражнение 2.
# Даны n предложений. Определите, сколько из них содержат хотя бы одну цифру.
# from typing import List
# import re
#
#
# def find_number_in_sentences(sentences: List[str]) -> int:
#     result = []
#     for sentence in sentences:
#         if re.search(r'\d+', sentence) is not None:
#             result.append(True)
#     return len(result)
#
#
# if __name__ == "__main__":
#     test_sentences = ['Привет 123, мир!',
#                       'Цифр4 вну7ри', 'Тут нет', 'Тут 2 есть']
#
#     print(find_number_in_sentences(test_sentences))

# Упражнение 3.
# Дана строка s и символ k. Реализуйте функцию, рисующую рамку из символа k вокруг данной строки, например:

# **************
# *Текст в рамке*
# **************


# Упражнение 4.
# Для введенного предложения выведите статистику символ=количество. Регистр букв не учитывается.
