def llenar(arreglo):
    x=0
    for f in range(10):
        for c in range(10):
            x+=1
            arreglo[f][c]=str(x)
def mostrar(arreglo):
    for f in range(10):
        fila=''
        for c in range(10):
            dato=str(arreglo[f][c])
            if len(str(arreglo[f][c])) == 1:
                dato='00'+str(arreglo[f][c])
            if len(str(arreglo[f][c])) == 2:
                dato='0'+str(arreglo[f][c])
            if len(str(arreglo[f][c])) == 3:
                dato=str(arreglo[f][c])
            fila = fila + ' ' + dato
        print(fila)
def comprar(arreglo,num_asiento):
    x=0
    for f in range(10):
        for c in range(10):
            x=x+1
            if str(x) == str(num_asiento):
                arreglo[f][c]='XXX'
def comprobarAsiento(arreglo,num_asiento):
    x = 0
    for f in range(10):
        for c in range(10):
            x = x + 1
            if str(x) == str(num_asiento):
                if arreglo[f][c] == 'XXX':
                    return False
    return True