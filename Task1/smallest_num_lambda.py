from functools import reduce

numbers = [5, 3, 8, 1, 9, 2]
smallest = reduce(lambda x, y: x if x < y else y, numbers)
print("Smallest number:", smallest)
