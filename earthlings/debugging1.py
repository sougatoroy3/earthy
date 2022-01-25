'''
nRows=4
for i in range(nRows, 0,-1):
    print('*'*i)'''

year=int(input())
if (year%400==0 or year%100!=0) and year%4==0:
    print("Leap")
else:
    print("not")