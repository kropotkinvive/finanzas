import csv

def main():
    archivo_csv = 'calificaciones.csv'
    encabezados = ['Nombre', 'Apellido', 'Nota', 'Estado']
    
    # Crear archivo con encabezados si no existe
    try:
        with open(archivo_csv, 'x', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(encabezados)
    except FileExistsError:
        pass
    
    while True:
        print("\nIngrese los datos del estudiante (o 'salir' para terminar):")
        
        # Validación nombre
        nombre = input("Nombre: ").strip().title()
        if nombre.lower() == 'salir':
            break
            
        # Validación apellido
        apellido = input("Apellido: ").strip().title()
        if apellido.lower() == 'salir':
            break
        
        # Validación nota con nuevo rango
        while True:
            nota = input("Nota (0-20): ").strip()
            if nota.lower() == 'salir':
                print("Saliendo del programa...")
                return
            try:
                nota = float(nota)
                if 0 <= nota <= 20:
                    # Determinar estado según las nuevas reglas
                    if nota == 0:
                        estado = "Inasistente"
                    elif 1 <= nota < 10:
                        estado = "Reprobado"
                    else:  # 10 <= nota <= 20
                        estado = "Aprobado"
                    break
                print("¡Error! La nota debe estar entre 0 y 20")
            except ValueError:
                print("¡Error! Ingrese un valor numérico válido")
        
        # Escribir en el CSV
        with open(archivo_csv, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([nombre, apellido, nota, estado])
        
        # Confirmación para continuar
        if input("\n¿Agregar otro estudiante? (s/n): ").lower() == 'n':
            print("\nRegistro completo. Archivo guardado:", archivo_csv)
            break

if __name__ == "__main__":
    main()
