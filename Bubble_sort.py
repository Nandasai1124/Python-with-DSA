def bubble_sort(arr):
    n=len(arr)
    
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
my_list=list(map(int,input().split()))

print("Original List:",my_list)
bubble_sort(my_list)
print("Sorted List:",my_list)