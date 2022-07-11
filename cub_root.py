def  cub_root(n):
    """this function returns the cubic root of n"""
    c_root = 1
    while not guess_enough(c_root, n):
          root = improve(c_root, n)
    return c_root
def guess_enough(c_root, k):
     """This function returns true if we have already guess the cubic root of k"""
    if abs(c_root**3 - k) < 0.0001:
        return true 
     return false
def improve(c_root, h):
    return ((h / (c_root**2)) + 2*c_root) / 3
    
 num = 8
print("the cubic root of num is equal:", cub_root(num))
