numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = {x for x in numbers if x % 2 == 0}
odd = {x for x in numbers if x % 2 != 0}

print("Even numbers:", even)
print("Odd numbers:", odd)
