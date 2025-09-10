# Changing while looping — risky
xs = [1, 2, 2, 3, 2]
for i, x in enumerate(xs):
    if x == 2:
        xs.remove(2)
print("risky:", xs)

# Safer: build a new list
ys = [1, 2, 2, 3, 2]
no_twos = [y for y in ys if y != 2]
print("safe:", no_twos)

# Front inserts are slow; if you need queue behavior, consider deque
from collections import deque
q = deque(["a", "b"])  # fast appends/pops on both ends
q.appendleft("z")
print(list(q))