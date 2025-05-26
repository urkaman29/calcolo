import numpy as np
from sympy.calculus.util import continuous_domain
import matplotlib.pyplot as plt
import sympy as sp
import time
import cv2
import glob

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

# Punto iniziale: per comodità, si parte da (x0, 0) sull'asse x
plt.plot(x0, 0, 'bo')  # punto iniziale
plt.savefig("img/grafico" + str(0) + ".png")

# Primo step: linea verticale da (x0, 0) a (x0, f(x0))
plt.plot([x0, x0], [0, f(x0)], 'r-')
plt.savefig("img/grafico" + str(1) + ".png")


# Imposto il punto corrente come x0
current = x0

epsilon = 1*(10**(-16))

for i in range(2, 60, 2):

    if(abs(d(fisso[2])) >= 1 or abs(d(fisso[2])) <= 0):
        print("funzione non valida per l'iterazione")
        break

    # Calcolo f(x0)
    y = f(current)
    if abs(y-current) <= epsilon:
        break


    # Passo orizzontale: da (current, y) a (y, y)
    plt.title("Iterazione n: " + str(i))
    plt.plot([current, y], [y, y], 'r-')
    plt.savefig("img/grafico" + str(i) + ".png")

    time.sleep(0.2)

    # Passo verticale: da (y, y) a (y, f(y))
    plt.title("Iterazione n: " + str(i+1))
    plt.plot([y, y], [y, f(y)], 'r-')
    plt.savefig("img/grafico" + str(i+1) + ".png")

    # Aggiorno il punto corrente
    current = y

plt.xlabel("x")
plt.ylabel("y")
plt.title("Iterazione del Punto Fisso")
plt.legend()
plt.grid(True)


# Salvataggio grafico iniziale e video
plt.savefig("grafico.png")
   # Recupero in ordine tutti i file delle immagini generate
immagini = sorted(glob.glob("img/grafico*.png"), key=lambda x: int(x.split("grafico")[-1].split(".png")[0]))

   # Leggo la prima immagine per ottenere le dimensioni del video
frame_iniziale = cv2.imread(immagini[0])
altezza, larghezza, _ = frame_iniziale.shape
dimensione = (larghezza, altezza)

   # Impostazioni video e definizione codec
video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'mp4v'), 1, dimensione)

   # Scrive ogni immagine nel video
for img in immagini:
    frame = cv2.imread(img)
    video.write(frame)

video.release()
#20/(x**2+2*x+10)
#(20-10*x)/(x**2+2*x)
