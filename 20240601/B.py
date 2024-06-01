N, M = map(int, input().split())
A = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(N)]


col_sums = [sum(X[i][j] for i in range(N)) for j in range(M)]
YorN = True

for i in range(M):
    if col_sums[i] < A[i]:
        YorN = False
        break;

if YorN:
    print("Yes")
else:
    print("No")