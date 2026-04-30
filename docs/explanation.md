# Explicación de Método de Cuadratura Gaussiana por Polinomios de Legendre

La Cuadratura Gaussiana por Polinomios de Legendre resulta ser uno de los métodos numéricos más relevantes para el cálculo de integrales, consiste en representar la integral como la sumatoria del muestreo de los valores de los puntos de muestreo equidistantes y los pesos asociados a cada punto.

$$
\int_{-1}^{1} f(x)dx \approx \sum_{i = 1}^{n} w_i f(x_i)
$$

* $x_i$: puntos de muestreo.
* $w_i$: pesos.

## Cambio de Intervalo

La definición determina el dominio en \([-1, 1]\) cuando se trabaja con los Polinomios de Legendre, por lo tanto, se debe realizar escalado para que funcione con el nuevo intervalo deseado \([a, b]\).

$$
x' = \frac{b - a}{2} * x + \frac{b + a}{2},
w' = \frac{b - a}{2} * w
$$

Con estos cambios ya se puede resolver la integral mediante Cuadratura Gaussiana por Polinomios de Legendre.