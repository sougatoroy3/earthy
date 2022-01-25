""" 
* * * *
* * *
* *
*
"""

ch='*'

print("Enter how long you want it to continue-")
n=int(input())

for i in range(n+1, 1, -1):
    for j in range(1, i):
        print(ch, end=" ")
    print()