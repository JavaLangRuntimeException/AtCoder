N, L, R = map(int, input().split())

List = []

for i in range(1, N+1):
    if L <= i <= R:
        List.append(L + R - i)
    else:
        List.append(i)

print(*List)