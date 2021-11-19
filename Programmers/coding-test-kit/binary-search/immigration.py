def solution(n, times):
    # 최소심사시간, 최대 심사시간
    left = min(times)
    answer = right = min(times) * n
    #binary search
    while (left <= right):
        mid = (left + right) // 2
        capability = 0
        for time in times:
            capability += (mid // time)
        if (capability >= n):
            right = mid - 1
            answer = min(answer, mid)
        else:
            left = mid + 1

    return answer