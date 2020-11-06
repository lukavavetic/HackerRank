def staircase(n):
    x = n - 1
    
    for i in range(1, n  + 1):
        print(str(x * ' ' + i * '#'))
        x = x - 1
    


print(staircase(6))