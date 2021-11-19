def solution(distance, rocks, n):
    # distance=16
    # rocks=[8,11]
    # n=1

    a = sorted(rocks)
    interval = []
    prev = 0
    for i in a:
        interval.append(i - prev)
        prev = i
    interval.append(distance - a[-1])
    # print(interval)

    left = answer = 1
    right = distance // (len(rocks) + 1 - n)

    # print(left,right)
    while (left <= right):
        mid = (left + right) // 2
        check = -2
        count = n
        for i, v in enumerate(interval):
            if v < mid and i != check + 1:
                count -= 1
                check = i
                # print('mid',mid,'count',count,'i',i)

        if count < 0:
            right = mid - 1
        if count >= 0:
            left = mid + 1
            answer = max(answer, mid)
    # print(answer)

    return answer