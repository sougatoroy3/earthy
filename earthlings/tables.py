for multiple in range(1, 4):
    for num in range(1, 6):
        print('{0: >2}'.format(num),'*', \
            '{0: >3}'.format(multiple),'=', \
            '{0: >3}'.format(num*multiple),'\t', end= '')
    print()