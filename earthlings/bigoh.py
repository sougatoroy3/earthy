def fact2(n):
    if n == 0:
        return 1
    else:
        print(n)
        return n * fact2(n-1)

print (fact2(5))