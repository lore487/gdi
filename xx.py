import tkinter as tk
import math

class MouseXApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse X")

        # Rimuove la barra del titolo e i bordi della finestra
        self.root.overrideredirect(True)
        # Mantiene la finestra sempre in primo piano
        self.root.attributes('-topmost', True)
        # Imposta la trasparenza generale della finestra (0.0 è completamente trasparente, 1.0 è opaco)
        self.root.attributes('-alpha', 0.9) # Leggermente trasparente per vedere il contenuto sottostante
        
        # Imposta un colore specifico come trasparente per rendere la forma della finestra (utile su Windows)
        # Scegli un colore che difficilmente userai per il tuo disegno, es. un nero quasi puro
        self.root.wm_attributes("-transparentcolor", "#000001") 

        self.canvas_size = 50 # Dimensione del lato della finestra/canvas (es. 50x50 pixel)
        self.root.geometry(f"{self.canvas_size}x{self.canvas_size}") # Imposta la dimensione della finestra

        # Crea un canvas dove disegnare la "X"
        # Il background deve essere lo stesso colore impostato come trasparente (#000001)
        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, highlightthickness=0, bg="#000001")
        self.canvas.pack()

        # Nasconde il cursore predefinito del mouse quando si trova sopra la finestra dell'applicazione
        self.root.config(cursor="none") 

        self.draw_x_shape() # Disegna la "X" iniziale
        self.update_x_position() # Avvia il loop di aggiornamento della posizione

    def draw_x_shape(self):
        # Pulisce il canvas prima di ridisegnare
        self.canvas.delete("all") 

        center_x = self.canvas_size / 2
        center_y = self.canvas_size / 2
        
        # Il raggio del simbolo (cerchio e X) sarà leggermente più piccolo del canvas per un piccolo margine
        symbol_radius = self.canvas_size / 2 * 0.8 

        # Disegna il cerchio rosso
        # Le coordinate sono (x1, y1, x2, y2) per il bounding box dell'ovale
        self.canvas.create_oval(
            center_x - symbol_radius, center_y - symbol_radius,
            center_x + symbol_radius, center_y + symbol_radius,
            fill="#dc2626",      # Colore rosso scuro (Tailwind red-600)
            outline=""           # Nessun bordo per il cerchio
        )

        # Disegna la "X" bianca all'interno del cerchio
        # La lunghezza delle linee della "X" è calcolata per stare bene all'interno del cerchio
        x_line_length = symbol_radius * math.sqrt(2) * 0.6 
        half_x_line_length = x_line_length / 2

        # Disegna la prima linea della "X" (diagonale da in alto a sinistra a in basso a destra)
        self.canvas.create_line(
            center_x - half_x_line_length, center_y - half_x_line_length,
            center_x + half_x_line_length, center_y + half_x_line_length,
            fill="white",        # Colore bianco
            width=4,             # Spessore della linea
            capstyle=tk.ROUND    # Estremità arrotondate per le linee
        )
        # Disegna la seconda linea della "X" (diagonale da in alto a destra a in basso a sinistra)
        self.canvas.create_line(
            center_x + half_x_line_length, center_y - half_x_line_length,
            center_x - half_x_line_length, center_y + half_x_line_length,
            fill="white",
            width=4,
            capstyle=tk.ROUND
        )

    def update_x_position(self):
        # Ottiene le coordinate globali attuali del puntatore del mouse
        mouse_x = self.root.winfo_pointerx()
        mouse_y = self.root.winfo_pointery()

        # Calcola la nuova posizione della finestra per centrare la "X" sul mouse
        # Sottrae metà della dimensione del canvas per posizionare il centro della finestra sul cursore
        new_x = mouse_x - self.canvas_size // 2
        new_y = mouse_y - self.canvas_size // 2

        # Sposta la finestra alla nuova posizione
        self.root.geometry(f"+{new_x}+{new_y}")

        # Richiama questa funzione dopo un breve ritardo (es. 10 millisecondi)
        # per un aggiornamento fluido della posizione
        self.root.after(10, self.update_x_position)

# Questo blocco viene eseguito solo quando lo script viene avviato direttamente
if __name__ == "__main__":
    root = tk.Tk() # Inizializza la finestra principale di Tkinter
    app = MouseXApp(root) # Crea un'istanza della nostra applicazione
    root.mainloop() # Avvia il loop principale di Tkinter che gestisce gli eventi
