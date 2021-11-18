def solution(s):
    result = []
    for width in range(1, len(s) // 2 + 1):
        cnt = 0
        temp = ""
        for i in range(0, len(s), width):
            if s[i:i + width] != s[i + width:i + 2 * width]:
                if cnt > 0:
                    temp += str(cnt + 1) + s[i:i + width]
                    cnt = 0

                else:
                    temp += s[i:i + width]
            else:
                cnt += 1

        result.append(temp)

    answer = len(s)
    for i in result:
        answer = min(len(i), answer)

    return answer