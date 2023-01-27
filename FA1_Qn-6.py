import numpy

def adddiag(n):
    sum = 0
    for i in range(0,len(n)):
        sum = sum + n[i]
    return sum


arr = ([1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,8])
arr1 = numpy.diagonal(arr)
print("Output :: ", adddiag(arr1))

# Output:-
# PS C:\Users\ssrinivasa1\Desktop\Assessments> python .\FA1_Qn-6.py
# Output ::  18