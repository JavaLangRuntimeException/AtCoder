H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# 行の合計を計算
row_sums = [sum(row) for row in A]

# 列の合計を計算
col_sums = [sum(A[i][j] for i in range(H)) for j in range(W)]

# 各マスの値を計算
B = [[row_sums[i] + col_sums[j] - A[i][j] for j in range(W)] for i in range(H)]

# 結果を出力
for row in B:
    print(*row)