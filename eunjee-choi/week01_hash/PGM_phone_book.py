def solution(phone_book):
    answer = True
    sorted_phone_book = sorted(phone_book)

    for a, b in zip(sorted_phone_book, sorted_phone_book[1:]):
        if b.startswith(a):
            answer = False
            return answer
    return answer
