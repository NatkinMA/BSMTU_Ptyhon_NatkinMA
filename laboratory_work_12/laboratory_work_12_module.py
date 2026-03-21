"""
Модуль с математическими функциями.
"""

# import

__all__ = ['add', 'multiply']

# Константы
_PI = 3.14159

# Функции
def add(a, b):
    return a + b

def _substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def _divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль невозможно.")
    else:
        return a/b

#print(add(10, 5))


if __name__ == "__main__":
    print(add(5, 10))
    print(_substract(5, 10))
    print(multiply(5, 10))
    print(_divide(5, 10))
    print(_PI)
else:
    print("Модуль импортирован.")
