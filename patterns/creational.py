"""Creational patterns (Pythonic)."""
from __future__ import annotations
from dataclasses import dataclass, field
from copy import deepcopy

# 1) Singleton (module-level or metaclass)
class Singleton(type):
    _inst = None
    def __call__(cls, *a, **k):
        if not cls._inst:
            cls._inst = super().__call__(*a, **k)
        return cls._inst

class AppConfig(metaclass=Singleton):
    def __init__(self): self.debug = True

# 2) Factory Method
class Document:
    def render(self): raise NotImplementedError

class PDF(Document):
    def render(self): return "PDF"

class HTML(Document):
    def render(self): return "HTML"

def doc_factory(kind: str) -> Document:
    return {"pdf": PDF, "html": HTML}[kind.lower()]()

# 3) Abstract Factory
class Widget: ...
class WinButton(Widget): ...
class MacButton(Widget): ...

class UIFactory:
    def button(self) -> Widget: raise NotImplementedError

class WinFactory(UIFactory):
    def button(self) -> Widget: return WinButton()

class MacFactory(UIFactory):
    def button(self) -> Widget: return MacButton()

# 4) Builder
@dataclass
class Meal:
    main: str = ""; sides: list[str] = field(default_factory=list)

class MealBuilder:
    def __init__(self): self.m = Meal()
    def main(self, v): self.m.main = v; return self
    def add_side(self, v): self.m.sides.append(v); return self
    def build(self) -> Meal: return deepcopy(self.m)

# 5) Prototype
@dataclass
class Prototype:
    x: int
    meta: dict
    def clone(self) -> "Prototype": return deepcopy(self)
