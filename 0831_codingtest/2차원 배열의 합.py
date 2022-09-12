# 계속 런타임에러 발생 

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
# dp[i][j] = 1, 1 부터 (i,j) 까지의 부분합
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + a[i-1][j-1]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1])