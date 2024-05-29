# 1. Examen VCS con Git y GitHub
## 1.1 Introducción
Este pequeño proyecto es para realizar la recuperación VCS con Git y GitHub.

# 2. Composición del proyecto
El proyecto se compone de un archivo main.py que instancia un objeto de la clase Frase para realizar varias operaciones con una cadena de caracteres mediante varios métodos.

## 2.1 La clase Frase
Se encuentra ubicada en el directorio clases y su estructura es la siguiente:

Propiedades:

- frase      -> Una cadena de caracteres

Métodos:

- mayuscula -> Devuelve la cadena en letras mayúsculas.
- minuscula -> Devuelve la cadena en letras minúsculas.

# 3. Cambios a realizar en los archivos fuente durante el examen

## Ejercicio 2a


------------------------------------
~~~
def longitud(self) -> int:
    return self.__frase.length
~~~
------------------------------------

## Ejercicio 5a

---------------------------------------------------------------
~~~
def longitud(self) -> int:
    return self.__frase.count(' ') + 1
~~~
-----------------------------------------------------------------------

## Ejercicio 7b

------------------------------------
~~~
def buscar(self, subcadena: str) -> bool:
    return self.__frase.find(subcadena) > -1
~~~
------------------------------------

## Ejercicio 7f

------------------------------------
~~~
def buscar(self, subcadena: str) -> bool:
    try:
        return self.__frase.index(subcadena) >= 0
    except:
        return False
~~~
------------------------------------

## Ejercicio 8c

------------------------------------
Atento al número de clase (NC) en el nombre del método

~~~
class nombreNC:
  def __init__(self, f: str):
    self.__frase = f;
~~~
------------------------------------

## Ejercicio 9a

------------------------------------
~~~
def __str__(self) -> str:
    return self.frase.__str__()
~~~
------------------------------------

## Ejercicio 10a

------------------------------------
~~~
def __rep__(self) -> str:
    return self.frase.__rep__()
~~~
------------------------------------
