from math import *

t = int(input('Input type(1 - ellipse, 2 - hyperbola, 3 - parabola):\n'))

if t == 1:
    x1, y1 = [float(e) for e in input('Input coordinates of 2 points:\n').split()]
    x2, y2 = [float(e) for e in input().split()]
    try:
        b = sqrt((x1*x1*y2*y2-x2*x2*y1*y1)/(x1*x1-x2*x2))
        a = sqrt(b*b*x1*x1/(b*b-y1*y1))
    except Exception:
        print('Incorrect points.')
    else:
        print(f'a={a:.2f}, b={b:.2f}')
elif t == 2:
    x1, y1 = [float(e) for e in input('Input coordinates of 2 points:\n').split()]
    x2, y2 = [float(e) for e in input().split()]
    try:
        b = sqrt((x1*x1*y2*y2-x2*x2*y1*y1)/(x1*x1+x2*x2))
        a = sqrt(b*b*x1*x1/(b*b+y1*y1))
    except Exception:
        print('Incorrect points.')
    else:
        print(f'a={a:.2f}, b={b:.2f}')
elif t == 3:
    x1, y1 = [float(e) for e in input('Input coordinates of 1 point:\n').split()]
    try:
        p = y1*y1/(2*x1)
    except Exception:
        print('Incorrect points.')
    else:
        print(f'p={p:.2f}')
else:
    raise ValueError('Wrong type.')
