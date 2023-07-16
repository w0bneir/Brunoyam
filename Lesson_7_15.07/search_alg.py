# from functools import wraps
# from time import time
# import random
# # def timing(func):
# #     @wraps(func)
# #     def wrap(*args, **kw):
# #         ts = time()
# #         result = func(*args, **kw)
# #         te = time()
# #         print('func:%r \nargs^[%r, %r]\n took %2.10f sec' % (func.__name__, args, kw, te - ts))
# #         return result
# #     return wrap
# # @timing
# # def sum_list(l):
# #     x = 0
# #     for i in l:
# #         x += i
# #     return x
# # l = [random.randint(-1000, 1000) for x in range(10000)]
#
# #  Алгоритмы поиска - алгоритм, определяющий наличие элемента в коллекции
#
# in_list = [random.randint(-100, 100) for _ in range(99)]
# print(in_list)
# correct_index = random.randint(0,99)
# correct_answer = in_list[correct_index]
# print("correct answer " + str(correct_answer) + " on index " + str(correct_index))
#
#
# # def linear_search(col, target):
# #     for i in range(len(col)):
# #         if col[i] == target:
# #             return i
# #     return -1
# # print(linear_search(in_list, correct_answer))
#
# # Бинарный поиск
# in_list.sort()
# def bin_search(col, targer):
#     first = 0
#     last = len(col)-1
#     result = -1
#     while (first <= last) and (result == -1):
#         mid = (first + last) // 2
#         # print("first = " + str(first) + " last = " + str(last) + " mid = " + str(mid) + " col[mid] = " + str(col[mid] + ))
#         if col[mid] == targer:
#             result = mid
#         elif col[mid] < targer:
#             first = mid + 1
#         else: last = mid-1
#     return result
# # print(bin_search(in_list, correct_answer)
# def exp_search(col, target):
#     if col[0] == target:
#         return 0
#     index = 1
#     while index < len(col) and col[index] <= target:
#         index *=2
#         return bin_search(col[:min(index, len(col))], target)
#
#
# print(in_list)
# correct_index = random.randint(0,99)
# correct_answer = in_list[correct_index]
# print("correct answer " + str(correct_answer) + " on index " + str(correct_index))
# print('binary search: ' + str(bin_search(in_list, correct_answer)))
# def inter_search(col, target):
#     first = 0
#     last = len(col)-1
#     i = 0
#     while first <= last and target >= col[first] and target <= col[last]:
#         i +=1
#         index = first + int((float(last - first)/(col[last] - col[first]))*(target - col[first]))
#         if col[index] == target:
#             print("interpol times in while loop: " + str(i))
#             return index
#         elif col[index]<target:
#             first = index + 1
#         else:
#             last = index -1
#     return -1
# print("interpol search: " + str(inter_search(in_list, correct_answer)))

l = [3, 4, 5, 7, 8, 6, 54, 34, 65, 7, 8, 9, 8, 6, 5, 4, 3, 2]
m = []
while True:
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            l[i], l[i + 1] = l[i + 1], l[i]
    if m == l:
        break
    else:
        m = l[:]
print(l)    