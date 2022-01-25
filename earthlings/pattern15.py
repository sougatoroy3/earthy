"""
A
B C
C D E
D E F G
"""
print("Enter how long you want it to continue-")
n=int(input())

ch=64
for i in range(1, n+1): 
    ch=64
    ch+=i   
    for j in range(1, i+1):     
        print(chr(ch), end=" ") 
        ch+=1      
    print()
    
