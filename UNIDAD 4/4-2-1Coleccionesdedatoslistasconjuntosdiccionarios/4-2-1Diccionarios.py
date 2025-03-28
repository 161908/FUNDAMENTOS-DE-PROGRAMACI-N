""" Utilizar diccionarios en Python para representar información estructurada y realizar operaciones comunes.

Instrucciones:

Crear un Diccionario:

Crea un diccionario llamado informacion_personal que contenga información ficticia sobre una persona, incluyendo al menos las claves "nombre", "edad", "ciudad" y "profesion".
Acceder y Modificar Valores:

Accede al valor asociado con la clave "ciudad" y modifícalo con una ciudad diferente.
Agrega una nueva clave-valor al diccionario que represente la "profesion" de la persona.
Verificar Existencia de Claves:

Verifica si la clave "telefono" existe en el diccionario. Si no existe, agrégala con un número de teléfono ficticio.
Eliminar una Clave:

Elimina la clave "edad" del diccionario, ya que esa información no es necesaria.
Imprimir el Diccionario Final:

Imprime el diccionario resultante después de realizar todas las operaciones."""

# Crear un diccionario con información personal
print("--------Diccionario Personal-------------")
informacion_personal = {
    "nombre": "Nataly",
    "edad": "29",
    "ciudad": "Quito",
    "profesion": "Abogada",
}

# Imprimir el diccionario original
print("Diccionario original:", informacion_personal)

# Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Zaruma"

# Agregar una nueva clave-valor "telefono" si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0934799021"

# Agregar una nueva clave-valor "correo"
informacion_personal["correo"] = "nataly@gmail.com"

# Eliminar la clave "edad"
informacion_personal.pop("edad", None)

# Imprimir el diccionario final
print("Diccionario final:", informacion_personal)