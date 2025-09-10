"""Print a tiny table showing growth for several n values."""
from math import log2


def table(ns: list[int]) -> None:
    print("n\t~O(1)\t~O(n)\t~O(log n)\t~O(n^2)")
    for n in ns:
        o1 = 1
        on = n
        olog = 1 if n <= 1 else int(log2(n))
        on2 = n * n
    print(f"{n}\t{o1}\t{on}\t{olog}\t{on2}")


if __name__ == "__main__":
    table([5, 10, 20, 40])