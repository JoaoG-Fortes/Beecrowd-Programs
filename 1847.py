a, b, c = list(map(int, input().split()))

if (a > b):

    if (b <= c):
        print(':)')

    elif (b > c):
        if ((a-b) > (b-c)):
            print(':)')
        elif ((a-b) <= (b-c)):
            print(':(')


if (a < b):

    if (b >= c):
        print(':(')

    elif (b < c):
        if ((a - b) > (b - c)):
            print(':(')
        elif ((a - b) <= (b - c)):
            print(':)')


if (a == b):

    if (b < c):
        print(':)')
    elif (b > c):
        print(':(')
