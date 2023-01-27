def smallest_positive_integer(arr):
	m = max(arr)
	if m < 1:
		return 1
	if len(arr) == 1:
		return 2 if arr[0] == 1 else 1
	l = [0] * m
	for i in range(len(arr)):
		if arr[i] > 0:
			if l[arr[i] - 1] != 1:
				l[arr[i] - 1] = 1
	for i in range(len(l)):
		if l[i] == 0:
			return i + 1
	return i + 2

if __name__ == '__main__':
	arr = [-1,1,2,3,0,-2,7,8]
	print("Smallest Positive Integer is ", smallest_positive_integer(arr))

# Output:-
# PS C:\Users\ssrinivasa1\Desktop\Assessments> python .\FA1_Qn-1.py
# Smallest Positive Integer is  4