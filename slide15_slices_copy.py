"""Prove that slices return a separate list."""

a = [1, 2, 3, 4, 5]
b = a[1:4]
print("a is b?", a is b)
b[0] = 99
print("a:", a)
print("b:", b)