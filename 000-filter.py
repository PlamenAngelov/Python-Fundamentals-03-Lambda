nums = [1, 2, 3, 4, 5]


even_nums = filter(lambda e: e % 2 ==0, nums )
print(*even_nums)


even_nums = list(filter(lambda e: e % 2 ==0, nums ))
print(even_nums)


