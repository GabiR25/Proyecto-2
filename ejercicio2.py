def funcion(linea):
    elementos = linea.strip().split(';')
    elemento = elementos[1:]
    return sum(map(int,elemento))

def funcion1(linea):
    elementos = linea.strip().split(';')
    elemento = elementos[1:]
    return sum(map(int, elemento))/4

datos = open('ejercicio2.csv','r')
primera_linea = datos.readline()
lineas = datos.readlines()

print('\n||Estadisticas de ganancia de la empresa||')
print(f'{primera_linea}')
for linea in lineas[1:]:
    datos_sep = linea.rstrip('\n').split(';')
    print(f'{datos_sep} | Total de año: ${funcion(linea)} | Promedio de año: ${funcion1(linea)}')

total_ganancias = sum(map(lambda linea: int(linea.rstrip('\n').split(';')[1]), lineas))
print(f'\nTotal de ganancias de todos los años: ${total_ganancias}')
datos.close()