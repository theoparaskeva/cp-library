list = [12,-5,14,65,-4]
n = len(list)
current_max = list[0]
final_max = list[0]

for x in range(1,n):
    current_max = max(list[x],current_max+ list[x])
    final_max = max(final_max,current_max)

print(final_max)