"""
A A A
B B B
C C C
"""

print("Enter how long you want it to continue-")
n=int(input())

char=65
for i in range(0, n):
    for j in range(0, n):
        print(chr(char), end=" ")
    print()
    char+=1