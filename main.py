import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def graficar_area(f_num, a, b, x_vals, titulo, xlabel='x', ylabel='y'):
    """Funcion auxiliar para graficar la curva y sombrear el area"""
    y_vals = f_num(x_vals)
    plt.plot(x_vals, y_vals, 'b-', linewidth=2)
    
    # Rellenar el area bajo la curva entre a y b
    x_fill = np.linspace(a, b, 100)
    y_fill = f_num(x_fill)
    plt.fill_between(x_fill, y_fill, alpha=0.3, color='red')
    
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

def ejercicio_3():
    # Integral de (x^3 + 2x) de -1 a 1
    print("\nejercicio_3() => Ejercicio 3: Propiedades de la integral")
    x = sp.Symbol('x')
    f = x**3 + 2*x
    resultado = sp.integrate(f, (x, -1, 1))
    print(f"ejercicio_3() => Funcion: {f}")
    print(f"ejercicio_3() => Resultado de la integral en [-1, 1]: {resultado}")
    
    f_num = sp.lambdify(x, f, 'numpy')
    x_vals = np.linspace(-1.5, 1.5, 100)
    graficar_area(f_num, -1, 1, x_vals, "Ejercicio 3: y = x^3 + 2x")

def ejercicio_4():
    # Integral de sin(x)cos(x) de 0 a pi/2
    print("\nejercicio_4() => Ejercicio 4: Integral trigonometrica")
    x = sp.Symbol('x')
    f = sp.sin(x) * sp.cos(x)
    resultado = sp.integrate(f, (x, 0, sp.pi/2))
    print(f"ejercicio_4() => Funcion: {f}")
    print(f"ejercicio_4() => Resultado de la integral en [0, pi/2]: {resultado}")
    
    f_num = sp.lambdify(x, f, 'numpy')
    x_vals = np.linspace(0, float(sp.pi), 100)
    graficar_area(f_num, 0, float(sp.pi/2), x_vals, "Ejercicio 4: y = sin(x)cos(x)")

def ejercicio_5():
    # Integral de 3t^2 - 2t + 4 de 1 a 4
    print("\nejercicio_5() => Ejercicio 5: Aplicaci´on en fisica")
    t = sp.Symbol('t')
    v = 3*t**2 - 2*t + 4
    distancia = sp.integrate(v, (t, 1, 4))
    print(f"ejercicio_5() => Funcion de velocidad v(t): {v}")
    print(f"ejercicio_5() => Distancia total recorrida de t=1 a t=4: {distancia} metros")
    
    v_num = sp.lambdify(t, v, 'numpy')
    t_vals = np.linspace(0, 5, 100)
    graficar_area(v_num, 1, 4, t_vals, "Ejercicio 5: Velocidad v(t) = 3t^2 - 2t + 4", xlabel='Tiempo (t)', ylabel='Velocidad (v)')

def ejercicio_8():
    # Integral de e^(-x) de 0 a 1
    print("\nejercicio_8() => Ejercicio 8: Integral exponencial")
    x = sp.Symbol('x')
    f = sp.exp(-x)
    resultado = sp.integrate(f, (x, 0, 1))
    print(f"ejercicio_8() => Funcion: {f}")
    print(f"ejercicio_8() => Resultado exacto: {resultado}")
    print(f"ejercicio_8() => Resultado numérico aproximado: {resultado.evalf(5)}")
    
    f_num = sp.lambdify(x, f, 'numpy')
    x_vals = np.linspace(-0.5, 2, 100)
    graficar_area(f_num, 0, 1, x_vals, "Ejercicio 8: y = e^(-x)")

def ejercicio_9():
    # Integral de 1/x de 1 a e
    print("\nejercicio_9() => Ejercicio 9: Integral logaritmica")
    x = sp.Symbol('x')
    f = 1/x
    resultado = sp.integrate(f, (x, 1, sp.E))
    print(f"ejercicio_9() => Funcion: {f}")
    print(f"ejercicio_9() => Resultado de la integral en [1, e]: {resultado}")
    
    f_num = sp.lambdify(x, f, 'numpy')
    x_vals = np.linspace(0.1, 4, 100)
    graficar_area(f_num, 1, float(sp.E), x_vals, "Ejercicio 9: y = 1/x")

if __name__ == "__main__":
    print("main() => Iniciando\n")
    ejercicio_3()
    ejercicio_4()
    ejercicio_5()
    ejercicio_8()
    ejercicio_9()
    print("\nmain() => Completado")