def aVeryBigSum(ar):
    i = 0
    res = 0
    
    while i < len(ar):
        res += ar[i]
        i += 1
        
    return res
    
    
print(aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))