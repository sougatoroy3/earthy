def sumOrProduct(n, q):
    sum=0
    prod=1
    for i in range(1, n+1):
            sum+=i
            prod=prod*i
    if q==1:
        return sum
    elif q==2:
        return prod

N=int(input())
Q=int(input())
out=sumOrProduct(N, Q)
print(out)