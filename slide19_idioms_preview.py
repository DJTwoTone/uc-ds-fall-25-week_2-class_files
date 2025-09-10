users = ["ana", "ben", "cai"]
scores = [91, 88, 95]
for u, s in zip(users, scores):
    print(u, s)

records = [
    {"name": "ana", "score": 91},
    {"name": "ben", "score": 88},
    {"name": "cai", "score": 95},
]
by_score = sorted(records, key=lambda r: r["score"])  # doesn't change originals
print(by_score)