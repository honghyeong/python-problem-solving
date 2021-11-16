# Heap Sort 오름차순


def heapify(li, idx,n): # n== heap size
    l=idx*2 # left child
    r=idx*2+1 # right child
    s_idx=idx 

    if(l<=n and li[s_idx] > li[l]):  # 부모노드가 자식노드 중 더 작은것을 선택
        s_idx=l
    if(r<=n and li[s_idx] > li[r]):  # 부모노드가 자식노드 중 더 작은것을 선택
        s_idx=r
    if (s_idx != idx):
        li[idx],li[s_idx]=li[s_idx],li[idx]
        return heapify(li,s_idx,n)


def heap_sort(v):
    n=len(v)
    v=[0]+v # index를 1부터 시작하기 위해 추


    # min heap 생성
    for i in range(n,0,-1):
        heapify(v,i,n)          # unsorted list인 v를 index : n~1에 대해서 heap정의(heap 성질 유지되는지 확인하며)하며, minheap 형성

    # min element extract & heap
    for i in range(n,0,-1): 
        print(v[1])             # 루트노드 제거
        v[i],v[1]=v[1],v[i]     # 가장 마지막 노드와 위치 변경,
        heapify(v,1,i-1)        # heap 재정의 ( 다시 heap 성질 유지하는 heapify )

heap_sort([8,3,1,2,1])
