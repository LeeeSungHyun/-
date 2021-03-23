finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]
# newnum = [0, 1, 2, 3, 4, 5, 6]
def is_exist_target_number_binary(target, numbers):
    start = 0
    end = len(numbers) - 1 
    mid = (start + end) // 2
    newnum = sorted(numbers)
    while start <= end:
        if newnum[mid] == target:
            return True
        elif newnum[mid] < target:
            start = newnum[mid] + 1
        else:
            end = newnum[mid] - 1
        mid = (start+end) // 2
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)

print(result)