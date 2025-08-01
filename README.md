# python-dictionary


﻿# Original dictionary: {'name': 'Alice', 'age': 25, 'city': 'New York'}
﻿# Name: Alice
﻿# After adding job: {'name': 'Alice', 'age': 25, 'city': 'New York', 'job': 'Engineer'}
﻿# After updating age: {'name': 'Alice', 'age': 26, 'city': 'New York', 'job': 'Engineer'}
﻿# After removing city: {'name': 'Alice', 'age': 26, 'job': 'Engineer'}
﻿# Key 'name' exists!
﻿# Key-Value pairs:
﻿# name → Alice
﻿# age → 26
﻿# job → Engineer



Here's a quick guide to **Python dictionaries** — compact and clear.

---

## 🧠 What Is a Dictionary?

A **dictionary** is a built-in data type in Python that stores data as **key–value pairs**.

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
```

---

## ✅ Basic Dictionary Operations

| Action           | Example                   |
| ---------------- | ------------------------- |
| Create           | `d = {"a": 1, "b": 2}`    |
| Access value     | `d["a"]` → `1`            |
| Add key-value    | `d["c"] = 3`              |
| Update value     | `d["a"] = 100`            |
| Delete key       | `del d["b"]`              |
| Check key exists | `"a" in d` → `True`       |
| Get value safely | `d.get("x", "not found")` |
| Keys only        | `d.keys()`                |
| Values only      | `d.values()`              |
| Key-value pairs  | `d.items()`               |
| Clear all items  | `d.clear()`               |
| Copy dictionary  | `d.copy()`                |

---

## 🔁 Loop Through Dictionary

```python
for key, value in d.items():
    print(key, "→", value)
```

---

## 🧱 Dictionary Nesting

```python
students = {
    "alice": {"age": 20, "grade": "A"},
    "bob": {"age": 22, "grade": "B"}
}
```

---

## 🔄 Dictionary Methods

* `update()` – Update/add multiple items
* `pop(key)` – Remove and return value
* `popitem()` – Remove and return **last inserted** item
* `setdefault(key, default)` – Get value or insert default
* `fromkeys(keys, value)` – Create dict from list of keys

---

