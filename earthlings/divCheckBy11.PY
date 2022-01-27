# if the number formed by first digits of first half and last digits of 2nd half is %11==0
def solve(A):
    # Write your code here
    nos=0
    nos2=0
    midIndex=N//2
    firstHalf=A[:midIndex]
    secondHalf=A[midIndex:]
    #print(firstHalf, secondHalf)

    for i in firstHalf:
        el1=(firstDigit(i))
        nos=(nos*10)+el1
    #print(nos)
    
    for j in secondHalf:
        el2=j%10
        nos2=(nos2*10)+el2
    #print(nos2)

    num=str(nos)+str(nos2)
    #print(num)

    sum=int(num)
    if sum%11==0:
        output= 'OUI'
    else:
        output= 'NON'

    return output

def firstDigit(n) :
 
    # Remove last digit from number
    # till only one digit is left
    while n >= 10:
        n = n / 10
     
    # return the first digit
    return int(n)

   
N = int(input())
#A = map(int, input().split())
A=list(map(int,input().strip().split()))[:N]
out_ = solve(A)
print(out_)