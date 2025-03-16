
def calcular_temperatura_promedio(datos_ciudades):
 """Calcula la temperatura promedio de cada ciudad durante el período de tiempo dado.
 :param datos_ciudades: Lista de listas que contienen los datos de temperatura por ciudad y semana.
 :return: Diccionario con el nombre de la ciudad y su temperatura promedio"""

 nombres_ciudades = ["Quito", "Zaruma", "Cuenca"]
 temperatura_promedio = {}

 for i, ciudad in enumerate(datos_ciudades):
  temperaturas = []
  for semana in ciudad:
   for dia in semana:
    temperaturas.append(dia["temp"])

  # Calcular el promedio
  if temperaturas:
   temperatura_promedio[nombres_ciudades[i]] = sum(temperaturas) / len(temperaturas)
  else:
   temperatura_promedio[nombres_ciudades[i]] = None

 return temperatura_promedio


ciudad_temperatura = [
 [  # Quito
  [  # Semana 1
   {"day": "Lunes", "temp": 7},
   {"day": "Martes", "temp": 12},
   {"day": "Miércoles", "temp": 16},
   {"day": "Jueves", "temp": 17},
   {"day": "Viernes", "temp": 20},
   {"day": "Sábado", "temp": 21},
   {"day": "Domingo", "temp": 29}
  ],
  [  # Semana 2
   {"day": "Lunes", "temp": 9},
   {"day": "Martes", "temp": 10},
   {"day": "Miércoles", "temp": 14},
   {"day": "Jueves", "temp": 21},
   {"day": "Viernes", "temp": 24},
   {"day": "Sábado", "temp": 26},
   {"day": "Domingo", "temp": 27}
  ],
  [  # Semana 3
   {"day": "Lunes", "temp": 13},
   {"day": "Martes", "temp": 14},
   {"day": "Miércoles", "temp": 15},
   {"day": "Jueves", "temp": 22},
   {"day": "Viernes", "temp": 28},
   {"day": "Sábado", "temp": 31},
   {"day": "Domingo", "temp": 35}
  ],
  [  # Semana 4
   {"day": "Lunes", "temp": 6},
   {"day": "Martes", "temp": 7},
   {"day": "Miércoles", "temp": 9},
   {"day": "Jueves", "temp": 19},
   {"day": "Viernes", "temp": 21},
   {"day": "Sábado", "temp": 22},
   {"day": "Domingo", "temp": 23}
  ]
 ],
 [  # Zaruma
  [  # Semana 1
   {"day": "Lunes", "temp": 12},
   {"day": "Martes", "temp": 14},
   {"day": "Miércoles", "temp": 16},
   {"day": "Jueves", "temp": 17},
   {"day": "Viernes", "temp": 18},
   {"day": "Sábado", "temp": 20},
   {"day": "Domingo", "temp": 29}
  ],
  [  # Semana 2
   {"day": "Lunes", "temp": 13},
   {"day": "Martes", "temp": 16},
   {"day": "Miércoles", "temp": 17},
   {"day": "Jueves", "temp": 19},
   {"day": "Viernes", "temp": 21},
   {"day": "Sábado", "temp": 22},
   {"day": "Domingo", "temp": 23}
  ],
  [  # Semana 3
   {"day": "Lunes", "temp": 10},
   {"day": "Martes", "temp": 12},
   {"day": "Miércoles", "temp": 16},
   {"day": "Jueves", "temp": 17},
   {"day": "Viernes", "temp": 19},
   {"day": "Sábado", "temp": 21},
   {"day": "Domingo", "temp": 22}
  ],
  [  # Semana 4
   {"day": "Lunes", "temp": 14},
   {"day": "Martes", "temp": 17},
   {"day": "Miércoles", "temp": 19},
   {"day": "Jueves", "temp": 21},
   {"day": "Viernes", "temp": 24},
   {"day": "Sábado", "temp": 27},
   {"day": "Domingo", "temp": 30}
  ]
 ],
 [  # Cuenca
  [  # Semana 1
   {"day": "Lunes", "temp": 10},
   {"day": "Martes", "temp": 12},
   {"day": "Miércoles", "temp": 14},
   {"day": "Jueves", "temp": 21},
   {"day": "Viernes", "temp": 26},
   {"day": "Sábado", "temp": 29},
   {"day": "Domingo", "temp": 30}
  ],
  [  # Semana 2
   {"day": "Lunes", "temp": 9},
   {"day": "Martes", "temp": 11},
   {"day": "Miércoles", "temp": 13},
   {"day": "Jueves", "temp": 20},
   {"day": "Viernes", "temp": 27},
   {"day": "Sábado", "temp": 34},
   {"day": "Domingo", "temp": 41}
  ]
 ]
]

# Calcular los promedios
temperaturas_promedio = calcular_temperatura_promedio(ciudad_temperatura)

# Mostrar los resultados
for ciudad, temperatura in temperaturas_promedio.items():
 print(f"Temperatura promedio de {ciudad}: {temperatura:.2f}°C")