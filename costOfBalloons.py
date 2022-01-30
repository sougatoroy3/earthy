'''tests=int(input())

nOfGreenBallons=0
nOfPurpleBallons=0
j=1
tg=0
tp=0
while j<=tests:
    n=int(input())
    costOfGreenBalloons, costOfPurpleBalloons=[int(x) for x in input().split()]
    for i in range(0, n+1):
        prob1, prob2=[int(x) for x in input().split()]
        if prob1==1:
            if prob2==1:
                nOfGreenBallons+=1
                nOfPurpleBallons+=1
            else:
                nOfGreenBallons+=1
        elif prob2==1:
            if prob1==1:
                nOfGreenBallons+=1
                nOfPurpleBallons+=1
            else:
                nOfPurpleBallons+=1
    totalCostOfGreenBalloons=nOfGreenBallons*costOfGreenBalloons
    tg+=totalCostOfGreenBalloons
    totalCostOfPurpleBalloons=nOfPurpleBallons*costOfPurpleBalloons
    tp+=totalCostOfPurpleBalloons
    sumCost=tg+tp
    print(sumCost)
    
'''

testCase= int(input())

for i in range(0, testCase):
    cpGB, cpPB = [int(x) for x in input().split()]
    if i%2==0:
        cpGB, cpPB = cpGB, cpPB
    else:
        cpGB, cpPB = cpPB, cpGB
    n= int(input())
    cost=0
    for j in range(0, n):
        val1, val2= [int(x) for x in input().split()]
        cost+= (val1*cpGB)
        cost+= (val2*cpPB)
    print(cost)