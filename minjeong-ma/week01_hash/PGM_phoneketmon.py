def solution(nums):
    answer = 0
    n = len(nums) // 2
    nums = set(nums)
    
    if len(nums) > n:
        answer = n
    else:
        answer = len(nums)
    return answer
