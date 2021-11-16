#134 : Greedy...?

# 불가능한 경우부터 유일한 출발점을 찾기위해 제거하는 과정이 greedy하다고 봐야될 듯.

# O(n2) - brute force algorithm
# visit all gas station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for start in range(len(gas)):
            fuel=0
            for i in range(start,len(gas)+start):
                index=i%len(gas)

                can_travel=True

                if gas[index]+fuel<cost[index]: # 다음 주유소로 이동이 불가능하다면,
                    can_travel=False
                    break
                else:
                    fuel+=gas[index]-cost[index] # fuel 변화량

            if can_travel:
                return start
        return -1

# Greedy Algorithm   
# 불가능한 경우부터 유일한 출발점을 찾기위해 제거하는 과정이 greedy하다고 봐야될 듯.

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas)<sum(cost):
            return -1

        fuel=0
        start=0
        for i in range(len(gas)):
            # 출발점이 될 수 없는 지점 선별
            if gas[i]+fuel<cost[i]: # 출발부터 불가능한 지점 선별
                fuel=0
                start=i+1
            else:
                fuel+=gas[i]-cost[i] # 출발은 가능한 경우 fuel 누적
        return start
