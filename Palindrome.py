n = int(input())

g = [list(input()) for _ in range(n)]

for i in range(n):
    h = [s[i] for s in g if i < len(s)]
    if h == h[::-1]:
        print('YES')
    else:
        print('NO')
