"""Compare: append at end vs insert at front vs slice copy."""
from timeit import repeat

def build_append(n: int) -> list[int]:
    xs: list[int] = []
    for i in range(n):
        xs.append(i)
    return xs

def build_front(n: int) -> list[int]:
    xs: list[int] = []
    for i in range(n):
        xs.insert(0, i)
    return xs

def slice_copy(n: int) -> list[int]:
    xs = list(range(n))
    return xs[1:]

if __name__ == "__main__":
    n = 20_000
    t_append = min(repeat("build_append(n)", setup="from __main__ import build_append, n", number=1, repeat=3))
    t_front  = min(repeat("build_front(n)",  setup="from __main__ import build_front, n",  number=1, repeat=3))
    t_slice  = min(repeat("slice_copy(n)",   setup="from __main__ import slice_copy, n",   number=10, repeat=3))
    print(f"append end (n={n}):   {t_append:.6f}s")
    print(f"insert front (n={n}): {t_front:.6f}s")
    print(f"slice copy x10 (n={n}): {t_slice:.6f}s total")