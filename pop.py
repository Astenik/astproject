def pop(data, ind = None):
     """This function remove the last number of data list if ind = None else removes ind-th element."""
     if ind == None:
         num = data[len(data) - 1]
         data.remove(data[len(data) - 1])
     else:
           num = data[ind]
           data.remove(data[ind])
     return num
data = [9, 87, 54, 67]
print(pop(data, 2))
