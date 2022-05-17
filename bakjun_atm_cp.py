n = int(input())
p = list(map(int, input()))
num = 0
for i in range(n):
    for j in range(j+1):
        num += p[j]
print(num)