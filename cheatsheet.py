"""Quick reference for Python syntax & stdlib (print-only)."""
import math, statistics as stats, itertools as it, pathlib, collections as co

# Math & stats
print(math.sqrt(16), math.pi)
print(stats.mean([1,2,3,4,5]))

# itertools
print(list(it.islice(it.count(10, 2), 5)))   # 10,12,14,16,18

# pathlib
p = pathlib.Path(".").resolve()
print("cwd:", p)

# Counter & deque
cnt = co.Counter("banana")
dq = co.deque([1,2,3]); dq.appendleft(0); dq.pop()
print(cnt, list(dq))
