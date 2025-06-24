a = frozenset([1, 2, 3, 4])
b = frozenset([3, 4, 5, 6])

print("Union:", a.union(b))
print("Intersection:", a.intersection(b))
print("Difference (a - b):", a.difference(b))
print("Symmetric Difference:", a.symmetric_difference(b))
