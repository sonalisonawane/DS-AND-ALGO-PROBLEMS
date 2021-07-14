# bubbleSort


# def BubbleSort(arr):
#     n = len(arr)
#     for i in range(n-1):
#         for j in range(0,n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]

# arr = [3,7,1,2,10,2]

# print(BubbleSort(arr))



# Max till i'th Element

# def Max_till_ith(arr):
#     max = 0
#     newarr=[]
#     for i in range(len(arr)):
#         if arr[i]>max:
#             max = arr[i]
#             newarr.append(max)
#         else:
#             newarr.append(max)
#     print(newarr)
# arr = [3,5,2,1,6,2]
# Max_till_ith(arr)


# sum of all subarrays
# subarrays are subsesquences which are continuos and there are n * (n+1)/2 number of subarrays are present in one array of length n

# def sumOfSubarray(arr):
#     current = 0  #initialization
#     for i in range(len(arr)):
#         current = 0 #this current is for empty the current value in previous ith iteration
#         for j in range(i,len(arr)):
#             current += arr[j]
#             print(current)

# arr = [1,2,0,7,2]
# sumOfSubarray(arr) # subarrays are :[1][1,2][1,2,0],[1,2,0,7][1,2,0,7,2],[2],[2,0],[2,0,7],[2,0,7,2],[0],[0,7],[0,7,2],[7],[7,2],[2]


