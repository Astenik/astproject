def recursive_func(n):
     """This is a recursive function that returns n if n<3 and recursive_func(n-1)+recursive_func(n-2)+recursive_func(n-3) if n>-3"""
     if n < 3 and n >= 0:
         return n
     elif n >= 3:
          return recursive_func(n - 1) + recursive_func(n - 2) + recursive_func(n - 3)
     return -1
     
     
print("function for n is equal:", recursive_func(67))
def  iterative_func(n):
     """This is a iterative function that iterates as long as  n is not smaller than 3"""
     if n < 0:
         return -1
     num = 2
     while n >= 2:
         num += (num - 1) + (num - 2)
     return num
      
print("Iterative function is equal:", iterative_func(23))
def  tail_rec_func(n, res = 2):
      """this is a tail recursiv function that returns n if n<3 and tail_rec_func(n-1)+tail_rec_func(n-2)+tail_rec_func(n-3) if n>-3"""
      if n >= 0 and n < 3:  
          return res
      return  tail_rec_func(n - 1, res + (res - 1) + (res - 2))
         
print("the result of tail_func is equal:", tail_rec_func(45))
        
      
      
