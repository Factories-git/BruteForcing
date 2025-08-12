ans = float('inf')
n = int(input())
arr = list(map(int, input().split()))
if n == 1:
    print(0)
    exit()
for i in [-1, 0, 1]:
    for j in [-1, 0, 1]:
        a0 = arr[0] + i # 가만히 두거나, -1 연산을 하거나, +1 연산을 하거나임.
        a1 = arr[1] + j
        if a1 - a0 != 1: # 공차가 1인 등차수열이니 나머지 필요 없음.
            continue
        unable = False
        differ = 1
        count = 0
        if i != 0:
            count += 1
        if j != 0:
            count += 1
        prev = a1
        for k in range(2, n):
            tar = prev + differ # 타겟(다음 공차인 애)
            if abs(arr[k] - tar) > 1: # 2 이상이면 아무리 연산해도 소용없음
                unable = True
                break
            if arr[k] != tar: #타겟이랑 다르고, 차이가 1 이하면 바꿀 수 있음
                count += 1
            prev = tar # 계속 갱신하며 타겟 변경
        if not unable: # 변경 가능하면
            ans = min(ans, count) # 최솟값으로 변경
print(ans if ans != float('inf') else -1) # 만약 어떤 경우를 해도 안된다면 -1 출력