import random

trabajadores = {
                "juan perez",
                "maria garcia",
                "carlos lopez",
                "ana martinez",
                "pedro rodriguez",
                "laura hernandez",
                "miguel sanchez",
                "isabel gomez",
                "francisco diaz",
                "elena fernandez"}

sueldomin = 300000
sueldomax = 2500000

def asignar_sueldo(trabajadores, sueldomin, sueldomax):
    sueldo={}
    for trabajador in trabajadores:
    
        sueldo = [trabajadores] = random.randint(sueldomin, sueldomax)
        return asignar_sueldo 
                







def menu():
    while True:
        print("\nMenu principal: ")
        print("1. asignar sueldos aleatorios")
        print("2. clasificar sueldos")
        print("3. ver estadisticas")
        print("4. reporte de sueldos")
        print("5. generar archivo(csv)")
        print("6. salir del programa")
        opcion = input("elige una opcion: ")
        if opcion == "1":
            asignar_sueldo(trabajadores, sueldomin, sueldomax)
        elif opcion == "2":
            clasificar_sueldos(trabajadores)
        elif opcion == "3":
            ver_estadisticas(trabajadores)
        elif opcion == "4":
            reporte_de_sueldos(trabajadores)
        elif opcion == "5":
            generar_archivo
        elif opcion == "6":
            print("cerrando el programa, desarrollado por Marcos Bustos, rut 20.204.725-4...")
        break

    
menu()
