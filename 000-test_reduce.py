from functools import reduce

nums = [1,2,3,4,5]

e = reduce(lambda a, b: a+b, nums)

print(e)