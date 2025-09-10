# Week 02 — Student Notes: Lists & Arrays (Beginner‑Friendly)

**You’ll be able to:**

* Explain Big‑O in plain words and spot four common growth shapes.
* Use Python lists safely (reading by spot, adding at end, slices, membership).
* Avoid common traps (copy vs same list, changing while looping).
* Implement small real‑world list tasks and test them.

> Python 3.11+, standard library only. All code below runs as is.

---

## 1) Big‑O in plain language

**Idea:** We count *steps*, not seconds. Ask: *“If the data doubles, how do the steps grow?”*

* **O(1)** — same few steps. Example: grab the top card.
* **O(n)** — one pass over the items. Example: look through a stack of papers.
* **O(log n)** — keep halving the search space. Example: guess‑the‑number game.
* **O(n²)** — compare everything with everything. Example: everyone meets everyone.

**Mini check:** Which is which?

* Show the 5th photo in a gallery → O(1)
* Search a name in an unsorted guest list → O(n)
* Number guessing where you say higher/lower → O(log n)

**Tiny demo (counts steps, not time):**

```python
# Save as big_o_steps.py and run
from math import log2

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

for n in (10, 100):
    print(n, steps_constant(n), steps_linear(n), steps_log(n), steps_quadratic(n))
```

---

## 2) Python lists: the mental picture

A list is a **row of boxes** that can grow. Each box has a position: 0, 1, 2, …

### Common operations (and why they feel fast or slow)

* **Read by position (fast):** `xs[i]` — jump straight to the box → \~O(1)
* **Add at the end (usually fast):** `xs.append(x)` → puts a new box at the end → \~O(1) per add
* **Add/remove at the *front* (slow):** `xs.insert(0, x)`, `xs.pop(0)` → everyone shifts over → O(n)
* **Membership in a list (a walk):** `x in xs` → check one by one → O(n). For fast membership, use a `set` → \~O(1) average
* **Slices make a copy:** `xs[a:b]` returns a **new** list → copying takes O(length of slice)

### Quick code you can run

```python
# list_basics.py
xs = [10, 20, 30, 40, 50]
print("spot 2:", xs[2])    # 30
xs.append(60)
print("after append:", xs) # [10,20,30,40,50,60]
```

---

## 3) Copy vs same list (super important)

Two names can point to the **same** list, or you can make a **new** list.

```python
# copy_vs_same.py
a = [1, 2, 3]
b = a          # same list
b.append(4)
print("a:", a)  # [1,2,3,4]

c = a[:]       # new list (copy)
c.append(5)
print("a:", a)  # still [1,2,3,4]
print("c:", c)  # [1,2,3,4,5]
```

**Rule of thumb:** If you see slicing (`[:]` or `[i:j]`), you made a **copy**.

---

## 4) Don’t change a list while you loop over it

Changing the same list during a `for` loop can **skip items**.

```python
# safe_editing.py
bad = [1, 2, 2, 3, 2]
for i, x in enumerate(bad):
    if x == 2:
        bad.remove(2)     # risky: structure changes while we loop
print("bad:", bad)        # output is surprising

# Safer: build a new list
xs = [1, 2, 2, 3, 2]
no_twos = [x for x in xs if x != 2]
print("good:", no_twos)   # [1, 3]
```

---

## 5) A few handy idioms

```python
# idioms.py
xs = ["apple", "banana", "cherry"]
for i, x in enumerate(xs):
    print(i, x)          # index and value together

users = ["ana", "ben"]
scores = [91, 88]
for u, s in zip(users, scores):
    print(u, s)          # walk two lists in parallel

records = [
    {"name": "ana", "score": 91},
    {"name": "ben", "score": 88},
]
by_score = sorted(records, key=lambda r: r["score"])
print(by_score)
```

---

## 6) Tiny “feel the cost” demo

Feel the difference between **add at end** and **add at front**, and how a **slice** copies.

```python
# feel_cost.py
from timeit import repeat

def build_with_append(n: int) -> list[int]:
    xs: list[int] = []
    for i in range(n):
        xs.append(i)
    return xs

def build_with_front_insert(n: int) -> list[int]:
    xs: list[int] = []
    for i in range(n):
        xs.insert(0, i)   # pushes everyone right
    return xs

def slice_copy(n: int) -> list[int]:
    xs = list(range(n))
    return xs[1:]         # new list

n = 20_000
print("append end:", min(repeat("build_with_append(n)", setup="from __main__ import build_with_append, n", number=1, repeat=3)))
print("insert front:", min(repeat("build_with_front_insert(n)", setup="from __main__ import build_with_front_insert, n", number=1, repeat=3)))
print("slice copy x10:", min(repeat("slice_copy(n)", setup="from __main__ import slice_copy, n", number=10, repeat=3)))
```

---

## 7) Micro‑problems (what they are and hints)

These are the three tasks you’ll implement in class/homework. **Write tests first if you can.**

### 7.1 Rotate right (new list)

**Plain words:** Move the last `k` items to the front. If `k` is big, it wraps around.

**Examples:**

