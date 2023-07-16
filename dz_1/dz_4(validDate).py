import datetime
def validDate(day, month, year):
    if year < 1:
        return False
    if month < 1 or month > 12:
        return False
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if day < 1 or day > 29:
                return False
        else:
            if day < 1 or day > 28:
                return False
    elif month in [4,6,9,11]:
        if day < 1 or day > 30:
            return False
        else:
            if day < 1 or day > 31:
                return False
    return True
print(validDate(int(input('Введите день: ')), int(input('Введите месяц: ')), int(input('Введите год: '))))
