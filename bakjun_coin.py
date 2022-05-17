#준규 동전 n개의 종류
#동전을 적절히 사용해서 가치합 k
#필요한 동전의 최소갯수

#첫째줄에 n k주어짐
#1<=n<=10
#1<=k<=100000000


n,k=map(int,input().split())
coin_lst = list()
for i in range(n):
    coin_lst.append(int(input()))
    
count = 0
for i in reversed(range(n)):
    count += k//coin_lst[i]
    k = k%coin_lst[i]
print(count)