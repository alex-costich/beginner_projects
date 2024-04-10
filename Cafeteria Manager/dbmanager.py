import sqlite3

# Path para la base de datos
db_path = 'orderGenius.db'

# Conexión a la BD
conn = sqlite3.connect(db_path)

# Definición del cursor
cur = conn.cursor()

# Agregamos la columna nueva
alter_table_command = "ALTER TABLE Tmenus ADD COLUMN URL_imagen TEXT" # Comando

# Ejecución de comandos
try:
    cur.execute(alter_table_command) # Ejecuta el comando
    conn.commit() # Guarda los cambios
    print("Column added successfully.") # Notifica
except sqlite3.Error as e:
    print(f"An error occurred: {e}") # Notifica de error

# Cierra la conexión
conn.close()
