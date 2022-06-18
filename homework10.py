def max(data):
   """ This function returns maximal member of the data list."""
   _max = data[0]
   ind = 1
   while ind < len(data):
        if data[ind] > _max:
            _max = data[ind]
        ind += 1
    return _max
    
    
data = [3, 4, 7, 8]
print("the maximal member of data is:",  max(data))
      
