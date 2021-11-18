from collections import defaultdict


def solution(record):
    namespace = {}
    printlist = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    answer = []
    for r in record:
        rr = r.split(' ')
        if rr[0] != "Leave":
            namespace[rr[1]] = rr[2]

    for r in record:
        rr = r.split(' ')
        if rr[0] != 'Change':
            answer.append(namespace[rr[1]] + printlist[rr[0]])

    return answer