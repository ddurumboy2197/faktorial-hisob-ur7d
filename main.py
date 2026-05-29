def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)
```

```python
def faktorial(n):
    if n < 0:
        raise ValueError("Faktorial berilgan son uchun mavjud emas")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
```

```python
import math

def faktorial(n):
    if n < 0:
        raise ValueError("Faktorial berilgan son uchun mavjud emas")
    else:
        return math.factorial(n)
