import timeit
from random import randint
def quicksort(arg):
    if len(arg) <= 1:
        return arg
    else:
        first = arg[0]
        less = [x for x in arg[1:] if x <= first]
        bigger = [x for x in arg[1:] if x > first]
        return quicksort(less) + [first] + quicksort(bigger)
list_ = []
for i in range(5):
    list_.append(randint(1, 1000))
print("Неотсортированный список:", list_)
start_time = timeit.default_timer()
sorted_list = quicksort(list_)
end_time = timeit.default_timer()
execution_time = end_time - start_time
print("Отсортированный список:", sorted_list)
print("Время выполнения: {:.9f} секунд".format(execution_time))