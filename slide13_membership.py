"""Compare membership strategies."""
from timeit import repeat


def in_list(xs: list[int], target: int) -> bool:
    return target in xs # walks


def in_set(xs: set[int], target: int) -> bool:
    return target in xs # near-instant on average


if __name__ == "__main__":
    n, trials = 50_000, 5
    arr = list(range(n))
    st = set(arr)
    t1 = min(repeat("in_list(arr, -1)", setup="from __main__ import in_list, arr", number=1, repeat=trials))
    t2 = min(repeat("in_set(st, -1)", setup="from __main__ import in_set, st", number=1000, repeat=trials))
    print(f"list scan (1 call): {t1:.6f}s")
    print(f"set lookup (1000 calls): {t2:.6f}s total")