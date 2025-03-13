import numpy as np
from sympy.calculus.util import continuous_domain
import matplotlib.pyplot as plt
import sympy as sp

# Definisco la funzione
x = sp.symbols('x')
funzione = input("Inserisci la funzione: ")
f_sym = sp.sympify(funzione)
f = sp.lambdify(x, f_sym, 'numpy')

# Definisco la bisettrice (y=x)
bisettrice = sp.sympify("x")

# Definisco intervallo funzione
intervallo = []
intervallo.append(float(input("Inserisci a dell'intervallo: ")))
intervallo.append(float(input("Inserisci b dell'intervallo: ")))

# Definisco punto di inizio x0
x0 = float(input("Inserisci x0: "))

# Calcolo derivata
derivata = sp.diff(f_sym, x)
d = sp.lambdify(x, derivata, 'numpy')

# Calcolo punto fisso f(x) = x (lista di punti fissi)
int_func = f_sym - x
fisso = sp.solve(int_func, x)
print(fisso)

# Funzione per intersecare (non essenziale per il cobweb, ma mantenuta)
def interseca(f1, f2):
    funz = f1 - f2
    intersezione = sp.solve(funz, x)
    return intersezione[0]

# Preparazione del grafico: funzione e bisettrice
x_vals = np.linspace(intervallo[0], intervallo[1], 400)
plt.figure(figsize=(8, 6))
plt.plot(x_vals, f(x_vals), label='f(x)')
plt.plot(x_vals, x_vals, 'k--', label='y = x')

# Disegno il cobweb direttamente

# Punto iniziale: per comodità, si parte da (x0, 0) sull'asse x
plt.plot(x0, 0, 'bo')  # punto iniziale

# Primo step: linea verticale da (x0, 0) a (x0, f(x0))
plt.plot([x0, x0], [0, f(x0)], 'r-')

# Imposto il punto corrente come x0
current = x0

epsilon = 1*(10**(-16))

for i in range(1000):
    print(i)
    # Calcolo f(x0)
    y = f(current)
    if abs(y-current) <= epsilon:
        break


    # Passo orizzontale: da (current, y) a (y, y)
    plt.plot([current, y], [y, y], 'r-')
    # Passo verticale: da (y, y) a (y, f(y))
    plt.plot([y, y], [y, f(y)], 'r-')
    # Aggiorno il punto corrente
    current = y

plt.xlabel("x")
plt.ylabel("y")
plt.title("Iterazione del Punto Fisso")
plt.legend()
plt.grid(True)
plt.savefig("grafico.png")

#20/(x**2+2*x+10)
