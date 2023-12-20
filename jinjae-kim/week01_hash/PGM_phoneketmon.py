def solution(nums):
    nums_dict = {}
    for num in nums:
        if num not in nums_dict:
            nums_dict[num] = 0
        else:
            nums_dict[num] += 1
    return min(len(nums_dict), len(nums) / 2)