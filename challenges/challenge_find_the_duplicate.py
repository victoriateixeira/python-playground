def find_duplicate(nums):
    if not nums or len(nums) <= 1:
        return False
    sorted_nums = sorted(nums)
    for idx, num in enumerate(sorted_nums):
        if type(num) is not int or num < 1:
            return False

        result = binary_search(sorted_nums, num, idx)
        if result != -1:
            return result
    return False


def binary_search(numbers, target, idx):
    start = 0
    end = len(numbers) - 1

    while start <= end:
        mid = (start + end) // 2

        if numbers[mid] == target and mid != idx:
            return target

        if target < numbers[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1


print(find_duplicate([1, 3, 4, 2, 2]))
