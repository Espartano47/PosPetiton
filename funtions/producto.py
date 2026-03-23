from config.database import get_connection

# ---------------- LISTAR TODOS LOS PRODUCTOS ----------------
def obtener_productos(db):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    productos = cursor.fetchall()
    cursor.close()
    db.close()
    return productos


# ---------------- OBTENER PRODUCTO POR ID ----------------
def obtener_producto_por_id(db, producto_id: int):
    cursor = db.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT *
        FROM products
        WHERE id = %s
        """,
        (producto_id,)
    )
    producto = cursor.fetchone()
    cursor.close()
    db.close()
    return producto


# ---------------- OBTENER PRODUCTO POR NOMBRE ----------------
def obtener_producto_por_nombre(db, nombre: str):
    cursor = db.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT *
        FROM products
        WHERE name = %s
        """,
        (nombre,)
    )
    producto = cursor.fetchone()
    cursor.close()
    db.close()
    return producto


# ---------------- CREAR PRODUCTO ----------------
def crear_producto(db, producto: dict, usuario_id: int):
    cursor = db.cursor()
    cursor.execute(
        """
        INSERT INTO products
        (name, description, price, cost, stock, min_stock, barcode, status, image, created_by)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            producto["name"],
            producto.get("description"),
            producto["price"],
            producto.get("cost", 0),
            producto.get("stock", 0),
            producto.get("min_stock", 0),
            producto.get("barcode"),
            producto.get("status", 1),
            producto.get("photo"),
            usuario_id
        )
    )
    db.commit()
    cursor.close()
    db.close()


# ---------------- EDITAR PRODUCTO ----------------
def editar_producto(db, producto_id: int, data: dict, usuario_id: int):
    cursor = db.cursor()

    # Actualiza campos dinámicamente
    campos = ", ".join([f"{k} = %s" for k in data.keys()])
    valores = list(data.values())

    # Actualizamos también quien modificó
    campos += ", updated_by = %s"
    valores.append(usuario_id)

    valores.append(producto_id)

    query = f"""
        UPDATE products
        SET {campos}
        WHERE id = %s
    """

    cursor.execute(query, valores)
    db.commit()
    cursor.close()
    db.close()


# ---------------- ELIMINAR PRODUCTO ----------------
def eliminar_producto(db, producto_id: int):
    cursor = db.cursor()

    cursor.execute(
        """
        DELETE FROM products
        WHERE id = %s
        """,
        (producto_id,)
    )

    db.commit()
    cursor.close()
    db.close()