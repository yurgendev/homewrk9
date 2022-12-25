# # Homework 9 (13.11.2022)
# # 1. Реалізуйте функцію, параметрами якої є два числа та рядок. Повертає вона конкатенацію рядка із сумою чисел.
def func(a, b, c):
    res = f'{a + b}{c}'
    return res


a = 10
b = 25
c = 'qwerty123'
print(func(a, b, c))

# # # 2. Реалізуйте функцію, яка малює на екрані прямокутник із зірочок «*».
# # # Її параметрами будуть цілі числа, які описують довжину та ширину такого прямокутника.

def rectangle_func(wide, hight):
    res_rect = f"{'*' * wide}\n" + \
               f"*{' ' * (wide - 2)}*\n" * (hight - 2) + \
               f"{'*' * wide}\n"
    return res_rect


wide = 5
hight = 7
print(rectangle_func(wide, hight))


# # 3. Напишіть функцію, яка реалізує лінійний пошук елемента у списку цілих чисел.
# # # Якщо такий елемент у списку є, то поверніть індекс, якщо ні, то поверніть число «-1».


def func():
    for value in new_list:
        if value % 1 == 0:
            print(new_list.index(value))
        elif value % 1 > 0:
            print('-1')


new_list = [1, 2, 3.3, -4, 5.5, 6.6]
func()


4. Напишіть функцію, яка поверне кількість слів у текстовому рядку.

import string

def count_func(text):
    for item in string.punctuation:
        text = text.replace(item, ' ')

    return len(text.split())

print(count_func('abc, ww, tga, aaaaaaaaa, sadasdasd, asdsdsd, asdsadsa   wwwaxv    ,,, 112'))


5. Напишіть функцію, яка переводить число, що означає кількість доларів і центів, в прописний формат. Наприклад:
> 123,34
> one hundred twenty three dollars thirty four cents

num = float(input('please enter an integer between 1 and 9999: '))


def int_to_en(num):
    d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
         6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
         11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
         15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
         19: 'nineteen', 20: 'twenty',
         30: 'thirty', 40: 'fourth', 50: 'fifty', 60: 'sixty',
         70: 'seventy', 80: 'eighty', 90: 'ninty'}
    k = 1000
    m = k * 1000

    if num == 0 or num == 1:
        return d[num] + ' dollar'

    if num < 20:
        return d[num]

    if num < 100:
        if num % 10 == 0:
            return d[num] + ' dollars'
        else:
            return d[num // 10 * 10] + ' ' + d[num % 10] + ' dollars'

    if num < k:
        if num % 100 == 0:
            return d[num // 100] + ' hundred dollars'
        else:
            return d[num // 100] + ' hundred ' + int_to_en(num % 100)
    if num < m:
        if num % k == 0:
            return int_to_en(num // k) + ' thousand dollars'
        else:
            return int_to_en(num // k) + ' thousand, ' + int_to_en(num % k) + ' dollars'


print(int_to_en(num))

Напишіть функцію, яка переводить ціле число з римського запису до десяткового.
Наприклад: XXII -> 22


ROMAN = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


def int_to_roman(number):
    result = ""
    for (arabic, roman) in ROMAN:
        (factor, number) = divmod(number, arabic)
        result += roman * factor

    return result

print(int_to_roman(11))


