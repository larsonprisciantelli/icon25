import tkinter as tk
from tkinter import ttk, messagebox

def suggerisci_film():
    messagebox.showinfo("Suggerimento", "Ecco un film suggerito per te!")

def scopri_genere():
    messagebox.showinfo("Genere", "Il genere del film/serie TV selezionato è: ...")

def interroga_sistema():
    messagebox.showinfo("Interrogazione", "Risposta del sistema: ...")

def esci():
    root.destroy()

# Creazione della finestra principale
root = tk.Tk()
root.title("CinemaAI")
root.geometry("600x370")  # Finestra più piccola

# Colori personalizzati
PRIMARY_COLOR = "#2C3E50"      # Sfondo principale
ACCENT_COLOR  = "#E74C3C"      # Colore pulsanti
TEXT_COLOR    = "#ECF0F1"      # Colore del testo
BTN_HOVER     = "#C0392B"      # Colore pulsante in hover/attivo

# Configurazione stile ttk
style = ttk.Style(root)
style.theme_use("clam")

root.configure(bg=PRIMARY_COLOR)

style.configure("TFrame",
                background=PRIMARY_COLOR)

# Stile per il titolo (grande)
style.configure("Title.TLabel",
                font=("Helvetica", 20, "bold"),
                background=PRIMARY_COLOR,
                foreground=TEXT_COLOR)

# Stile per il sottotitolo (più piccolo)
style.configure("Subtitle.TLabel",
                font=("Helvetica", 12),
                background=PRIMARY_COLOR,
                foreground=TEXT_COLOR)

# Stile per i pulsanti
style.configure("TButton",
                font=("Helvetica", 12, "bold"),
                padding=10,
                borderwidth=0,
                relief="flat",
                foreground=TEXT_COLOR,
                background=ACCENT_COLOR)

style.map("TButton",
    background=[("active", BTN_HOVER), ("pressed", BTN_HOVER)],
    foreground=[("active", TEXT_COLOR), ("pressed", TEXT_COLOR)]
)

# Layout principale
frame = ttk.Frame(root, padding=20)
frame.pack(expand=True, fill="both")

# Titolo
title_label = ttk.Label(frame, text="Benvenuto", style="Title.TLabel")
title_label.pack(pady=10)

# Sottotitolo con font più piccolo e testo aggiornato
subtitle_label = ttk.Label(frame,
                           text="Clicchi l'opzione che desidera scegliere...",
                           style="Subtitle.TLabel")
subtitle_label.pack(pady=5)

# Pulsanti
btn_suggerisci = ttk.Button(frame,
    text="Consigliami un nuovo film",
    command=suggerisci_film
)
btn_suggerisci.pack(fill="x", padx=50, pady=5)

btn_scopri = ttk.Button(frame,
    text="Scopri il genere di un film o serie TV",
    command=scopri_genere
)
btn_scopri.pack(fill="x", padx=50, pady=5)

btn_interroga = ttk.Button(frame,
    text="Interroga il sistema",
    command=interroga_sistema
)
btn_interroga.pack(fill="x", padx=50, pady=5)

# Pulsante Esci ripristinato
btn_esci = ttk.Button(frame,
    text="Esci",
    command=esci
)
btn_esci.pack(fill="x", padx=50, pady=5)

# Avvio del loop principale
root.mainloop()