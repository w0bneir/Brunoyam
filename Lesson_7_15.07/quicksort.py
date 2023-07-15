from random import randint
def quicksort_(arg):
    if len(arg)<=1:
        return arg
    else:
        first = arg[0]
        less = [x for x in arg[1:] if x <= first]
        more = [x for x in arg[1:] if x > first]
        return quicksort_(less) + [first] + quicksort_(more)
list_ = []
for i in range(10):
    list_.append(randint(1,30))
print(list_)
print(quicksort_(list_))