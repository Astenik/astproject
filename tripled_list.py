def triple(data):
     """This function returns list consist of 3 times laeger members of the data."""
     res = []
     for num in data:
        res.append(num*3)
     return res
    
data = [7, 9, 0]
print("the 3 times larger list of data is:",triple(data))
