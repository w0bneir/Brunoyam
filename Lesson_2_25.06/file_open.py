with open('borodino.txt', 'w+') as file:
    file.write("— Скажи-ка, дядя, ведь недаром\n"
                "Москва, спаленная пожаром,\n"
                "Французу отдана?\n"
                "Ведь были ж схватки боевые,\n"
                "Да, говорят, еще какие!\n"
                "Недаром помнит вся Россия\n"
                "Про день Бородина!\n")
file = open("borodino.txt", 'r')
with open('borodino2.txt', 'w+') as file2:
    for i in file:
        print(i)
        file2.write(i)
file.close()
file2.close()