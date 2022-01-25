""" 
1 2 3 4 5
  2 3 4 5
    3 4 5
      4 5
        5
"""

print("Enter how long you want it to continue-")
n=int(input())
#n=5
for i in range(1, n+1):
    for j in range(i-1):
        print(" ", end=" ")
    for k in range(i, n+1):
        print(k, end=" ")
    print()