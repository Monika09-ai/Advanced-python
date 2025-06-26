from functools import reduce
numbers = [10, 5, 22, 18, 20]
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print("Maximum element:", maximum)

