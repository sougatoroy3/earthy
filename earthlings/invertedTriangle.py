nRows=int(input())
nSpaces=0
nStars=2*nRows-1
for i in range(1, nRows+1):
    print(' ' * nSpaces+ '*' * nStars)
    nStars-=2
    nSpaces+=1