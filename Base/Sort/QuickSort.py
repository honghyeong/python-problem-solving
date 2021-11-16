# Quick Sort - O( n * logn) ~ O ( n**2 ) : Average : O(n * log n)

def quick_sort(Array):
    Array_length=len(Array)
    if(Array_length<=1):
        return Array
    else:
        pivot=Array[0]
        Greater=[element for element in Array[1:] if element>pivot]
        Lesser=[element for element in Array[1:] if element<=pivot]

        return quick_sort(Lesser) + [pivot] + quick_sort(Greater)
