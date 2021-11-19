import itertools


def solution(numbers):
    answer = 0
    permute = set()
    # 가능한 문자열 순열을 permute에 추가
    for i in range(1, len(numbers) + 1):
        permute|=set(map(int,map(''.join, itertools.permutations(list(numbers), i))))
        # int로 변경했을때 겹치는 값 제거

    # 소수 체크 함수
    def is_prime(number):
        if number == 1 or number == 0:
            return False
        for i in range(2, number):
            if (number % i == 0):
                return False
        return True

    for per in permute:
        if is_prime(per):
            answer += 1

    return answer