def  pascal_rec(n, m):
     """This function returns the member of pascal's triangle and carred out in a recursive way. """
    return 1 if m in (1, n) else pascal_rec(m-1, n-1) + pascal_rec(m - 1, n)
  
  
print(" member of pascal's triangle is equal:", pascal(7, 5))
