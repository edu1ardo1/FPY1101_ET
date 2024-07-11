import csv
import os

#definicion del nombre del archivo csv
archivo_csv = "datos_csv"

random =("300.000","2.500.000")

#funcion para cargar datos de los trabajadores en un archivo csv 
def cargar_datos():
    datos = []
    try:
        with open(archivo_csv, mode="r", newline="") as file:
            reader =csv.DictReader(file)
            for row in reader:
                datos.append(row)
    except FileNotFoundError:
        print(f"el archivo {archivo_csv} no existe. se creara uno nuevo.")
        return datos
    
#funcion para guardar datos en un archivo_csv
def guardar_datos(datos):
    try:
        with open(archivo_csv,mode="w", newline="")as file:
            fieldnames = ["nombre","sueldo","descuento"]
            writer = csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader()
            for dato in datos:
                writer.writerow(dato)
        print(f"datos guardados exitosamente en {archivo_csv}.")
    except IOError:
        print(f"error al intentar guardar los datos en{archivo_csv}.")

lista_trabajadores = ["juan perez","maria garcia","carlos lopez","ana martinez","pedro rodriguez","laura hernandez","miguel sanchez","isabel gomez","francisco diaz","elena hernandez"]

print(lista_trabajadores)

#funcion para agregar sueldo a un  trabajador en archivo_csv
def agregar_sueldo(sueldo):
    nombre = input("ingrese el nombre del trabajador: ")
    sueldo = float(input("ingrese el sueldo del trabajador: "))
    descuento = int(input("ingrese el descuento del IVA: "))
    trabajador = {"nombre":"nombre","sueldo":"sueldo","descuento del IVA":"descuento del IVA"}


#ciclo principal del programa
while True:
    print("=====sistema de gestion de sueldos=====")
    print("1. asignar sueldos aleatorios")
    print("2. clasificar sueldos")
    print("3. ver estadisticas")
    print("4. reporte de sueldos")
    print("5. salir del programa")

    opcion = input("seleccione una opcion: ")

    if opcion == "1":
        agregar_producto(productos)
    elif opcion == '2':
        realizar_venta(productos)
    elif opcion == '3':
        mostrar_inventario(productos)
    elif opcion == '4':
            # Guardar productos en archivo CSV antes de salir
        guardar_productos(productos)
        print("¡Hasta luego!")
    break
else:
    print("Opción no válida. Por favor, seleccione una opción válida.")
        
# Iniciar el programa
if __name__ == "__main__":
    main()

print("desarrollado por jovanni Riquelme")
print("21-986-624-0")