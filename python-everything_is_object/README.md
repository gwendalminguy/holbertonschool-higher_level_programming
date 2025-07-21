# Python - Everything Is Object

In Python, everything is an object. Understanding how Python handles variables, object identity, mutability, and function arguments is essential for writing correct and predictable code. This document provides an overview of core concepts including the nature of objects, how Python handles variable references and assignments, the difference between mutable and immutable objects, and the implications for function arguments.

## Type and Identifier

Every object in Python has:
- A **type**, which defines what kind of object it is.
- An **identifier** (ID), which uniquely identifies the object during its lifetime.

Built-in functions `type()` and `id()` can be used to inspect these properties:

```python
x = 42
print(type(x))  # <class 'int'>
print(id(x))    # 140352130391248
```

The `id()` value is unique for an object during its lifetime and is commonly its memory address.

## Mutable Objects

These are objects whose content can be changed after creation. Mutable objects include:

- `list`
- `dict`
- `set`

### Example:

```python
l1 = [1, 2, 3]
l2 = l1
l2.append(4)

print(l1)         # [1, 2, 3, 4]
print(l1 is l2)   # True
```

## Immutable Objects

These are objects whose content cannot be changed once they are created. Immutable objects include:

- `int`
- `float`
- `bool`
- `str`
- `tuple`

### Example:

```python
x = 10
y = x
y += 1

print(x)        # 10
print(y)        # 11
print(x is y)   # False
```

## Reference, Assignment, and Aliasing

- **Assignment** creates a reference from a variable name to an object.
- **Aliasing** creates a reference with a different name to the same object.
- Identity operator (`is`) checks if two variables point to the same object.
- Equality operator (`==`) checks if values are equal, not necessarily the same object.

Understanding mutability and object identity helps avoid unintended side effects:

```python
l1 = [1, 2]
l2 = l1
print(a == b)     # True
print(l1 is l2)   # True

l1 = [1, 2]
l2 = l1[:]
print(l1 == l2)   # True
print(l1 is l2)   # False
```

## Function Argument Passing

Python passes **object references** to functions. This is often referred to as **call by object reference** or **call by sharing**.

- If a **mutable** object is passed, changes inside the function can affect the original object.
- If an **immutable** object is passed, changes inside the function create a new object.

### Mutable:

```python
def append(list):
    list.append(4)

my_list = [1, 2, 3]
append(my_list)
print(my_list)  # [1, 2, 3, 4]
```

### Immutable:

```python
def increment(n):
    n += 1
    print("Inside:", n)

x = 10
increment(x)          # Inside: 11
print("Outside:", x)  # Outside: 10
```

## Summary

Understanding how Python handles object identity, mutability, and function arguments helps write safer and more predictable code.

| Concept | Description |
|---------|-------------|
| Object | A structure in memory with a type and ID |
| Mutable | Can be changed after creation |
| Immutable | Cannot be changed after creation |
| Reference | A variable pointing to an object |
| Assignment | Binds a variable name to an object |
| Alias | Two variables referring to the same object |
| `is` | Checks if two variables refer to the same object |
| `==` | Checks if two variables have equal values |
