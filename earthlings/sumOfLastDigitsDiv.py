'''Problem

You are provided an array A of size N that contains non-negative integers. 
Your task is to determine whether the number that is formed by selecting the
last digit of all the N numbers is divisible by 10.

.

Note: View the sample explanation section for more clarification.

Input format

    First line: A single integer 

 N denoting the size of array 
Second line: 

     space-separated integers.

Output format

If the number is divisible by
, then print . Otherwise, print .
'''

N=int(input())
A=list(map(int,input().strip().split()))[:N]

'''for i in range(0, N):
    elements=int(input())
    A.append(elements)
'''

nos=''
for i in A:
    el2=str(i%10)
    nos=''.join(el2)

sum=int(nos)
if sum%10==0:
    print('Yes')
else:
    print('No')