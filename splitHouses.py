n=int(input())
data=input()

if 'HH' in data:
    print('NO')
else:
    print('YES')
    newData=data.replace('.', 'B')
    print(newData)