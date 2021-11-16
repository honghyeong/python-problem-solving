# 621
# 많은 빈도의 task를 먼저 사용하는 greedy choice


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter=collections.Counter(tasks)
        result=0

        while True:
            sub_count=0
            #개수 순 추출
            for task, _ in counter.most_common(n+1):
                sub_count+=1
                result+=1

                counter.subtract(task)
                # 0 이하인 아이템을 목록에서 완전히 제거;  Hack
                counter+=collections.Counter()

            if not counter:
                break

            result+=n+1-sub_count # 추가 idle 처리

        return result
