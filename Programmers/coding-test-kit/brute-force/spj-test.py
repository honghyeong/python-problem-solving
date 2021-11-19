def solution(answers):
    # 수포자 찍기 패턴
    spj_1 = [1, 2, 3, 4, 5]
    spj_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    spj_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0] * 3  # 각 수포자의 정답수

    for answer in range(len(answers)):
        if spj_1[answer % 5] == answers[answer]:
            score[0] += 1
        if spj_2[answer % 8] == answers[answer]:
            score[1] += 1
        if spj_3[answer % 10] == answers[answer]:
            score[2] += 1
    answer = []
    for index, value in enumerate(score):
        if (value == max(score)):  # 가장 높은 점수를 받은 경우 answer에 수포자 index 추가
            answer.append(index + 1)
    # 점수 sort
    answer.sort()
    return answer