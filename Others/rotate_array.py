"""
Rotating an array by 90 degrees clockwise

arr = \
[[1, 2, 3], 
 [4, 5, 6], 
 [7, 8, 9]]

Ans:
[[7, 4, 1], 
 [8, 5, 2], 
 [9, 6, 3]]
"""
arr = \
[[1, 2, 3], 
 [4, 5, 6], 
 [7, 8, 9]]

larger_arr = \
[[1,  2, 3, 4],
 [5,  6, 7, 8],
 [9, 10,11,12],
 [13,14,15,16]]


def rotate(arr):
    # transpose matrix: row to col
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            temp = arr[i][j]
            arr[i][j] = arr[j][i]
            arr[j][i] = temp
    
    # flip horizontically
    for i in range(len(arr)):
        for j in range(len(arr) // 2):
            temp = arr[i][j]
            arr[i][j] = arr[i][len(arr) - 1 - j]
            arr[i][len(arr) - 1 - j] = temp
    
    return arr

print(rotate(larger_arr))

print(0xff == ord("q"))
