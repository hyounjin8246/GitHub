L = int(input())
i = list(map(int, input().split()))
n = int(input())

i.sort()

if n in i:
    print(0)
else:
    low = 0
    high = 1001
    for I in i:
        if I < n:
            low = I
        elif I > n:
            high = min(high, I)
    print((n - low) * (high - n) - 1)