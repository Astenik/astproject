def remove_all(data, value):
    """This function removes all members of datat that are equal to value."""
    if  not value in data:
        raise Exception('the list is not contain the value')
    ind = 0 
    while  ind < len(data):
         if data[ind] == value:
             data.remove(ind)
         ind += 1
    return  data
     
data = [9, 6, 13, 9]
print(remove_all(data, 9))
      
