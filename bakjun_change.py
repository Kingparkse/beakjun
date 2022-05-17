n = int(input())

a = n%5
b = n//5
if n==1 or n==3:
    print(-1)
elif a%2 == 0:
    print(b + a//2)
else :
    print(b-1 +(a+5)//2)