import numpy as np

matrizEscenario = np.empty((10, 10), dtype=object)
matrizComprador = np.empty((10, 10), dtype=object)

for entrada in range(10):
    matrizEscenario[entrada] = "disponible"
    matrizComprador[entrada] = "no disponible"


def comprar_entrada():
    entrada = input("Ingrese el tipo de entrada: Platinum, Gold, Silver: ")
    if entrada not in ['platinum', 'gold', 'silver, ']:
        print("Tipo de entrada inválida.")
        return
    else:
        if entrada == 'platinum':
            tipo2 = 0
        elif entrada == 'gold':
            tipo2 = 1
        elif entrada == 'silver':
            tipo2 = 2

        if 'X' in matrizEscenario[:, tipo2]:
            print("La entrada seleccionada ya ha sido vendida.")
            return
        else:
            fila_vacia = np.where(matrizEscenario[:, tipo2] == 'disponible')[0][0]
            matrizEscenario[fila_vacia, tipo2] = 'X'
            run = input("Ingrese el RUN del comprador (sin guiones ni puntos): ")
            if run in matrizComprador[:, tipo2]:
                print("El RUN ingresado ya ha sido registrado para otra entrada.")
                return
            matrizComprador[fila_vacia, tipo2] = run
            print("Entrada [", entrada, fila_vacia+1, "] adquirida correctamente.")


def mostrar_entradas_disponibles():
    print("Entradas disponibles:")
    for entrada in range(3):
        if entrada == 0:
            entrada2 = 'platinum'
        elif entrada == 1:
            entrada2 = 'gold'
        elif entrada == 2:
            entrada2 = 'silver'
        print("Entrada [", entrada2, "]:", matrizEscenario[:, entrada])


def ver_listado_asistentes():
    print("Listado de Asistentes:")
    for entrada in range(3):
        if entrada == 0:
            entrada2 = 'platinum'
        elif entrada == 1:
            entrada2 = 'gold'
        elif entrada == 2:
            entrada2 = 'silver'
        print("Asistentes [", entrada2, "]:", matrizComprador[:, entrada])


def mostrar_ventas_totales():
    valorPlatinum = 120000
    valorGold = 80000
    valorSilver = 50000

    ventasPlatinum = np.count_nonzero(matrizEscenario[:, 0] == 'X')
    ventasGold = np.count_nonzero(matrizEscenario[:, 1] == 'X')
    ventasSilver = np.count_nonzero(matrizEscenario[:, 2] == 'X')

    print("Tipo Platinum: cantidad -", ventasPlatinum, "/ total -", ventasPlatinum * valorPlatinum)
    print("Tipo Gold: cantidad -", ventasGold, "/ total -", ventasGold * valorGold)
    print("Tipo Silver: cantidad -", ventasSilver, "/ total -", ventasSilver * valorSilver)


def mostrar_menu():
    print("------ Menú de opciones ------")
    print("1. Comprar Entradas")
    print("2. Mostrar Entradas disponibles")
    print("3. Ver listado de Asistentes")
    print("4. Mostrar ventas totales")
    print("5. Salir")
    print("-----------------------------")


while True:
    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        comprar_entrada()
    elif opcion == "2":
        mostrar_entradas_disponibles()
    elif opcion == "3":
        ver_listado_asistentes()
    elif opcion == "4":
        mostrar_ventas_totales()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
  

                
    
              
                  
                        
    
    
    
                
                            
                        
                        
