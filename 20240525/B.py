size = input().split()
A = input().split()
B = input().split()

A = [int(i) for i in A]
B = [int(i) for i in B]

for i in range(int(size[0])):
    for j in range(len(A) - i - 1):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]

for i in range(int(size[1])):
    for j in range(len(B) - i - 1):
        if B[j] > B[j + 1]:
            B[j], B[j + 1] = B[j + 1], B[j]

C = A + B

for i in range(int(size[0]) + int(size[1])):
    for j in range(len(C) - i - 1):
        if C[j] > C[j + 1]:
            C[j], C[j + 1] = C[j + 1], C[j]

found = False
for i in range(len(C) - 1):
    if C[i] in A and C[i + 1] in A:
        found = True
        break

if found:
    print("Yes")
else:
    print("No")