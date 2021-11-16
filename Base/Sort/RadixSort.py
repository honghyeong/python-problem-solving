# Radix Sort : d x O (n + k)  선형 시간에 가까운 정렬 수행

# 현재 자릿수 (d)와 진법(base)에 맞는 숫자 변환
def get_digit(number,d,base):
    return (number//base**d)%base

# 자릿수 기준으로 counting sort
# A : input array
# position : 현재 자릿수
# base : 10진수라면 base=10
def counting_sort_with_digit(A,d,base):
    k=base-1               #k : ex) 10진수의 최대값 = 9
    B=[-1]*len(A)
    C=[0]*(k+1)

    #현재 자릿수를 기준으로 빈도수 세기
    for a in A:
        C[get_digit(a,d,base)]+=1
    #C 업데이트
    for i in range(k):
        C[i+1]+=C[i]

    # 현재 자릿수를 기준으로 정렬
    for j in reversed(range(len(A))):
        B[C[get_digit(A[j],d,base)]-1]=A[j]
        C[get_digit(A[j],d,base)]-=1
    return

from math import log

def radix_sort(list, base=10):
    # 입력된 리스트 가운데 최대값의 자릿수 확인
    digit = int(log(max(list), base) + 1)
    # 자릿수 별로 counting sort
    for d in range(digit):
        list = counting_sort_with_digit(list, d, base)
    return list
