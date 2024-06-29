# TIPOS DE DATOS EN PYTHON
* Numericos
  -Integer

      a = 3
  -Complex Number

      c = 2 + 3j
  -Float

      b = 3.5
* Dictionary
    
      d= {"key1": "value1", "key2": "value2"}

* Boolean
  
      e = True
      e = False
* Set
  
      f = {1, 2, 3, "cuatro", 5.0}

* SequenceType
  -String

      g = "Hola mundo"

  -List

      h = [1, 2, 3, "cuatro", 5.0]

  -Tuple

      i = (1, 2, 3, "cuatro", 5.0)

  Ejemplos [Ver Main linea 20](/Clases/main.py)

## MANEJO DE STRINGS
Se realiza con el operador  **+** 
### Concatenaciones
- Concatenación de cadenas
- Concatenación variable + cadena
- Concatenación variables
Ejercicio mi grupo favorito [Ver Main linea 42](/Clases/main.py)


### Transformación de String a Int
    numero1 = "2"
    numero2 = "6"
    print(int(numero1) + int(numero2))
[Ver Main linea 50](/Clases/main.py)

## BOOLEANOS
Nos permite saber si o no, 1 - 0, verdadero - falso
No pueden cumplirse ambas, o es verdadero o es falso, existe o no existe
      
      soyBooleano = 7 > 2
      print(soyBooleano)
      if soyBooleano:
      print("El resultado es verdadero")
      else: print("El resultado es falso")


[Ver Main linea 55](/Clases/leccion1/main.py)


## INPUTS - Entradas de usuario

  -Funcion input: pedimos al usuario que ingrese un valor y procesamos el resultado
  -Regresa un dato de tipo *string*

      resultado = input()
      print(resultado)
[Ver Main linea 62](/Clases/leccion1/main.py)  

### Conversión de entrada de datos
    numero1 = input("Escribe el primer numero ")
    numero2 = input("Escribe el segundo numero ")
    resultado = int(numero1) + int(numero2)
    print("El resultado de la suma es", resultado)

[Ver Main linea 66](/Clases/leccion1/main.py) 

##### Ejercicios
###### [1 "Como estuvo tu dia"](/Ejercicios/ejercicio1.py) 
###### [2 Libro](/Ejercicios/ejercicio2.py) 