def square(a):
    if a>0:
        return (a*2, a**2, 2**0.5*a)
        # return f"P={a*2}, S={a**2}, d={2**0.5*a}"
    else:
        return "Сторона должна быть больше 0"
b = int(input("Введите сторону квадрата. Число должно быть целым: "))
print(type(square(b)))
print(square(b))