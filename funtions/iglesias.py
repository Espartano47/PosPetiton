def obtener_iglesias(db):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM iglesias")
    return cursor.fetchall()