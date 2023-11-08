# quick sort (divide and conquer)

# best case - O(nlogn)
# average case - O(nlogn)
# worst case - o(n^2)

def partition(arr, low, high):
    pi=arr[low]
    p=low+1
    q=high
    
    while True:
        if p<=q and arr[p]<=pi:
            p+=1
        elif p<=q and arr[q]>=pi:
            q-=1
        if p<=q:
            arr[p], arr[q]=arr[q], arr[p]
        else:
            break
    arr[low], arr[q]=arr[q], arr[low]
    return q
    
def solveQuickSort(arr, low, high):
    if low<high:
        pi=partition(arr, low, high)
        solveQuickSort(arr, low, pi-1)
        solveQuickSort(arr, pi+1, high)
        
arr=[15, 23, 11, 56, 76, 43, 23]
print(arr)
solveQuickSort(arr, 0, len(arr)-1)
print(arr)