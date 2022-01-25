"""
1
2 3
3 4 5
4 5 6 7
"""

print("Enter how long you want it to continue-")
n=int(input())
#ct=1
for i in range(0, n):
    ct=i+1
    for j in range(0, i+1):
        print(ct, end=" ")
        ct+=1
    print()
    #ct-=1