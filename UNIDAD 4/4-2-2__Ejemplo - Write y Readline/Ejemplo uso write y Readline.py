"""Escritura de Archivo de Texto:

Crea un nuevo archivo llamado my_notes.txt.
Escribe al menos tres líneas de notas personales en el archivo.
Lectura de Archivo de Texto:

Abre el archivo my_notes.txt.
Lee el contenido del archivo línea por línea utilizando el método adecuado.
Muestra en la consola cada línea leída.
Cierre de Archivos:

Asegúrate de cerrar el archivo my_notes.txt después de realizar las operaciones necesarias.
Instrucciones Adicionales:

Utiliza métodos como write() y readline() para manipular el archivo de texto.
Agrega comentarios explicativos en tu código."""
# Ejemplo de Escritura en Archivos en Python usando write() y Readline()
# Definimos el nombre del archivo
file_name = "my_notes.txt"
# Escritura en el archivo de texto
# Modo de apertura: "w" para escritura (write)
file = open('my_notes.txt', 'w')

# Metodo write(): escribir una línea a la vez
file.write("1. Hoy comencé a practicar manejo de archivos en Python.\n")
file.write("2. Es importante siempre cerrar los archivos después de usarlos.\n")
file.write("3. Aprendí la diferencia entre los modos 'w' y 'r'.\n")
file.write("4. Practicar todos los días mejora mi lógica de programación.\n")
file.write("5. Los comentarios en el código ayudan a entender mejor el proceso.\n")
file.write("6. El método write() se utiliza para escribir en archivos.\n")
file.write("7. El método readline() se utiliza para leer archivos línea por línea.\n")
file.write("8. Puedo usar .strip() para eliminar saltos de línea sobrantes.\n")
file.write("9. Con Python, automatizar tareas de archivos es sencillo y útil.\n")
file.write("10. Seguiré practicando para dominar la manipulación de archivos.\n")

# Cierra el archivo después de escribir
file.close()

# Lectura del archivo de texto
# Abre el archivo 'my_notes.txt' en modo lectura ('r')
file = open('my_notes.txt', 'r')

# Metodo readline(): leemos cada línea una a una
# Lee y muestra cada línea del archivo
line = file.readline()
while line:
    print(line.strip())  # .strip() elimina saltos de línea adicionales
    line = file.readline()

# Cierra el archivo después de leer
file.close()