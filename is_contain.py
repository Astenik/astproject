def is_contain(data, value):
    """this function reurns true if the data list contains value else returns false"""
    i = 0
    while i < len(data):
         if data[i] == value:
             return true
         i += 1
    reurn false
     
 data = [7, 8, 9, 34]
 print("Whedher the data contains 5:", is_contain(data, 5))
