n = int(input())
m = list(map(int, input().split()))
c = list(map(int, input().split()))

res = 0
l = c[0]
for i in range(n-1):
    if c[i] < l:
        l = c[i]
    res += l * m[i]
    
print(res)