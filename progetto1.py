import numpy as np
from sympy.calculus.util import continuous_domain
import matplotlib.pyplot as plt
import sympy as sp



# Definisco la funzione
x = sp.symbols('x')
funzione = str(input("Inserisci la funzione: "))
f_sym = sp.sympify(funzione)
f = sp.lambdify(x, f_sym, 'numpy')

# Definisco intervallo funzione
intervallo= []
intervallo[0]= int(input("Inserisci a dell'intervallo: "))
intervallo[1]= int(input("Inserisci b dell'intervallo: "))

# Definisco punto di inizio x0
x0= int(input("Inserisci x0: "))

# Calcolo derivata
derivata = sp.diff(f_sym, x)
d = sp.lambdify(x, derivata, 'numpy')

# Calcolo punto fisso f(x) = x
int_func= f_sym - x
intersezione= sp.solve(int_func, x) #lista con x dei punti di intersezione tra f(x) ed y=x.

# Funzione per iterazione
def iterazione(x0, f_sym):
    tuple_punti= []
    for i in range(120):
        if(i == 0):
            tuple_punti.append([x0, f(x0)])
    return 0