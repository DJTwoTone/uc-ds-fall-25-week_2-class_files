"""Usually fast to grow a list by appending at the end."""
from timeit import repeat


def build_with_append(n: int) -> list[int]:
    xs: list[int] = []
    for i in range(n):
        xs.append(i)
    return xs


if __name__ == "__main__":
    n = 50_000
    t = min(repeat("build_with_append(n)", setup="from __main__ import build_with_append, n", number=1, repeat=3))
    print(f"append end, n={n}: {t:.6f}s")