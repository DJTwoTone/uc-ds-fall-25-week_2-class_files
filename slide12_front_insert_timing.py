"""Slow at the front: everyone shifts right."""
from timeit import repeat


def build_with_front_insert(n: int) -> list[int]:
    xs: list[int] = []
    for i in range(n):
        xs.insert(0, i)
    return xs


if __name__ == "__main__":
    n = 10_000
    t = min(repeat("build_with_front_insert(n)", setup="from __main__ import build_with_front_insert, n", number=1, repeat=3))
    print(f"insert front, n={n}: {t:.6f}s")