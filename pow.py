def  pow(base, exp):
    """This function returns the exp pow of base"""
    if base > 0 and exp > 0:
        return base ** exp
    elif base > 0 and exp==0:
        return 1
    elif base > 0 and exp < 0:
        return 1 / base ** (-exp)
    elif (base == 0 and exp < 0) or base < 0:
         return -1
         
         
  print("the exp pow of base is equal:", pow(5, 7))
