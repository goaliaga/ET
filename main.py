import numpy as np
from Funciones import *
from Asistente import *
arreglo=np.full((10,10),'---')
lista_asistente=[]

ciclo=True
llenar(arreglo)
def Salir():
    print("Hasta luego,Gonzalo Aliaga,06/07/2023")
    return False
def ingresoAsistente(lista_asistente,num_asiento):
    a = Asistente()
    c = False
    while c==False:
        c = a.setRut(input("Ingrese rut:"))
    a.num_asiento=num_asiento
    if num_asiento>=1 and a.num_asiento<=20:
        a.valor=120000
    if num_asiento>=21 and num_asiento<=50:
        a.valor=80000
    if num_asiento>=51 and num_asiento<=100:
        a.valor=50000
    lista_asistente.append(a)
def comprarEntrada(arreglo):
    try:
        cant_ent=int(input("Cantidad de entradas:"))
        if cant_ent>=1 and cant_ent<=3:
            cantidad=0
            while cantidad<cant_ent:
                mostrar(arreglo)
                try:
                    num_asiento=int(input("Seleccione ubicacion:"))
                    if num_asiento>=1 and num_asiento<=100:
                        disponible=comprobarAsiento(arreglo,num_asiento)
                        if disponible == True:
                            comprar(arreglo,num_asiento)
                            ingresoAsistente(lista_asistente,num_asiento)
                            cantidad=cantidad+1
                        else:
                            print("No esta disponible")
                    else:
                        print("Asientos entre 1 y 100")
                except BaseException as error:
                    print(f"Error:{error}")
        else:
            print("Cantidad de entradas entre 1 y 3")
    except BaseException as error:
        print(f"Error:{error}")

def listadoAsistentes(lista_asistente):
    for asistente in lista_asistente:
        print(f"Rut Asistente:{asistente.rut}")
def totales(lista_asistente):
        p=0
        g=0
        s=0
        tot_p=0
        tot_g=0
        tot_s=0
        for a in lista_asistente:
            if a.valor == 120000:
                p+=1
                tot_p+=120000
            if a.valor == 80000:
                g+=1
                tot_g+=80000
            if a.valor == 50000:
                s+=1
                tot_s+=50000
            tot_gen=(tot_s+tot_g+tot_p)
            tot_ent=(p+g+s)
        print("Tipo entradas    |cantidad|Total")
        print(f"Platinum $120000:| {p}      | {tot_p}")
        print(f"Gold $80000:     | {g}      | {tot_g}")
        print(f"Silver $50000:   | {s}      | {tot_s}")
        print(f"Total general:   | {tot_ent}      | {tot_gen}")

while ciclo:
    print("Creativos.cl")
    print("1) Comprar entradas")
    print("2) Mostrar ubicaciones disponibles")
    print("3) Ver Listado de Asistentes")
    print("4) Mostrar Ganancias Totales")
    print("5) Salir")
    try:
        op=int(input("Seleccione(1-5):"))
        match op:
            case 1:
                comprarEntrada(arreglo)
            case 2:
                mostrar(arreglo)
            case 3:
                listadoAsistentes(lista_asistente)
            case 4:
                totales(lista_asistente)
            case 5:
                ciclo=Salir()
            case _:
                print("Opcion no valida")
    except BaseException as error:
        print(f"Error:{error}")