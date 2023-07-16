def fibonacci(a):
    if a == 0:
        return 0
    elif a in (1,2):
        return 1
    else:
        return fibonacci(a-1) + fibonacci(a-2)
index = int(input("Напишите индекс числа:" '\n'))
print(fibonacci(index))