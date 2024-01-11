def solution(prices):
    answer = [0] * len(prices)
    st = [[0, 0, 0]]
    for i, p in enumerate(prices):
        # print("stack:", st)
        while st[-1][1] > p:
            tmp = st.pop(-1)
            # print("poped:", tmp)
            answer[tmp[0]] = tmp[2]
        st.append([i, p, 0])
        for s in st:
            if i != len(prices) - 1:
                s[2] += 1
    st.pop(0)
    for s in st:
        answer[s[0]] = s[2]
    # print(st)
    return answer