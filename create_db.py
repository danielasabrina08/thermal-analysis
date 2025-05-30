
import sqlite3
import csv

conn = sqlite3.connect('unidades_refrigeradas.db')
cursor = conn.cursor()

with open("datos_camionetas_ref.csv", newline='', encoding='utf-8') as archivo:
    reader = csv.reader(archivo)
    next(reader)  # Salta la primera línea (encabezado)
    for row in reader:
     #   cursor.execute("INSERT INTO ModeloUnidad (nombre_modelo, anio, nombre_de_pila) VALUES (?, ?, ?);", row)
         cursor.execute("INSERT INTO Unidad (placas, id_modelo_unidad, volumen_caja_m3, id_sistema) VALUES (?, ?, ?, ?);", row)


# Ejemplo: insertar modelo de unidad
#cursor.execute("""           

 #   INSERT INTO ModeloUnidad (nombre_modelo, anio, nombre_de_pila) 
  #      VALUES ('Isuzu Elf 500', 2010, 'Isuzu 1');           
               
#""")

'''
cursor.execute(""" DELETE FROM ModeloUnidad WHERE nombre_de_planta = 'Hilux'; """)
'''

conn.commit()
conn.close()
