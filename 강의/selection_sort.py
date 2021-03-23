input = [4, 6, 2, 9, 1]

# 4 6 2 9 1  
# - - - - - 
# 1 6 2 9 4
#   - - - -
# 1 2 6 9 4
#     - - -
# 1 2 4 9 6
#       - -
# 1 2 4 6 9



def selection_sort(array):
    n = len(array)
    for i in range(n-1):
        min_index = i               #최솟값을 위한 인덱스
        for j in range(n-i):
            if array[i+j] < array[min_index]:
                min_index = i+j
        array[i], array[min_index] = array[min_index], array[i]


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!