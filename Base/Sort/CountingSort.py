# Counting Sort : O(n+max) ~= O(n)

def counting_sort(array,max):

    # counting array 생성
    counting_array=[0]*(max+1)

    # counting array에 input array 내 원소의 빈도수 담기
    for i in array:
        counting_array[i]+=1

    # counting array 업데이트.
    for i in range(max):
        counting_array[i+1]+=counting_array[i]

    # output array 생성
    output_array=[-1]*len(array)

    # output array에 정렬하기 (counting array를 참조)
    for i in array:
        output_array[counting_array[i]-1]=i
        counting_array[i]-=1

    return output_array


a=[2,0,1,4,5,4,3,2,0,1,1,0,5,4,3]
b=counting_sort(a,max(a))
print(b)
