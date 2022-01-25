"""
1
2 2
3 3 3
"""
print("Enter how long you want it to continue-")
n=int(input())

i=1

for i in range(1, n+1):
    for j in range(1, i+1):
        print(i, end=" ")
    print()