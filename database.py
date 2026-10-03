import sqlite3

DATABASE = "inventory.db"

def create_database():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL DEFAULT 0,
            qr_code TEXT UNIQUE NOT NULL
        )
    """)

    connection.commit()
    connection.close()

if __name__ == "__main__":
        create_database()
        print("Base de données créée avec succès")


def insert_products():
      products = [
            ("P001","Bouteille d'eau", "Boisson", 1.50, 25, "P001"),
            ("P002","Jus de pomme", "Boisson", 2.25, 18, "P002"),
            ("P003","Boite de biscuits", "Aliment", 3.50, 12, "P003"),
            ("P004","Sac à Dos", "Accessoire", 35.00, 8, "P004"),
            ("P005","Cahier", "Papeterie", 4.25, 30, "P005"),
            ("P006","Stylo bleu", "Papeterie", 1.25, 50, "P006"),
            ("P007","Livre", "Papeterie", 18.00, 10, "P007"),
            ("P008","Casquette", "Vêtement", 15.00, 7, "P008"),
            ("P009","Tasse", "Accessoire", 8.50, 14, "P009"),
            ("P010","Clé USB", "Électronique", 12.00, 20, "P010"),

      ]

      connection = sqlite3.connect(DATABASE)
      cursor = connection.cursor()

      cursor.executemany("""
           INSERT OR IGNORE INFO products
           (id, name, category, price, stock, qr_code)
           VALUES (?,?,?,?,?,?)
      """, products)

      connection.commit()
      connection.close()


if __name__ == "__main__":
        create_database()
        insert_products()
        print("Base de données initialisée avec 10 produits.")
            
      