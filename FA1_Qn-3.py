arr1 = [10,20,30,40,60]
arr2 = [70,80,90,100,200]
nevenarr1 = []
noddarr1 = []
nevenarr2 = []
noddarr2 = []
for i in range(0,len(arr1)):
    if i == 0:
        nevenarr1.append(arr1[i])
    if i > 0:
        if i%2 == 0:
            nevenarr1.append(arr1[i])
        else:
            noddarr1.append(arr1[i])
# print(nevenarr1)

for j in range(0,len(arr2)):
    if j == 0:
        nevenarr2.append(arr2[j])
    if j > 0:
        if j%2 == 0:
            nevenarr2.append(arr2[j])
        else:
            noddarr2.append(arr2[j])
# print(noddarr2)

sum1 = 0

for k in range(0,len(nevenarr1)):
    sum1 = sum1 + nevenarr1[k]
# print(sum1)

sum2 = 0
for l in range(0,len(noddarr2)):
    sum2 = sum2 + noddarr2[l]
# print(sum2)

print("Output :", sum1+sum2)