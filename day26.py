'''rd, rm, ry = [int(x) for x in input().split(' ')]
ed, em, ey = [int(y) for y in input().split(' ')]

if ry > ey:
    print(10000)
elif (ry == ey) & (rm > em):
    print(500 * (rm - em))
elif (ry == ey) & (rm == em) & (rd > ed):
    print(15 * (rd - ed))
else:
    print(0)'''
n = input()
x = list(map(int, n.split()))
m = input()
y = list(map(int, m.split()))
z=0
if y[2] < x[2]:
    z = 10000
elif y[2] == x[2]:
    if y[1] < x[1]:
        z = 500*(x[1]-y[1])
    elif y[0] < x[0]:
        z = 15*(x[0]-y[0])
print(z)