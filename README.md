# Python Basics + Design Patterns (Quick Pack)

This pack gives you:
- `basics.py` — runnable Python basics (variables, control flow, OOP, files, exceptions, decorators, typing).
- `cheatsheet.py` — tiny stdlib tour.
- `patterns/` — Pythonic implementations of classic design patterns:
  - **Creational**: Singleton, Factory Method, Abstract Factory, Builder, Prototype
  - **Structural**: Adapter, Facade, Decorator (object), Proxy, Composite, Flyweight
  - **Behavioral**: Strategy, Observer, Command, State, Template, Iterator, Mediator, Chain of Responsibility, Memento, Visitor

## How to use
```bash
python basics.py         # run basics with prints
python cheatsheet.py     # quick stdlib tour
python -c "from patterns.creational import AppConfig; print(AppConfig() is AppConfig())"
```
Patterns are intentionally compact and Pythonic (prefer modules, functions, dataclasses).

## Tips
- Create a virtual env:
  ```bash
  python -m venv .venv
  source .venv/bin/activate  # Windows: .venv\Scripts\activate
  pip install -U pip
  ```
- Use `ruff` or `flake8` for linting; `pytest` for tests.
- Use `match/case` (Python ≥3.10) for simple state machines.
