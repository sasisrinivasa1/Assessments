def solution(arr):
    arr1 = []
    count = 0
    for i in range(0,len(arr)):
        count += 1
        print(count)
        for j in range(0,len(arr)):
            sum = 0
            sum = sum + arr[i] + arr[j]
            arr1.append(sum)
    print(arr1)

        


if __name__ == '__main__':
    arr = [4,4,5,3]
    solution(arr)
