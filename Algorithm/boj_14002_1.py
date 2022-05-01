n = int(input())
arr = list(map(int,input().split()))
dp = [0 for _ in range(n)]
seq_arr = [[] for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and dp[j] > dp[i]:
            dp[i] = dp[j]
            seq_arr[i] = seq_arr[j]
    dp[i] += 1
    print(seq_arr[i])
    seq_arr[i].append(arr[i])

    
max = 0
answer = []
for i in range(n):
    if dp[i] > max:
        max = dp[i]
        answer = seq_arr[i]
        
print(max,answer, sep ='\n')