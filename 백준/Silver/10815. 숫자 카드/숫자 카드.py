def binarySearch(arr, target):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None


N = int(input())
sang = list(map(int, input().split()))
M = int(input())
cards = list(map(int, input().split()))

sang.sort()
res = []
for i in cards:
    if binarySearch(sang, i) is not None:
        res.append(1)
    else:
        res.append(0)

print(*res)