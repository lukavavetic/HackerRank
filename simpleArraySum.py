def simpleArraySum(ar):
    i = 0
    res = 0
    
    while i < len(ar):
        res += ar[i]
        i += 1
        
    return res

print(simpleArraySum([1, 2, 3, 4, 10, 11]))
    