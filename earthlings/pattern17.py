"""
      *
    * *
  * * * 
* * * *
"""

ch='*'

print("Enter how long you want it to continue-")
n=int(input())

for i in range(1,n+1):
    for j in range(1, n-i+1):
        print(" ", end="")
    for k in range(i):
        print(ch, end="")
    print()
