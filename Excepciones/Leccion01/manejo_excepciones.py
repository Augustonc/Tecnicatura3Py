from NumerosIgualesException import NumerosIgualesException

# Podemos utilizar también la clase hija
#  "ZeroDivisionError" pero se usa para una excepción más específica
# Exception es más genérico

resultado = None
# 'None' Indica que la variable no tiene nada
# Esta variable está fuera del 'try' lo que
#    significa que es global, funciona fuera y dentro de este

# a = '10' <-- Esto dará TypeError
# b = 0

# a = 7
# b = 5 #<--- Esto no dará ningún tipo de error
#  por que efectivamente son numero que se pueden dividir

try:
    a = int(input('Por favor ingrese el primer dígito de la división: '))
    b = int(input('Por favor ingrese el segundo dígito de la división: '))
    # Podemos poner las variables dentro del bloque
    #  del 'try' pero serán exclusivas de este bloque
    # 10/0
    if a == b:
        raise NumerosIgualesException('Son número iguales') # Creamos nuestra propia Exception
    resultado = a / b  # modificamos
except TypeError as e:
    print(f'Type Error - Ocurrió un error: {type(e)}')
except ZeroDivisionError as e:  # La letra 'e' es una variable,
                                #  por lo que podemos usar cualquier nombre
    print(f'ZeroDivisionError - Ocurrió un erro: {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrió un error: {type(e)}')
    # Las aclaraciones en el string y el 'type'
    #  lo ponemos para saber que tipo de excepción es
    # La clase 'Exception' siempre debe ir al final
    #  ya que primero intentará definir el error especifico
    #  con las clases hijas y si no lo encuentra recurrirá a la
    #  clase madre de todas ---> 'Exception'
else:
    print('No se arrojó ninguna excepcion')
# La función else es opcional para cuando no se prowduce ninguna excepcion.
finally:
    print('El Bloque finally siempre se ejecutrá')

print(f'El resultado es: {resultado}')
print('seguimos...')
