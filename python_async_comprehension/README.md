# Python - Async Comprehension

This project focuses on practicing asynchronous programming in Python, specifically around generators, comprehensions, and measuring execution time in parallel execution.

## 📚 Topics Covered

- `async` and `await`
- Creating asynchronous generators
- Using `async for` loops
- Running multiple coroutines in parallel with `asyncio.gather`
- Measuring execution time of asynchronous code

## 🗃️ Files Description

| File | Description |
|------|-------------|
| `0-async_generator.py` | Contains `async_generator()` that yields 10 random floats (0–10) with a 1-second delay between each |
| `1-async_comprehension.py` | Contains `async_comprehension()` that collects 10 numbers from `async_generator()` using async comprehension |
| `2-measure_runtime.py` | Contains `measure_runtime()` that runs `async_comprehension()` 4 times in parallel and measures total runtime (~10s) |

---

## ⚙️ Usage

To test the output of a file, run:

```bash
python3 <filename>.py
```

---

## ✍️ Author
[Meshari - M0simi](https://github.com/M0simi)
