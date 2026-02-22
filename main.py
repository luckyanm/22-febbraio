import qrcode
from datetime import datetime
import os

# --- I TUOI DATI (Settimana 22-28 Feb 2026) ---
static_lines = [
    "7_GIORNI",
    "ANM",
    "2026-02-22T17:42",
    "2026-02-28T23:59",
    "E3GGJ2BYZE",
    "15",
    "2",
    "4",
    "050e9ecf31070627ed6a06783002899a3059e5749040e7f77aeb18f80c"
]

# --- CALCOLO ORARIO ATTUALE ---
# Prende l'ora del server e aggiunge il fuso orario +01:00
now = datetime.now()
timestamp_line = now.strftime("%Y-%m-%dT%H:%M:%S") + "+01:00"

# Unisce tutto
full_data = "\n".join(static_lines) + "\n" + timestamp_line

print(f"--- GENERAZIONE IN CORSO ---")
print(f"Orario biglietto: {timestamp_line}")

# --- CREAZIONE QR CODE COMPATTO ---
qr = qrcode.QRCode(
    version=7,      # Versione fissa ANM
    error_correction=qrcode.constants.ERROR_CORRECT_L, # Livello L
    box_size=5,     # DIMENSIONE RIDOTTA (Era 10, ora 5)
    border=2,       # Bordo sottile
)

qr.add_data(full_data)
qr.make(fit=True)

# Salva l'immagine sovrascrivendo sempre la stessa
filename = "qr.png"
img = qr.make_image(fill_color="black", back_color="white")
img.save(filename)

print(f"FATTO! Clicca su '{filename}' a sinistra per vedere il biglietto.")
