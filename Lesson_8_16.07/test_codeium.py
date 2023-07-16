from random import randint
def quicksearch(arg):
    if len(arg)<=1:
        return arg
    else:
        first = arg[0]
        less = [x for x in arg[1:] if x <= first]
        more = [x for x in arg[1:] if x > first]
        return quicksearch(less) + [first] + quicksearch(more)
massive_list = [randint(0, 100000) for i in range(25)]
print(quicksearch(massive_list))