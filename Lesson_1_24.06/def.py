def salary(okl, prem, ndfl):
    p = okl * prem
    zp = okl + p
    final = zp - zp * ndfl
    return final
oleg = salary(100000, 0.30, 0.13)
print(oleg)