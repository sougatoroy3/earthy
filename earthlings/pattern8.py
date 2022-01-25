"""
1
2 1
3 2 1
4 3 2 1
"""

print("Enter how long you want it to continue-")
n=int(input())
'''
for i in range(1, n):
    ct=i
    for j in range(1, i+1):
        print(ct, end=" ")
        ct-=1
    print()

'''
for i in range(1, n):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print("")
    