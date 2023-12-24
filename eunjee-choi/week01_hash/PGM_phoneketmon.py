def solution(nums):
    answer = 0
    max = len(set(nums))

    if len(nums) / 2 > max:
        return max
    else:
        return len(nums) / 2
