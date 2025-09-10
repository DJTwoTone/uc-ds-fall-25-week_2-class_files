"""Feel the difference: list scan vs set lookup."""
from timeit import repeat




def has_in_list(xs: list[int], target: int) -> bool:
    return target in xs


def has_in_set(xs: set[int], target: int) -> bool:
    return target in xs


if __name__ == "__main__":
    n, trials = 20_000, 5
    arr = list(range(n))
    st = set(arr)
    t1 = min(repeat("has_in_list(arr, -1)", setup="from __main__ import has_in_list, arr", number=1, repeat=trials))
    t2 = min(repeat("has_in_set(st, -1)", setup="from __main__ import has_in_set, st", number=1000, repeat=trials))
    print(f"list scan (1 call): {t1:.6f}s")
    print(f"set lookup (1000 calls): {t2:.6f}s total")