"""Count steps, not seconds: tiny step counters for common shapes."""


def steps_constant(n: int) -> int:
    return 1


def steps_linear(n: int) -> int:
    s = 0
    for _ in range(n):
        s += 1
    return s


def steps_log(n: int) -> int:
    s, size = 0, max(1, n)
    while size > 1:
        size //= 2
        s += 1
    return max(1, s)


def steps_quadratic(n: int) -> int:
    s = 0
    for _ in range(n):
        for _ in range(n):
            s += 1
    return s


if __name__ == "__main__":
    for n in (10, 100):
        print(n, steps_constant(n), steps_linear(n), steps_log(n), steps_quadratic(n))