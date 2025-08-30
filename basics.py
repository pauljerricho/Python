"""Python Basics – runnable cheatsheet.

Run parts in an interactive shell or execute the file.
Each section is tiny & idiomatic, with print() so you can see outputs.
"""

# 0) Shebang & encoding (optional)
#   #!/usr/bin/env python3
#   # -*- coding: utf-8 -*-

# 1) Variables & types
i = 42                      # int
f = 3.14                    # float
s = "hello"                 # str
b = True                    # bool
n = None                    # NoneType
tpl = (1, 2, 3)             # tuple (immutable)
lst = [1, 2, 3]             # list (mutable, ordered)
st  = {1, 2, 2, 3}          # set (unique, unordered)
dct = {"a": 1, "b": 2}      # dict (mapping)

print(type(i), type(s), type(lst))

# 2) String formatting
name = "Alice"
age = 20
print(f"{name=}, {age=}")       # f-strings (best)
print("{} is {}".format(name, age))

# 3) Arithmetic, comparison, logical
print(1 + 2, 2 ** 3, 7 // 3, 7 % 3)
print(3 < 4 and not False)

# 4) Sequences & slicing
nums = [10, 20, 30, 40, 50]
print(nums[0], nums[-1], nums[1:4], nums[::2])

# 5) Control flow
for x in nums:
    if x > 25:
        print("gt25:", x)
    elif x == 20:
        print("is20")
    else:
        pass

# 6) Comprehensions
squares = [x * x for x in range(6)]                 # list comp
evens = {x for x in range(10) if x % 2 == 0}        # set comp
index = {c: i for i, c in enumerate("abc")}       # dict comp
print(squares, evens, index)

# 7) Functions
def add(a: int, b: int = 0) -> int:
    """Type hints are optional but helpful."""
    return a + b

def variadic(*args, **kwargs):
    return args, kwargs

print(add(1, 2), variadic(1, 2, k=3))

# 8) Lambdas & higher-order
apply = lambda fn, x: fn(x)
print(apply(lambda v: v * 2, 5))

# 9) Unpacking
a, b, *rest = [1, 2, 3, 4]
print(a, b, rest)

# 10) Exceptions
try:
    1 / 0
except ZeroDivisionError as e:
    print("caught:", e)
finally:
    pass

# 11) Context managers
from contextlib import contextmanager

@contextmanager
def demo_cm():
    print("enter")
    try:
        yield "resource"
    finally:
        print("exit")

with demo_cm() as res:
    print("use", res)

# 12) File I/O
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("hello file\n")
with open("example.txt", "r", encoding="utf-8") as f:
    print(f.read().strip())

# 13) Iterators & generators
def gen():
    for i in range(3):
        yield i

for v in gen():
    print("gen:", v)

# 14) Classes & dataclasses
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

u = User("Bob", 33)
print(u)

# 15) Enum & pattern matching (3.10+)
from enum import Enum
class Kind(Enum):
    A = 1
    B = 2

def handle(x):
    match x:
        case Kind.A:
            return "alpha"
        case Kind.B:
            return "beta"
        case _:
            return "other"

print(handle(Kind.A))

# 16) Decorators
def log(fn):
    def wrapper(*a, **k):
        print("calling", fn.__name__, a, k)
        return fn(*a, **k)
    return wrapper

@log
def mul(x, y): return x * y
print(mul(2, 3))

# 17) Virtual env (notes only)
#   python -m venv .venv
#   .venv\Scripts\activate  # Windows
#   source .venv/bin/activate # macOS/Linux
#   pip install -U pip

# 18) Packaging (notes only)
#   pyproject.toml + build backends (e.g., hatchling, setuptools)

# End
