"""Structural patterns (Pythonic)."""
from __future__ import annotations
from dataclasses import dataclass

# 1) Adapter
class Legacy:
    def do_legacy(self): return "legacy"

class Target:
    def request(self): raise NotImplementedError

class Adapter(Target):
    def __init__(self, legacy: Legacy): self.legacy = legacy
    def request(self): return self.legacy.do_legacy()

# 2) Facade
class SubA: 
    def work(self): return "A"
class SubB: 
    def work(self): return "B"
class Facade:
    def __init__(self): self.a, self.b = SubA(), SubB()
    def do(self): return f"{self.a.work()}-{self.b.work()}"

# 3) Decorator (object wrapper, not function decorator)
class Service:
    def op(self): return "core"
class LoggingDecorator(Service):
    def __init__(self, svc: Service): self.svc = svc
    def op(self): return f"log({self.svc.op()})"

# 4) Proxy
class LazyProxy(Service):
    def __init__(self, factory): self._factory=factory; self._real=None
    def op(self):
        if self._real is None: self._real = self._factory()
        return self._real.op()

# 5) Composite
@dataclass
class Node:
    name: str
    children: list["Node"] | None = None
    def render(self):
        if not self.children: return self.name
        return self.name + "(" + ",".join(c.render() for c in self.children) + ")"

# 6) Flyweight (simple cache)
class Fly:
    _pool = {}
    def __new__(cls, key):
        if key not in cls._pool:
            cls._pool[key] = super().__new__(cls)
        return cls._pool[key]
