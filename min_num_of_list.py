def min(data):
   """ This function returns minimal member of the data list."""
   _min = data[0]
   ind = 1
   while ind < len(data):
        if data[ind] < _min:
            _min = data[ind]
        ind += 1
   return _min
    
    
data = [3, 4, 7, 8]
print("the minimal member of data is:",  min(data))
      
