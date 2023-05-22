archivo = open('prueba.txt', 'r',encoding = 'utf8')

# print(archivo.read())
# print(archivo.read(16)) # Imprime los primeros x caracteres
# print(archivo.read(10)) # Continúa desde el anterior
print(archivo.readline()) # Lee la primera linea completa
print(archivo.readline()) # Como está a continuación, leería la 2da linea

# los parámetros del método open son {
#   r: Read
#   a: Append
#   w: Write
#   x: Excepción, en caso de que no exista el archivo
#   t: texto
#   b: archivos binarios
#   w+: Lee y escribe
#   r+: Escribir y leer
#   encoding = 'utf8': Juego de caracteres UTF-8 para no tener problemas con acentos
#   }
