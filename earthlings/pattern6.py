"""
1
2 3
4 5 6 
7 8 9 10
"""

print("Enter how long you want it to continue-")
n=int(input())
ct=1
for i in range(0, n):
    for j in range(0,i+1):
        print(ct, end=" ")
        ct+=1
    print()
    