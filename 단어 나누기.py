msg = input()
min_str = 'z' * 50
for i in range(1, len(msg)-1):
    for j in range(i+1, len(msg)):
        temp = msg[i-1::-1] + msg[j-1:i-1:-1] + msg[:j-1:-1]
        if temp < min_str:
            min_str = temp
print(min_str)