def sum_of_quadras(a, b, c):
    """This project counts the sum of quadras of two max numbers."""
    if a > c and  b > c:
        return a**2 + b**2
    elif  a > b and c > b:
        return a**2 + c**2
    elif  b > a and c > a:
         return b**2 + c**2
print("the sum of quadras is equal:", sum_of_quadras(5, 7, 8))
