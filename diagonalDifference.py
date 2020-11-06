#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
        
def diagonalDifference(arr):
    leftSum = 0
    rightSum = 0
    j = 0
    z = len(arr) - 1

    for i in range(0, len(arr)):
        leftSum += arr[i][j]
        rightSum += arr[i][z]

        j = j + 1
        z = z - 1

    
    return abs(leftSum - rightSum)
    

ar = [[11, 2, 4],
      [4, 5, 6],
      [10, 8, -12]]

print(diagonalDifference(ar))