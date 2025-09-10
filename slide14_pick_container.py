"""Show how a set speeds up membership checks."""
users = [f"user{i}" for i in range(10_000)]
users_set = set(users)
print("'user9999' in list:", 'user9999' in users)
print("'user9999' in set:",  'user9999' in users_set)