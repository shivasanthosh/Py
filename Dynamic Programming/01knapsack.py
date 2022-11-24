val = [6, 10, 12]
weight = [10, 20, 30]
w = 50
n = len(val)
dp = [[-1 for _ in range(w + 1)] for _ in range(n + 1)]



def knapscak(n, w):
    if n == 0 or w == 0:
        return 0
    if dp[n][w] != -1:
        return dp[n][w]

    if weight[n - 1] > w:
        # reject
        dp[n][w] = knapscak(n - 1, w)
        return dp[n][w]
    else:
        dp[n][w] = max(val[n - 1] + knapscak(n - 1, w - weight[n - 1]), knapscak(n - 1, w))
        return dp[n][w]


x = knapscak(n, w)
print(x)
