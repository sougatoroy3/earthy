"""
A B C
B C D
C D E
"""
print("Enter how long you want it to continue-")
n=int(input())

ch=65

for i in range(1, n+1):
    for j in range(1,n+1):
        print(chr(ch), end=" ")
        ch+=1
    print()
    ch-=2