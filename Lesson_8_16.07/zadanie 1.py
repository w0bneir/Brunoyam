# zadanie 1
# numbers_input = input("Введите числа через запятую: ")
# numbers_list = numbers_input.split(',')
# numbers_output = []
# for num in numbers_list:
#     if num not in numbers_output:
#         numbers_output.append(num)
# print(numbers_output)

# zadanie 2
# numbers_input = input("Введите числа через запятую: ")
# numbers_list = numbers_input.split(',')
# numbers_count = {}
# for num in numbers_list:
#     if num in numbers_count:
#         numbers_count[num] += 1
#     else:
#         numbers_count[num] = 1
# numbers_output = []
# for num, count in numbers_count.items():
#     numbers_output.append((f"Число {num} встречалось {count} раз"))
# print(numbers_output)

# zadanie 3
# print("Является ли строка палиндромом?)
# string_input = input("Введите строку: ").lower().replace(" ", "")
# reversed_string = string_input[::-1]
# if string_input == reversed_string:
#     print(True)
# else:
#     print(False)