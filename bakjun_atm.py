#예를들어 5명 a,b,c,d,e 이있다
#a = 3, b = 1, c = 4, d = 3, e = 2 분이 걸린다.
#그러므로 a = 3분 b = 4분 ...

#1. 각사람마다 걸리는 시간이 적은 수 대로 배열
#2. 순서대로 앞에서 부터 연속하여 더 함

n = int(input())
p = list(map(int,input().split()))
num = 0
p.sort()
for i in range(n):
    for j in range(i+1):
        num += p[j]
print(num)
