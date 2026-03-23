def crear_category(db, data: dict):
    cursor = db.cursor()
    cursor.execute(
        """
        INSERT INTO categories (name, description)
        VALUES (%s, %s)
        """,
        (data["name"], data.get("description"))
    )
    db.commit()
    cursor.close()
    db.close()

def obtener_categories(db):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM categories ORDER BY id DESC")
    categories = cursor.fetchall()
    cursor.close()
    db.close()
    return categories

def obtener_category(db, category_id: int):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM categories WHERE id=%s", (category_id,))
    category = cursor.fetchone()
    cursor.close()
    db.close()
    return category

def actualizar_category(db, category_id: int, data: dict):
    cursor = db.cursor()
    cursor.execute(
        """
        UPDATE categories
        SET name=%s, description=%s
        WHERE id=%s
        """,
        (data["name"], data.get("description"), category_id)
    )
    db.commit()
    cursor.close()
    db.close()

def eliminar_category(db, category_id: int):
    cursor = db.cursor()
    cursor.execute("DELETE FROM categories WHERE id=%s", (category_id,))
    db.commit()
    cursor.close()
    db.close()