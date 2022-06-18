def revers(data):
    """This function reverses the layout of the data list."""
    data1 = [None] * len(data) - 1
    i = 0
    j = len(data) - 1
    while j >= 0 and i < len(data):
       data1[i] = data[j]
       i += 1
       j -= 1
    return data1
    t
    
data = [8, 9, 24, 9]
print("The reveres version of data is:", revers(data))
    
