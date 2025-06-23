from functools import reduce
fact = reduce(lambda x, y: x * y, range(1, 6))
print("factorial of 5 is:",fact) 
