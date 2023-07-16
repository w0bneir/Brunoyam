import datetime
def validDate(day, month, year):
    try:
        datetime.datetime(year, month, day)
        return True
    except:
        return False
print(validDate(int(input('Введите день: ')), int(input('Введите месяц: ')), int(input('Введите год: '))))

try:
    with open("file.txt", 'r') as file:
        pass
except:
    print("Файла не существует")

try:
    a = int("a")
except:
    print("'a' not int")