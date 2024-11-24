def isPalindrome(s):
    left = 0
    right = len(s)-1
    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


n = int(input())
arr = [False, False] + [True] * 999999

for i in range(2, 1000001):
    if arr[i]:
        for j in range(i+i, 1000001, i):
            arr[j] = False


for i in range(n, 1000001):
    if arr[i] and isPalindrome(str(i)):
        print(i)
        break
