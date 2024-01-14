def solution(numbers):
    numbers.sort(key=lambda x: str(x) * 3, reverse=True)
    answer = ""
    if numbers[0] == 0:
        return "0"
    for n in numbers:
        answer += str(n)
    return answer