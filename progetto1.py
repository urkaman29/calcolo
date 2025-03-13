import numpy as np
from sympy.calculus.util import continuous_domain
import matplotlib.pyplot as plt
import sympy as sp



# Definisco la funzione
x = sp.symbols('x')
funzione = str(input("Inserisci la funzione: "))
f_sym = sp.sympify(funzione)
f = sp.lambdify(x, f_sym, 'numpy')

# Definisco la bisettrice
bisettrice= sp.sympify("x")

# Definisco intervallo funzione
intervallo= []
intervallo.append(int(input("Inserisci a dell'intervallo: ")))
intervallo.append(int(input("Inserisci b dell'intervallo: ")))

# Definisco punto di inizio x0
x0= int(input("Inserisci x0: "))

# Calcolo derivata
derivata = sp.diff(f_sym, x)
d = sp.lambdify(x, derivata, 'numpy')

# Calcolo punto fisso f(x) = x
int_func= f_sym - x
intersezione= sp.solve(int_func, x) #lista con x dei punti di intersezione tra f(x) ed y=x.

# Funzione per intersecare 
def interseca(f1, f2):
    funz= f1 - f2
    intersezione= sp.solve(funz, x)
    return intersezione[0]

# Funzione per iterazione
tuple_punti= []
for i in range(120):
    if(i == 0):
        tuple_punti.append([x0, f(x0)])
    else:
        if(i%2 == 1):  #orizzontale
            x1 = interseca(interseca(tuple_punti[i-1][1], bisettrice)) 
            tuple_punti.append([tuple_punti[i-1][1], x1])
        if(i%2 == 0):  #verticale
            tuple_punti.append([tuple_punti[i-1][1], f(x1)])

#20/(x**2+2*x+10)
