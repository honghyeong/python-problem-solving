from collections import Counter

def solution(participant, completion):
    answer = ''
    p = dict(Counter(participant))
    c = dict(Counter(completion))
    # print(p)
    # print(c)
    for k, v in p.items():
        try:
            if v - c[k] > 0:
                answer = k
        except Exception as e:
            answer = k

    return answer