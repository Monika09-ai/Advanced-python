a, b, s = 0, 1, set()
for _ in range(10): s.add(a); a, b = b, a + b
print("fibonacci series",s)
