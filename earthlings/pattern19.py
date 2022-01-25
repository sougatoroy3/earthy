""" 
* * * *
  * * *
    * *
      *
"""

ch='*'

print("Enter how long you want it to continue-")
n=int(input())

for i in range(0, n):
    for j in range(i):
        print(" ", end=" ")
    for k in range(i, n):
        print(ch, end=" ")
    print()

'''

rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    # process each column
    for j in range(0, k):
        # print space in pyramid
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        # display star
        print("$ ", end="")
    print("")

    '''