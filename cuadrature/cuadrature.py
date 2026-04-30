#Importación de Bibliotecas
import numpy as np
import matplotlib.pyplot as plt

#Gauss
def gaussxw(N):
    """
    Calcula los puntos de muestreo y pesos de la Cuadratura de Gauss-Legendre
    en el intervalo [-1, 1].

    Parámetros
    ----------
    N (int):
        Número de puntos de integración.

    Retorna
    -------
    x (numpy.ndarray):
        Arreglo con los puntos de muestreo para la integración en [-1, 1].
    w (numpy.ndarray):
        Arreglo con los pesos asociados a cada punto de muestreo.

    Notas
    -----
    Los puntos de muestreo corresponden a las raíces del polinomio de Legendre
    de grado N, y los pesos están definidos para maximizar la
    precisión del método.

    Ejemplos
    --------
        >>> valores = gaussxw(3)
        >>> len(valores[0])
        3
    """
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w

#Escalado de Intervalo
def gaussxwab(a, b, x, w):
    """
    Escala los puntos de muestreo y pesos de la Cuadratura Gaussiana desde
    el intervalo [-1, 1] a un intervalo arbitrario [a, b].

    Parámetros
    ----------
    a (float): 
        Límite inferior del intervalo.
    b (float): 
        Límite superior del intervalo.
    x (numpy.ndarray): 
        Puntos de muestreo en el intervalo [-1, 1].
    w (numpy.ndarray): 
        Pesos en el intervalo [-1, 1].

    Retorna
    -------
    xp (numpy.ndarray):
        Puntos de muestreo transformados al intervalo [a, b].
    wp (numpy.ndarray):
        Pesos ajustados al intervalo [a, b].

    Notas
    -----
    La transformación utilizada es:

    x' = (b - a)/2 * x + (b + a)/2

    w' = (b - a)/2 * w

    Ejemplos
    --------
        >>> import numpy as np
        >>> x = np.array([-0.5, 0.5])
        >>> w = np.array([1.0, 1.0])
        >>> escalado = gaussxwab(0, np.pi, x, w)
        >>> escalado[0]
        (2,)
    """
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

#Función Integrando
def func(varInt):
    """
    Función integrando del problema.

    Parámetros
    ----------
    varInt (float):
        Variable de integración.

    Retorna
    -------
    float:
        Valor de la función evaluada en varInt.

    Notas
    -----
    La función corresponde a:

    f(x) = sin(x^2)

    Esta función no tiene una solución analítica, por lo que se requiere un método numérico para
    evaluar su integral.

    Ejemplos
    --------
        >>> import numpy as np
        >>> func(np.pi)
        np.sin(np.pi**2)
    """
    return np.sin(varInt**2)

if __name__ == "__main__":
    #Declaración de Variables
    a = 0.0
    b = np.pi
    nite = np.arange(1,15)
    varIntegral = []

    #Ciclo para evaluar todos los valores
    for n in nite:
        valores = gaussxw(n)
        escalado = gaussxwab(a,b,valores[0],valores[1])
        I = np.sum(func(escalado[0]) * escalado[1])
        varIntegral.append(I)
        print(f"En la iteración n = {n:2d} el valor de la Integral es I = {I:.10f}")

    #Gráfico
    plt.figure()
    plt.plot(nite,varIntegral,'o-')
    plt.xlabel("n")
    plt.ylabel("I(n)")
    plt.title("Cuadratura Gaussiana para $\int_0^\pi \sin(x^2)\,dx$")
    plt.grid()
    plt.show()