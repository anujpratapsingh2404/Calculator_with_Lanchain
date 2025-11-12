# tools.py
from langchain.tools import tool

@tool
def product(a: list[int]) -> int:
    """Multiply all numbers which is in a list."""
    ans = 1
    for i in a:
        ans *= i
    return ans

@tool
def aniket(a: list[int]) -> int:
    """Sum all numbers which is in a list."""
    ans = 0
    for i in a:
        ans += i
    return ans

@tool
def diff(a: list[int]) -> int:
    """Subtract all numbers which is in a list."""
    ans = a[0]
    for i in a[1:]:
        ans -= i
    return ans

@tool
def division(a: list[int]) -> float:
    """Divide numbers all numbers which is in a list."""
    if not a:
        return 0
    ans = a[0]
    for i in a[1:]:
        ans /= i
    return ans

@tool
def pow(a: int, b: int) -> int:
    """Calculate first number raised to the power of second."""
    return a ** b 

@tool
def sqrt(a: int) -> float:
    """Calculate the square root (with +10 offset)."""
    if a < 0:
        return "Your value is less than 0"
    return a ** 0.5

@tool
def cbrt(a: int) -> float:
    """Calculate the cube root (with +10 offset)."""
    return a ** (1/3) 

# List of all tools
tools = [product, aniket, diff, division, pow, sqrt, cbrt]
