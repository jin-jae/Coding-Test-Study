def solution(s):
    stack = 0
    for e in s:
        stack += 1 if e == "(" else -1
    if stack != 0:
        return False
    return True