import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import os

# Definisco la funzione
x = sp.symbols('x')
funzione = input("Inserisci la funzione: ")
f_sym = sp.sympify(funzione)
f = sp.lambdify(x, f_sym, 'numpy')

# Intervallo e costante L
a = float(input("Inserisci a dell'intervallo: "))
b = float(input("Inserisci b dell'intervallo: "))
L = float(input("Inserisci L: "))
k_max = int(input("Definisci numero di iterazioni massime: "))

# Inizializzazione dei punti
X = [a, b]
Y = [f(a), f(b)]

# Crea cartella per le immagini
if not os.path.exists("iterazioni_piyavski"):
    os.makedirs("iterazioni_piyavski")

# Crea figura e asse (il grafico rimarrà aperto e verrà aggiornato)
x_vals = np.linspace(a, b, 500)
fig, ax = plt.subplots()

# Plot iniziale della funzione e dei punti iniziali
ax.plot(x_vals, f(x_vals), 'k-', label='f(x)')
ax.scatter(X, Y, color='red', zorder=5, label='Punti valutati')
ax.set_title("Iterazione 0")
ax.legend()
fig.savefig("iterazioni_piyavski/iterazione_0.png")

# Iterazioni: il grafico viene aggiornato cumulativamente
for k in range(1, k_max + 1):
    # Ordino i punti
    idx_sort = np.argsort(X)
    X, Y = np.array(X)[idx_sort], np.array(Y)[idx_sort]
    
    # Calcolo le caratteristiche Ri per ogni sottointervallo
    R = (Y[:-1] + Y[1:]) / 2 - L * (X[1:] - X[:-1]) / 2
    
    # Seleziono il sottointervallo con la minima caratteristica
    t_idx = np.argmin(R)
    t = (X[t_idx] + X[t_idx+1]) / 2 - (Y[t_idx+1] - Y[t_idx]) / (2 * L)

    # Criterio d'arresto: se il sottointervallo è troppo piccolo
    if np.abs(X[t_idx+1] - X[t_idx]) < 1e-5:
        break
    
    # Aggiungo il nuovo punto
    X = np.append(X, t)
    Y = np.append(Y, f(t))
    
    # Traccio le due linee di minorante sul sottointervallo [X[t_idx], X[t_idx+1]]
    # Linea con pendenza -L a partire da X[t_idx]
    x_left = np.linspace(X[t_idx], t, 50)
    y_left = Y[t_idx] - L * (x_left - X[t_idx])
    ax.plot(x_left, y_left, 'b--', label='Minorante -L' if k==1 else "")
    
    # Linea con pendenza +L a partire da X[t_idx+1]
    x_right = np.linspace(t, X[t_idx+1], 50)
    y_right = Y[t_idx+1] + L * (x_right - X[t_idx+1])
    ax.plot(x_right, y_right, 'b--', label='Minorante +L' if k==1 else "")
    
    # Traccio il nuovo punto candidato
    ax.scatter([t], [f(t)], color='orange', zorder=2, label='Nuovo punto' if k==1 else "")
    
    # Aggiorno il titolo e la legenda
    ax.set_title(f"Iterazione {k}")
    ax.legend()
    
    # Salvo l'immagine dell'iterazione corrente senza cancellare le tracce precedenti
    fig.savefig(f"iterazioni_piyavski/iterazione_{k}.png")

# Grafico finale: evidenzia il minimo trovato
x_min = X[np.argmin(Y)]
ax.scatter([x_min], [f(x_min)], color='green', s=100, zorder=5, label=f'Minimo trovato: x={x_min:.4f}')
ax.set_title("Algoritmo di Piyavski-Shubert - Risultato finale")
ax.legend()
fig.savefig("iterazioni_piyavski/risultato_finale.png")
plt.show()

print(f"Minimo trovato in x = {x_min}, f(x) = {f(x_min)}")