* `[1,2,3,4,5], k=2 → [4,5,1,2,3]`
* `[1,2], k=2 → [1,2]`

**Hints:**

* If `k < 0` → error.
* If the list is empty → return `[]`.
* Use `k %= len(xs)` to handle big `k`.
* A clean approach uses **slices**: last `k` + the rest.

```python
# pattern_rotate.py
def rotate_right(nums: list[int], k: int) -> list[int]:
    if k < 0:
        raise ValueError("k must be non-negative")
    n = len(nums)
    if n == 0:
        return []
    k %= n
    return nums[-k:] + nums[:-k] if k else nums[:]
```

### 7.2 Keep first time we saw each value

**Plain words:** Remove duplicates but keep the first appearance of each number.

```python
# pattern_unique.py
def unique_preserve_order(nums: list[int]) -> list[int]:
    seen: set[int] = set()
    out: list[int] = []
    for x in nums:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out
```

### 7.3 Do any two add up to the target?

**Plain words:** If any two numbers sum to `target`, return `True`. Otherwise `False`.

```python
# pattern_two_sum_exists.py
def pair_sum_exists(nums: list[int], target: int) -> bool:
    need: set[int] = set()
    for x in nums:
        if x in need:
            return True
        need.add(target - x)
    return False
```

> Complexity
>
> * `rotate_right` (slice) → O(n) time, O(n) space (makes a new list)
> * `unique_preserve_order` → O(n) time, O(n) space (uses a set)
> * `pair_sum_exists` → O(n) time, O(n) space (stores needed complements)

---

## 8) Studio challenges (extra practice)

These are not the same as the micro‑problems, but use the same habits.

### 8.1 Low‑Stock Day

**Plain words:** Start with `initial` items. Subtract each day’s sales. Return the first day index when the remaining items are at or below `threshold`. If never, return `None`.

```python
# studio_low_stock.py
def detect_first_low_stock(initial: int, daily_sales: list[int], threshold: int) -> int | None:
    remaining = initial
    for i, sold in enumerate(daily_sales):
        if sold < 0:
            raise ValueError("daily_sales cannot be negative")
        remaining -= sold
        if remaining <= threshold:
            return i
    return None
```

### 8.2 Goal Window

**Plain words:** Steps per day are in `values`. Did any `k`‑day stretch average at least `target_avg`?

```python
# studio_goal_window.py
def has_window_with_avg_at_least(values: list[int], k: int, target_avg: float) -> bool:
    n = len(values)
    if k <= 0:
        raise ValueError("k must be positive")
    if k > n:
        return False
    target_sum = target_avg * k
    win = sum(values[:k])
    if win >= target_sum:
        return True
    for i in range(k, n):
        win += values[i] - values[i - k]
        if win >= target_sum:
            return True
    return False
```

### 8.3 Merge Logs

**Plain words:** You have two lists of `(time, message)` that are already sorted by time. Combine them into one sorted list. If times tie, take from the first list, then the second.

```python
# studio_merge_logs.py
def merge_log_streams(a: list[tuple[int, str]], b: list[tuple[int, str]]) -> list[tuple[int, str]]:
    i = j = 0
    out: list[tuple[int, str]] = []
    while i < len(a) and j < len(b):
        ta, tb = a[i][0], b[j][0]
        if ta <= tb:          # a wins ties
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    out.extend(a[i:])
    out.extend(b[j:])
    return out
```

---

## 9) Edge‑case checklist (use this while testing)

* Empty list; one item; all items the same; already rotated.
* For rotation: `k = 0`, `k = len(xs)`, `k > len(xs)`, negative `k` (error).
* For pair sums: many solutions vs none; negative numbers; target not reachable.
* For goal windows: `k > len(values)`; exact equality to the target; zeros and negatives.
* For merging: one side empty; equal timestamps; very uneven lengths.

---

## 10) Practice questions (short and sweet)

1. What does `xs[2:5]` return — a view or a new list?
2. Why is adding at the front of a list slow for big lists?
3. When would you pick a `set` over a `list`?
4. What does `enumerate(xs)` give you?
5. If data doubles, which grows faster — O(n) or O(log n)? By roughly how much?

**Self‑check answers:**

1. A **new** list (a copy of that slice). 2) Because everyone has to **shift** over. 3) When you need fast “is it there?” checks. 4) Pairs of `(index, value)` while looping. 5) O(n) doubles; O(log n) increases by about one step.

---

## 11) Glossary (no jargon)

* **Steps grow how?**: How work increases as data gets bigger.
* **Copy**: A separate list with the same items (changing it won’t change the original).
* **Same list**: Two names pointing to the exact same list in memory.
* **Slice**: `xs[a:b]` — takes a **copy** of that range.
* **Window**: A run of consecutive items of fixed size `k`.

---

## 12) What to turn in (for graded work)

* Python files in `/src` with type hints and short docstrings.
* Your own edge‑case tests in `/tests` (use `pytest`).
* A short README note: “How do the steps grow?” for each function.

> Tip: Write small, test small. If something breaks, make a **tiny** example that shows the bug, fix it, and then run the full tests again.
