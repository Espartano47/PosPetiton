# ---------------- OBTENER CLIENTES ----------------
def obtener_clientes(db):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customers ORDER BY id DESC")
    clientes = cursor.fetchall()

    cursor.close()
    db.close()

    return clientes


# ---------------- OBTENER CLIENTE POR ID ----------------
def obtener_cliente(db, cliente_id: int):
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM customers WHERE id=%s", (cliente_id,))
    cliente = cursor.fetchone()

    cursor.close()
    db.close()

    return cliente


# ---------------- CREAR CLIENTE ----------------
def crear_cliente(db, cliente: dict, usuario_id: int):
    cursor = db.cursor()

    cursor.execute(
        """
        INSERT INTO customers
        (name, phone, email, address, document, status, created_by)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            cliente["name"],
            cliente.get("phone"),
            cliente.get("email"),
            cliente.get("address"),
            cliente.get("document"),
            cliente.get("status", 1),
            usuario_id
        )
    )

    db.commit()

    cursor.close()
    db.close()


# ---------------- ACTUALIZAR CLIENTE ----------------
def actualizar_cliente(db, cliente_id: int, cliente: dict, usuario_id: int):
    cursor = db.cursor()

    cursor.execute(
        """
        UPDATE customers
        SET
        name=%s,
        phone=%s,
        email=%s,
        address=%s,
        document=%s,
        status=%s,
        updated_by=%s
        WHERE id=%s
        """,
        (
            cliente["name"],
            cliente.get("phone"),
            cliente.get("email"),
            cliente.get("address"),
            cliente.get("document"),
            cliente.get("status", 1),
            usuario_id,
            cliente_id
        )
    )

    db.commit()

    cursor.close()
    db.close()


# ---------------- ELIMINAR CLIENTE ----------------
def eliminar_cliente(db, cliente_id: int):
    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM customers WHERE id=%s",
        (cliente_id,)
    )

    db.commit()

    cursor.close()
    db.close()