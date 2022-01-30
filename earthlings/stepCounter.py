n=int(input())
a=list(map(int,input().strip().split()))[:n]
b=list(map(int,input().strip().split()))[:n]

#print(a, b)

count=0
minVal=min(a)
for i in range(0, n):
    while a[i]>minVal:
        a[i]=a[i]-b[i]
        count+=1
    if a[i]<minVal:
        minVal=a[i]
        i=0
    elif a[i]<0:
        count=-1
        break
    else:
        i+=1
            
print(count)            
'''
Problem

You are given two arrays
and . In each step, you can set  if . Determine the minimum number of steps that are required to make all

's equal.

Input format

    First line: 

 
Second line:
Third line:

Output format

Print the minimum number of steps that are required to make all

's equal. If it is not possible, then print -1.

Constraints

Sample input

2
5 6
4 3

Sample output

-1
Sample Input

5
5 7 10 5 15
2 2 1 3 5

Sample Output

8

Time Limit: 1
Memory Limit: 256
Source Limit: 
'''