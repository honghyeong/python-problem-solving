from collections import defaultdict


def solution(record):
    userlist = defaultdict(list)
    printlist = []
    answer = []
    for rcd in record:
        temp = rcd.split()
        if temp[0] != "Leave":
            userlist[temp[1]].append(temp[2])

    for rcd in record:
        rcd_split = rcd.split()
        temp = []
        if rcd_split[0] != "Change" and rcd_split[1] in userlist.keys():
            temp.append(rcd_split[0])
            temp.append(userlist[rcd_split[1]][-1])
            printlist.append(temp)

    for line in printlist:
        nickname = line[1]
        action = "님이 들어왔습니다." if line[0] == "Enter" else "님이 나갔습니다."
        answer.append(nickname + action)

    return answer