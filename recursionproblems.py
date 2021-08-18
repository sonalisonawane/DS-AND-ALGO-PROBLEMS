# sorted or not

# arr = [2,4,5,6,7,5]
# def sorted(arr):
#         if len(arr)==1:
#                 return True
#         return arr[0]<= arr[1] and sorted(arr[1:])


# print(sorted(arr))

n = int(input("enter the number"))
newList = []
for i in range(n):
    inputs = int(input("Enter N number of input"))
    newList.append(inputs)

for j in range(len(newList)):
     total = sum(newList)
     average = total/n
print(average)

 