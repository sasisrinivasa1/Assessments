import numpy

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [1,2,3,4],
    [5,6,7,8]
]

arr = numpy.array(matrix)

print("Transpose matrix :: \n", arr.transpose())

# Output:-
# PS C:\Users\ssrinivasa1\Desktop\Assessments> python .\FA2_Qn-14.py
# Transpose matrix :: 
#  [[1 5 1 5]
#  [2 6 2 6]
#  [3 7 3 7]
#  [4 8 4 8]]