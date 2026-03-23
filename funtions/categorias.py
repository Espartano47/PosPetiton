def obtener_categorias(db):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM categorias")
    return cursor.fetchall()

def obtener_categorias_byname(db,categoria = str):
    cursor = db.cursor(dictionary=True)
    cursor.execute(
    "SELECT * FROM categorias WHERE nombre = %s",
    (categoria,)   # 👈 OJO con la coma
    )
    return cursor.fetchall()