NumPy is a powerful Python library used for:
- numerical computing
- arrays
- matrix operations
- mathematical calculations
- AI and Machine Learning

---

# Why NumPy?

NumPy is:
- faster than Python lists
- memory efficient
- widely used in AI/ML
- foundation of Pandas, TensorFlow, PyTorch

---

# Installation

```bash
pip install numpy
````

---

# Import NumPy

```python
import numpy as np
```

---

# Creating Arrays

```python
import numpy as np

arr = np.array([1,2,3,4])

print(arr)
```

---

# Array Operations

```python
import numpy as np

arr = np.array([1,2,3])

print(arr + 2)
print(arr * 2)
```

---

# Array Attributes

```python
print(arr.shape)
print(arr.ndim)
print(arr.size)
```

---

# Indexing & Slicing

```python
print(arr[0])
print(arr[1:3])
```

---

# Reshape Array

```python
arr = np.array([1,2,3,4])

print(arr.reshape(2,2))
```

---

# Common NumPy Functions

| Function        | Use                  |
| --------------- | -------------------- |
| `np.array()`    | create array         |
| `np.zeros()`    | array of zeros       |
| `np.ones()`     | array of ones        |
| `np.arange()`   | range array          |
| `np.linspace()` | evenly spaced values |
| `np.mean()`     | average              |
| `np.sum()`      | total sum            |
| `np.max()`      | maximum value        |
| `np.min()`      | minimum value        |

---

# Example

```python
import numpy as np

arr = np.array([1,2,3,4,5])

print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
```

---

# Matrix Operations

```python
import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(a + b)
print(np.dot(a,b))
```

---

# Random Numbers

```python
import numpy as np

print(np.random.rand(3))
```

---

# Why NumPy is Important for AI?

NumPy is used in:

* Machine Learning
* Deep Learning
* Data Science
* Computer Vision
* AI Engineering
* LLM pipelines

Libraries like:

* Pandas
* TensorFlow
* PyTorch
* Scikit-learn

are built heavily on NumPy.

---

# Learning Roadmap

1. Arrays
2. Indexing
3. Slicing
4. Reshape
5. Matrix Operations
6. Statistics Functions
7. Broadcasting
8. Random Module



```
```
