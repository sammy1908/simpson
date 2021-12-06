import sympy as sp
import numpy as np

x = sp.var('x')  

def simpson_method(f,a,b,n):
    h = (b-a)/n

    f = sp.sympify(f)
    r = np.arange(a,b,h)
    intervalo = 0
    middle = []

    for i in range(1,len(r)):
        if intervalo == 0:
            print(f'{r[i]} -> 4*{f.subs(x,r[i])}')
            middle.append(4*f.subs(x,r[i]))
            intervalo = 1
        else:
            print(f'{r[i]} -> 2*{f.subs(x,r[i])}')
            middle.append(2*f.subs(x,r[i]))
            intervalo = 0
    simpson = (h/3)*(f.subs(x,a) + f.subs(x,b) + sum(middle))
    return round(simpson,3)
