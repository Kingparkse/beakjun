import sys

n = int(sys.stdin.readline())
money = [int(sys.stdin.readline()) for _ in range(n)]
money.sort(reverse = True)
result = 0

for i in range(n):
    tip = money[i] - i
    if tip >0:
        result += tip
        
print(result)