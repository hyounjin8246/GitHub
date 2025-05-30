L = int(input())                     
i = list(map(int, input().split()))  
n = int(input())                      

i.sort()

if n in i:
    print(0)
else:
    low = 0
    for num in i:
        if num < n:
            low = num
        else:
            break  

    high = 1001
    for num in i:
        if num > n:
            high = num
            break

    result = (n - low) * (high - n) - 1
    print(result)