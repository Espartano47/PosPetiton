# ---------------- CREAR CONFIGURACION ----------------

def crear_configuracion(db, config: dict):

    cursor = db.cursor()

    cursor.execute(
        """
        INSERT INTO settings
        (system_name, currency, tax, business_name, phone, email, address, logo)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            config["system_name"],
            config.get("currency"),
            config.get("tax"),
            config.get("business_name"),
            config.get("phone"),
            config.get("email"),
            config.get("address"),
            config.get("logo")
        )
    )

    db.commit()
    cursor.close()
    db.close()



# ---------------- OBTENER CONFIG ----------------

def obtener_configuracion(db):

    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM settings LIMIT 1")

    config = cursor.fetchone()

    cursor.close()
    db.close()

    return config



# ---------------- ACTUALIZAR CONFIG ----------------

def actualizar_configuracion(db, config: dict):

    cursor = db.cursor()

    cursor.execute(
        """
        UPDATE settings
        SET system_name=%s,
        currency=%s,
        tax=%s,
        business_name=%s,
        phone=%s,
        email=%s,
        address=%s,
        logo=%s
        WHERE id=%s
        """,
        (
            config["system_name"],
            config.get("currency"),
            config.get("tax"),
            config.get("business_name"),
            config.get("phone"),
            config.get("email"),
            config.get("address"),
            config.get("logo"),
            config["id"]
        )
    )

    db.commit()
    cursor.close()
    db.close()