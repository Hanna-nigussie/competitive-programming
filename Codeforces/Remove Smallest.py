for _ in range(int(input())):
    input()
    a=set(map(int,input().split()))
    print('YES' if max(a)-min(a)==len(a)-1 else 'NO')