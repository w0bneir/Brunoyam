ch1 = 0
ch2 = 0
op = 0
res = 0
print("Здравствуйте, я ваш персональный калькулятор")
while True:
    print("Введите первое число")
    ch1 = int(input())
    print("Введите второе число")
    ch2 = int(input())
    print("Выберете операцию из следующих и напишите ее ниже: +, -, *, /, **, //, %")
    op = str(input())
    if op == "+":
        res = ch1 + ch2
    elif op == "-":
        res = ch1 - ch2
    elif op == "*":
        res = ch1 * ch2
    elif op == "/":
        res = ch1 / ch2
    elif op == "**":
        res = ch1 ** ch2
    elif op == "//":
        res = ch1 // ch2
    elif op == "%":
        res = ch1 % ch2
    else:
        print("Вы ввели неверный оператор")
    print(res)
    print("Вы хотите продолжить? Да/Нет")
    ask = str(input())
    if ask == "Да":
        continue
    elif ask == "Нет":
        break