# Escribir la siguiente expresión en forma de expresión algorítmica
# a3*(b2-2ac)/2b
# pedimos e valores a,b,c
# Mostramos resultado final

a = float(input("ingrese valor de a: "))
b = float(input("ingrese valor de b: "))
c = float(input("ingrese valor de c: "))
resultado = (a ** 3 * (b ** 2 - 2 * a *c))/(2*b)
print(f'el resultado es: {resultado}')