import random
def write_nums(path):
    nums = [random.randint(1,10), random.randint(11,20), random.randint(21,30)]
    with open(path, 'w+') as file:
        for i in nums:
            file.write(str(i) + '\n')
def read_nums(path):
    nums = []
    with open(path, 'r') as file:
        for i in file:
            nums.append(i.strip())
    return nums
path = "nums.txt"
write_nums(path)
nums = read_nums(path)
print(nums)