arr = [1, 2, 'a', 'b', '3', 'c', '4', 'd', 5]
output = []
for i in range(0,len(arr)):
    if type(arr[i]) == type(int("1")):
        output.append(arr[i])
print(output)