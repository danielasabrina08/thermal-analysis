import sqlite3

conn = sqlite3.connect('unidades_refrigeradas.db')
cursor = conn.cursor()

cursor.execute("""
    UPDATE ModeloUnidad
    SET nombre_modelo = "Hino Serie 300 616"
    WHERE id_modelo_unidad = 9
"""         
)

conn.commit()
conn.close()