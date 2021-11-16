def zero_one_knapsack(cargo):
    capacity=15
    pack=[]

    # 짐의 최대개수 +1 X 배낭의 최대 용량 +1 테이블 생성
    for i in range(len(cargo)+1):
        pack.append([])
        for c in range(capacity+1):
            if i==0 or c==0:
                pack[i].append(0)
            elif cargo[i-1][1]<=c: # 짐 2개째일때, cargo에서는 index 1 이므로
                pack[i].append(
                    max(
                        cargo[i-1][0]+pack[i-1][c-cargo[i-1][1]], # i번째 짐을 싣는경우
                        pack[i-1][c] # i번째 짐을 싣지 않는경우
                    )
                )
            else:
                pack[i].append(pack[i-1][c]) # i번째 짐을 싣을수 없으므로, i-1개 짐을 실었을때 그대로 간다

    return pack[-1][-1]

cargo=[
    (4,12),
    (2,1),
    (10,4),
    (1,1),
    (2,2)
]

r=zero_one_knapsack(cargo)
