
import sqlite3

# Crear la base de datos, se ejecuta una sola vez si la bd no existe
conn = sqlite3.connect('unidades_refrigeradas.db')
cursor = conn.cursor()

 
# Estructura de las tablas 
cursor.executescript("""
-- TABLA: Modelos de unidades
CREATE TABLE IF NOT EXISTS ModeloUnidad (
    id_modelo_unidad INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_modelo TEXT NOT NULL,
    anio INT NOT NULL,
    nombre_de_pila TEXT NOT NULL
);

-- TABLA: Sistemas de enfriamiento
CREATE TABLE IF NOT EXISTS SistemaEnfriamiento (
    id_sistema INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_modelo TEXT NOT NULL,
    capacidad_watts REAL NOT NULL,
    volumen_max_enf REAL NOT NULL
);

-- TABLA: Unidades refrigeradas
CREATE TABLE IF NOT EXISTS Unidad (
    id_unidad INTEGER PRIMARY KEY AUTOINCREMENT,
    placas TEXT NOT NULL UNIQUE,
    id_modelo_unidad INTEGER NOT NULL,
    volumen_caja_m3 REAL NOT NULL,
    id_sistema INTEGER NOT NULL,
    FOREIGN KEY (id_modelo_unidad) REFERENCES ModeloUnidad(id_modelo_unidad),
    FOREIGN KEY (id_sistema) REFERENCES SistemaEnfriamiento(id_sistema)
);

-- TABLA: Pruebas térmicas
CREATE TABLE IF NOT EXISTS PruebaTermica (
    id_prueba_termica INTEGER PRIMARY KEY AUTOINCREMENT,
    id_unidad INTEGER NOT NULL,
    fecha DATE NOT NULL,
    temperatura_ambiente REAL NOT NULL,
    FOREIGN KEY (id_unidad) REFERENCES Unidad(id_unidad)
);

-- TABLA: Pruebas de modelado
CREATE TABLE IF NOT EXISTS ModeloEnfriamiento (
    id_prueba_modelo INTEGER PRIMARY KEY AUTOINCREMENT,
    id_unidad INTEGER NOT NULL,
    fecha DATE NOT NULL,
    temperatura_ambiente REAL NOT NULL,
    FOREIGN KEY (id_unidad) REFERENCES Unidad(id_unidad)
);

-- TABLA: Lecturas de sensores (para pruebas térmicas y modelado)
CREATE TABLE IF NOT EXISTS LecturaSensor (
    id_lectura INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor_codigo TEXT NOT NULL,
    tipo_sensor TEXT,
    hora TIME NOT NULL,
    valor REAL NOT NULL,
    id_prueba_termica INTEGER,
    id_prueba_modelo INTEGER,
    FOREIGN KEY (id_prueba_termica) REFERENCES PruebaTermica(id_prueba_termica),
    FOREIGN KEY (id_prueba_modelo) REFERENCES ModeloEnfriamiento(id_prueba_modelo)
);

-- TABLA: Resultados de análisis
CREATE TABLE IF NOT EXISTS ResultadosModelo (
    id_resultado INTEGER PRIMARY KEY AUTOINCREMENT,
    id_unidad INTEGER NOT NULL,
    temperatura_ambiente REAL NOT NULL,
    k_teorico REAL,
    k_experimental REAL,
    tiempo_setpoint INTEGER,
    FOREIGN KEY (id_unidad) REFERENCES Unidad(id_unidad)
);
""")

conn.commit()
conn.close()