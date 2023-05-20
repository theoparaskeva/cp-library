### Kadane's Algorithm
### maxiumum subarray

list = [12,-5,14,65,-4]
n = len(list)
# set to first element in list
current_max = list[0]
# set to first element in list
final_max = list[0]

for x in range(1,n):
    # list[x] vs current_max + list[x] 
    #checks if the current element is more than the previous cumulative subarray
    current_max = max(list[x],current_max+ list[x])
    # checks if the new subarray value is the largest
    final_max = max(final_max,current_max)

print(final_max)


