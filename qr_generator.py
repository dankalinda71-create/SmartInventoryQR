import sqlite3
import os
import qrcode

DATABASE = "inventory.db"
OUTPUT_DIR = "qr_codes"

def generate_qr_codes():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("SELECT id FROM products ORDER BY id")
    products = cursor.fetchall()

    connection.close()

    if not products:
        print("Aucun produit trouvé dans la base de données.")
        return

    for(product_id,) in products:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4
        )
        # Le QR contient uniquement l'identifiant
        qr.add_data(product_id)
        qr.make(fit=True)

        image = qr.make_image()

        filename= os.path.join(
            OUTPUT_DIR,
            f"{product_id}.png"
        )

        image.save(filename)

        print(f"QR généré : {filename}")

    print(f"\n{len(products)} QR code(s) généré(s).")

if __name__ == "__main__":
    generate_qr_codes()