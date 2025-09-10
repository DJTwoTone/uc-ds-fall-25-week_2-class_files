"""Grab the 5th item quickly."""


def fifth(xs: list[int]) -> int | None:
    return xs[4] if len(xs) > 4 else None


if __name__ == "__main__":
    print(fifth([10, 20, 30, 40, 50]))