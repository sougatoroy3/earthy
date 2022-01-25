"""
A
B B
C C C
"""
print("Enter how long you want it to continue-")
n=int(input())

ch=65

for i in range(1, n+1):
    for j in range(1, i+1):
        print(chr(ch), end=" ")
    print()
    ch+=1