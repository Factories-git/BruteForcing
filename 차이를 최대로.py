n = int(input())
arr = list(map(int, input().split()))
arr.sort()
re = 0
left = 0
right = n-1
while left <= right:
    re += abs(arr[right] - arr[left])
    left += 1
    right -= 1
print(re)