def binarySearch(lst, target):
    start, end = 0, len(lst) - 1

    while start <= end:
        mid = (start + end) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


N = int(input())
A = list(map(int, input().split()))
M = int(input())
M_arr = list(map(int, input().split()))

A.sort()
for i in range(M):
    if binarySearch(A, M_arr[i]) is not None:
        print(1)
    else:
        print(0)