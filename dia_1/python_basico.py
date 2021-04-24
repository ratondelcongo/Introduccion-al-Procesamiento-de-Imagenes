# Tipos de datos basicos

# int 
-12312
12123
# float
23213.0
-23.121212
# string
'hola mundo'
"hola mundo"
# bool
True
False


# Impresion 
print("hola")                   # hola
print(4.5)                      # 4.5
# print(hola)                   # error de impresion
print("hola", end='-')          # hola- (sin salto de linea)


# Entradas

# solicitar nombre y guardar en variable
nombre = input('Nombre: ')
# solicitar un numero
edad = int(input('Edad: '))


# Variables 
a = 10
b = 3


# Operaciones

# Artimetica                    # + - * / // %
suma = a + b                    # 13
resta = a - b                   # 7
producto = a * b                # 30
division = a / b                # 3.3333333333333335
division_piso = a // b          # 3
residuo = a % b                 # 1
# Criterio                      # Br Ex Di Mu Ad Su

# Condicionales                 # == != <= >= < >
r1 = a == b                     # False
r2 = a > b                      # True
r3 = not r1                     # True      # en C o C++ es !
r4 = r1 or r2                   # True      # en C o C++ es ||
r5 = r1 and r2                  # False     # en C o C++ es &&


# If / Else / Elif
if a == b:
    print('"a" es igual a "b"')
elif a > b:
    print ('"a" es mayor que "b"')
else:
    print('"a" es menor(diferente y no mayor) de "b"')


# Bucles

# For
for i in range(5):              # range(final)
    print(i, end=',')           # 0, 1, 2, 3, 4,

for i in range(1, 6):           # range(inicio, final)
    print(i, end=',')           # 1, 2, 3, 4, 5, 

for i in range(1, 6, 2):        # range(inicio, final, salto)
    print(i, end=',')           # 1, 3, 5, 

# While
i = 0
while i < 5:
    print(i, end=',')           # 1, 2, 3, 4, 5,
    i += 1


# Listas
x = [1, 2, 3, 4, 5]
print(x)                        # [1, 2, 3, 4, 5]
print(x[0])                     # 1
y = [1, 'Hola', True, 0.33333]

# Agregar un elemento al final
x.append(6)
print(x)                        # [1, 2, 3, 4, 5, 6]

# Agregar multiples elementos al final
x.extend([7, 8, 9])
print(x)                        # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Eliminar ultimo elemento
x.pop()
print(x)                        # [1, 2, 3, 4, 5, 6, 7, 8]

# Referenciar una lista
z = x

# Copiar una lista
z = x[:]

# Longitud de una lista
print(len(x))                   # 8

# Recorrer una lista
for i in range(len()):
    print(x[i], end=', ')       # 1, 2, 3, 4, 5, 6, 7, 8


# Notacion Slice [incio:final] o [inicio:final:salto]

x = [1, 2, 3, 4, 5, 6, 7, 8]

x_siliced = x[0:6:2]
print(x_siliced)                # [0, 2, 4]

