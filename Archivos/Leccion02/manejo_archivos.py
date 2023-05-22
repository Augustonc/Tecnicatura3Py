try: # intenta lo siguiente, si va bien, se queda ahí, si va mal, sigue con except
     # Declaramos una variable
    archivo = open('prueba.txt','w',encoding = 'utf8') # w viene de write
    # al crear la variable con este metodo se crea el archivo, si el archivo existe, no hace nada

    # Modificamos el archivo que ya creamos
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt\n')
    archivo.write('Los acentos son importantes para la palabras\n')
    archivo.write('como por ejemplo: acción, ejecución y producción\n')
    archivo.write('-----------------------------\n')
    archivo.write('Los parámetros del método open son {\n\tr: Read\n\ta: Append\n\tw: Write\n\tx: Excepción, en caso de que no exista el archivo\n\tt: texto\n\tb: archivos binarios\n\tw+: Lee y escribe\n\tr+: Escribir y leer\n\tencoding = "utf8": Juego de caracteres UTF-8 para no tener problemas con acentos\n\t}')
    archivo.write('\nCon esto terminamos')
except Exception as e:
    print(e)
finally: # siempre se ejecuta
    archivo.close() # Con esto se debe cerra el archivo
    # archivo.write('Con esto terminamos')
    # Este es un error, ya que finally ya se ejecutó, esta cerrado