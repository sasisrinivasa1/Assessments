from math import sqrt

arr = [16,6,8,4,144]
perfect_sqrt_arr = []
for i in range(0,len(arr)):
    num = arr[i]
    for j in range(2,len(arr)):
        f = float(j)
        if sqrt(num) % f == 0:
            perfect_sqrt_arr.append(num)
            break
print(perfect_sqrt_arr)

# Output:-
# PS C:\Users\Sasikumar S\PythonAssessments> python .\FA2_Qn-11.py
# [16, 4, 144]