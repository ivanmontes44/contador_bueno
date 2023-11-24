def comparar_ficheros(fichero1, fichero2, coincidencias, volcar_resultado, insensible_mayusculas):
    # Leemos el contenido de los ficheros con la función
    with open(fichero1, 'r', encoding='utf-8') as file1, open(fichero2, 'r', encoding='utf-8') as file2: # 'r' en modo lectura
        lines1 = file1.readlines()
        lines2 = file2.readlines()

    # Creamos otra función para comparar líneas teniendo en cuenta la posibilidad de mayúsculas y minúsculas
    def comparar_lineas(line1, line2):
        if insensible_mayusculas:
            return line1.lower() == line2.lower() # aplicamos el lower para que todo sea en minúsculas
        else:
            return line1 == line2

    # Indicamos las variables para encontrar líneas coincidentes y diferentes
    coincidentes = []
    diferentes = []

    for line1 in lines1:
        for line2 in lines2:
            if comparar_lineas(line1, line2):
                coincidentes.append(line1)
                break

    for line1 in lines1:
        if line1 not in coincidentes:
            diferentes.append(line1)

    # Mostramos los resultados por pantalla
    print("Operación satisfactoria.")
    print(f"Coincidencias encontradas: {len(coincidentes)}") # f cadena de texto con nombres de variables
    print(f"Diferencias encontradas: {len(diferentes)}")

    # Volcamos los resultados al fichero de salida si se solicita
    if volcar_resultado:
        with open(volcar_resultado, 'w', encoding='utf-8') as output_file: # 'w' en modo escritura
            if coincidencias:
                output_file.write("Coincidencias:\n")
                output_file.writelines(coincidentes)
            if diferentes:
                output_file.write("Diferencias:\n")
                output_file.writelines(diferentes)

if __name__ == "__main__":
    fichero1 = input("Introduce el nombre del primer fichero: ")
    fichero2 = input("Introduce el nombre del segundo fichero: ")
    coincidencias = input("¿Quieres obtener coincidencias? No para diferencias (Sí/No): ").strip().lower() == "sí" # strip para quitar los espacios iniciales y finales en la cadena
    volcar_resultado = input("Introduce el nombre del fichero de salida (deja en blanco si no quieres volcar resultados): ")
    insensible_mayusculas = input("¿Quieres que la comparación sea insensible a mayúsculas y minúsculas? (Sí/No): ").strip().lower() == "sí"

    comparar_ficheros(fichero1, fichero2, coincidencias, volcar_resultado, insensible_mayusculas)

