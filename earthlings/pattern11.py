"""
A B C
D E F
G H I
"""
print("Enter how long you want it to continue-")
n=int(input())

ch=65

for i in range(0, n):
    for j in range(0,n):
        print(chr(ch), end=" ")
        ch+=1
    print()