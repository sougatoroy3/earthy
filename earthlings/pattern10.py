"""
A A A
A B C
A B C
"""
print("Enter how long you want it to continue-")
n=int(input())

for i in range(0, n):
    ch=65
    for j in range(0,n):
        print(chr(ch), end=" ")
        ch+=1
    print()