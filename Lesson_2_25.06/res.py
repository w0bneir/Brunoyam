import re
#
# res = re.match("Nikita", "Nikita is my name")
# print(res, '\n')
#
# res = re.search("Nikita", "qNikita is my name Nikita")
# print(res, '\n')
#
# res = re.findall("Nikita", "qNikita is my name Nikita")
# print(res, '\n')
#
# res = re.split(",", "1.Nikita,2.Nikita,3.Nikita")
# print(res, '\n')
#
# res = re.sub("Oleg", "Nikita", "my name is Oleg Oleg")
# print(res, '\n')
#
# res = re.findall(r"\d""{3}", "qNi213kita is 412my nam234e Niki54674000ta")
# print(res, '\n')

# with open ('borodino.txt', 'r') as file:
#     file2 = open('borodino2.txt', 'w')
#     for i in file:
#         res = re.findall(r'\w', i)
#         file2.write(str(res))
#         file2.write('\n')
#     file2.close()

with open ('borodino.txt', 'r+') as file:
    file2 = open('borodino3.txt')
    for i in file:
        res = re.sub('а', 'о', i)
        print(type(res))
    file2.close()