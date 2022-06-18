def  fast_pow(m, n):
      """This function returns x, where m**x >= n."""
      if n == 1:
         return 1
      res = 1
      count = 0
      while res < n:
          res *= m
          count += 1
      return count
      
print("the fast_pow of m is equal:", fast_pow(6, 8))
      
