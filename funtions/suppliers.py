# funtions/suppliers.py

def crear_supplier(db, data: dict):
    cursor = db.cursor()
    cursor.execute(
        """
        INSERT INTO suppliers (name, phone, email, address)
        VALUES (%s, %s, %s, %s)
        """,
        (
            data["name"],
            data.get("phone"),
            data.get("email"),
            data.get("address"),
        )
    )
    db.commit()
    cursor.close()  # ✅ Solo cerramos el cursor, no la conexión


def obtener_suppliers(db):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM suppliers ORDER BY id DESC")
    suppliers = cursor.fetchall()
    cursor.close()
    return suppliers  # ❌ NO cerrar db


def obtener_supplier(db, supplier_id: int):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM suppliers WHERE id=%s", (supplier_id,))
    supplier = cursor.fetchone()
    cursor.close()
    return supplier


def actualizar_supplier(db, supplier_id: int, data: dict):
    cursor = db.cursor()
    cursor.execute(
        """
        UPDATE suppliers
        SET name=%s, phone=%s, email=%s, address=%s
        WHERE id=%s
        """,
        (
            data["name"],
            data.get("phone"),
            data.get("email"),
            data.get("address"),
            supplier_id
        )
    )
    db.commit()
    cursor.close()


def eliminar_supplier(db, supplier_id: int):
    cursor = db.cursor()
    cursor.execute("DELETE FROM suppliers WHERE id=%s", (supplier_id,))
    db.commit()
    cursor.close()