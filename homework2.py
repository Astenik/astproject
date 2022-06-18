def sum_of_ints(a, b):
    """This function returns the sum of all integer numbers from  a to b"""
    sum = a + 1
    count = a
    while count <= b:
        sum += count
        count += 1
    return sum
    
print("sum of ints is equal:", sum(3, 5))
