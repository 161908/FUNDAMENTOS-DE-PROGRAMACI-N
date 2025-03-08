# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 7},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 9},
            {"day": "Martes", "temp": 10},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 27}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 13},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 35}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 6},
            {"day": "Martes", "temp": 7},
            {"day": "Miércoles", "temp": 9},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 21},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 23}
        ]
    ],
    [   # Zaruma
        [   # Semana 1
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 20},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 13},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 21},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp":23}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 22}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 30}
        ]
    ],
    [   # Cuenca
        [   # Semana 1
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp":30}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 9},
            {"day": "Martes", "temp": 11},
            {"day": "Miércoles", "temp": 13},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 41}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp":43}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 5},
            {"day": "Martes", "temp":7 },
            {"day": "Miércoles", "temp": 9},
            {"day": "Jueves", "temp": 10},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 10}
        ]
    ]
]

# Lista de nombres de ciudades corregida
ciudades = ["Quito", "Zaruma", "Cuenca"]

# Recorrer ciudades y calcular promedios semanales
for ciudad_idx, ciudad in enumerate(temperaturas):
    print(f"\nPromedios de temperatura en {ciudades[ciudad_idx]}:")
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum(dia["temp"] for dia in semana)
        promedio = suma_temperaturas / len(semana)  # Cálculo del promedio
        print(f"  Semana {semana_idx + 1}: {promedio:.2f}°F")

