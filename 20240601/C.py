N, M, K = map(int, input().split())
A = [list(map(int, input().split())) + [input().strip()] for _ in range(M)]

count = 0
for i in range(2**N):
    keys = [int(i // (2**j) % 2) for j in range(N)]
    valid = True
    for a in A:
        count_true_keys = sum(keys[key - 1] for key in a[:-1])
        if (a[-1] == 'o' and count_true_keys < K) or (a[-1] == 'x' and count_true_keys >= K):
            valid = False
            break
    if valid:
        count += 1

print(count)

# わからんかった https://atcoder.jp/contests/abc356/tasks/abc356_c