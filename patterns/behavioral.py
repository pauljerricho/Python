"""Behavioral patterns (Pythonic)."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Callable, Iterable

# 1) Strategy
def s_add(a,b): return a+b
def s_mul(a,b): return a*b
def do_strategy(fn: Callable[[int,int], int], a: int, b: int) -> int:
    return fn(a,b)

# 2) Observer
class Event:
    def __init__(self): self._subs: list[Callable[[str], None]] = []
    def subscribe(self, fn): self._subs.append(fn)
    def emit(self, msg): [fn(msg) for fn in list(self._subs)]

# 3) Command
@dataclass
class Command:
    exec: Callable[[], None]
    undo: Callable[[], None]

class Invoker:
    def __init__(self): self.history: list[Command] = []
    def run(self, c: Command):
        c.exec(); self.history.append(c)
    def rollback(self):
        while self.history:
            self.history.pop().undo()

# 4) State
class State:
    def handle(self, ctx): raise NotImplementedError
class On(State):
    def handle(self, ctx): ctx.state = Off()
class Off(State):
    def handle(self, ctx): ctx.state = On()
class Context:
    def __init__(self): self.state: State = Off()
    def toggle(self): self.state.handle(self)

# 5) Template Method
class Template:
    def run(self): return self.step1() + self.step2()
    def step1(self): return "A"
    def step2(self): raise NotImplementedError
class Impl(Template):
    def step2(self): return "B"

# 6) Iterator
class RangeIt:
    def __init__(self, n): self.i = 0; self.n = n
    def __iter__(self): return self
    def __next__(self):
        if self.i >= self.n: raise StopIteration
        self.i += 1; return self.i

# 7) Mediator
class Mediator:
    def __init__(self): self._subs: list[Callable[[str], None]] = []
    def reg(self, fn): self._subs.append(fn)
    def send(self, msg): [fn(msg) for fn in self._subs]

# 8) Chain of Responsibility
@dataclass
class Handler:
    next: "Handler|None" = None
    def handle(self, req: int) -> str:
        if self.next: return self.next.handle(req)
        return "unhandled"
class EvenHandler(Handler):
    def handle(self, req: int) -> str:
        return "even" if req % 2 == 0 else super().handle(req)
class PosHandler(Handler):
    def handle(self, req: int) -> str:
        return "positive" if req > 0 else super().handle(req)

# 9) Memento (snapshots)
@dataclass
class Editor:
    text: str = ""
    def snapshot(self): return self.text
    def restore(self, snap): self.text = snap

# 10) Visitor
class Visitor:
    def visit_int(self, x:int): return x*2
    def visit_str(self, x:str): return x.upper()
def visit(v: Visitor, obj):
    return getattr(v, f"visit_{type(obj).__name__}", lambda o:o)(obj)
