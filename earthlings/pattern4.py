"""
*
* *
* * * 
* * * *
"""

print("Enter how long you want it to continue-")
n=int(input())

c='*'
print("We'll print", c)
'''for i in range(1, n+1):
    for j in range(1, i+1):
        print(c, end=" ")
    print()
    '''
for i in range(1,n+1):
    print('* ' * i)