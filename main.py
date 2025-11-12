# AUTORE: Christian Lancini
# Data inizio sviluppo: 9/11/25

# BUG TROVATI:
#! 1. BUG: Appena torno nella home il tasto impostazioni non va.


# DA FARE:
#TODO: Fai la grafica per inserire i dati per confermare la prenotazione
#TODO: Creare schermata impostazioni
#TODO: Migliorare UI


import tkinter as tk
import json

window = tk.Tk()
window.geometry("1200x700")
window.title("Gestione di prenotazione")
window.configure(background="white")

# --- VARIABILI GLOBAL PER CLEAR2 ---
frame_titolo_prenotazioni = None
frame_elenco_sale = None


# --- FUNZIONI ---
def clear():
    for widget in window.winfo_children():
        widget.pack_forget()
        widget.grid_forget()
        widget.place_forget()

def dati_sala():
    pass

def prenota_sala_ui(sala_selezionata):
    with open("sale.json", "r", encoding="utf-8") as file:
        sale_data = json.load(file) 

    sala_trovata = None
    for s in sale_data:
        if s["descrizione"] == sala_selezionata["descrizione"]:
            sala_trovata = s
            print(sala_trovata)
            break

    if sala_trovata:
        clear()

        button_back_widget = tk.Frame(window, bg="white")
        button_back_widget.pack(anchor="nw", padx=10, pady=10)  # Posizionamento a sinistra
        back_button = tk.Button(button_back_widget, text="⭠", font=("Arial", 18, "bold"),
                                bg="white", relief="flat", command=prenota_sezione)
        back_button.grid(row=0, column=0)

        frame_titolo_prenota = tk.Frame(window, bg="#f7f7f7", bd=5, relief="solid", padx=20, pady=20)
        frame_titolo_prenota.pack(pady=30, padx=30)

        titolo_prenota = tk.Label(frame_titolo_prenota, text="Prenotazione Sala", bg="#f7f7f7", font=("Helvetica", 24, "bold"), fg="#333")
        titolo_prenota.pack(pady=10)

        descrizione = sala_trovata["descrizione"]
        capienza = sala_trovata["capienza"]
        orario = sala_trovata["orario-occupato"]

        testo_sala = f"Sala: {descrizione}\nCapienza: {capienza} persone\nOrario: {orario}"
        conferma_label = tk.Label(frame_titolo_prenota, text=testo_sala, bg="#f7f7f7", font=("Arial", 16), fg="#555")
        conferma_label.pack(pady=20)

        conferma_btn = tk.Button(frame_titolo_prenota, text="Conferma Prenotazione", font=("Helvetica", 14), bg="#808080",  fg="white", relief="flat", width=20, height=2, command=dati_sala)
        conferma_btn.pack(pady=20)

        # Effetto hover
        conferma_btn.bind("<Enter>", lambda e: conferma_btn.config(bg="#778899", relief="raised"))
        conferma_btn.bind("<Leave>", lambda e: conferma_btn.config(bg="#808080", relief="flat"))
    else:
        errore_label = tk.Label(window, text="Sala non trovata. Riprova.", fg="red", bg="white")
        errore_label.pack(pady=10)


def prenota_sezione():
    #------------------------------------------------
    #|           [Seleziona la Data]                 |
    #|  (Calendario o input di data)                 |
    #------------------------------------------------
    #|                                              |
    #|   [Lista Sale Disponibili]                   |
    #|   Sala A - Capienza: 10 persone [Prenota]     |
    #|   Sala B - Capienza: 20 persone [Prenota]     |
    #|   Sala C - Capienza: 15 persone [Prenota]     |
    #|                                              |
    #------------------------------------------------
    #|      [Seleziona Orario]                       |
    #|  (Orario di inizio e fine)                   |
    #------------------------------------------------
    #|  [Conferma Prenotazione]                      |
    #------------------------------------------------
    #frame_test = tk.Frame(window, bg="white")
    #frame_test.pack(pady=20)

    #testo_di_conferma = tk.Label(frame_test, text="Test riuscito")
    #testo_di_conferma.grid(row=0, column=0, padx=10) 

    global frame_titolo_prenotazioni, frame_elenco_sale
    clear()

    button_back_widget = tk.Frame(window, bg="white")
    button_back_widget.pack(anchor="nw", padx=10, pady=10)  # Posizionamento a sinistra
    back_button = tk.Button(button_back_widget, text="⭠", font=("Arial", 18, "bold"),
                            bg="white", relief="flat", command=home)
    back_button.grid(row=0, column=0)

    frame_titolo_prenotazioni = tk.Frame(window, bg="white")
    frame_titolo_prenotazioni.pack(pady=20)

    titolo_prenotazione = tk.Label(frame_titolo_prenotazioni, text="Prenotazioni", bg="white", font=("Arial", 20))
    titolo_prenotazione.pack(pady=50)

    frame_elenco_sale = tk.Frame(window, bg="white")
    frame_elenco_sale.pack(pady=15)

    with open("sale.json", "r", encoding="utf-8") as file:
        sale = json.load(file)

    i = 0

    for sala in sale:   
        i += 1
        desc = sala["descrizione"]
        cap = sala["capienza"]
        occupata = sala["occupata"]
        orario = sala["orario-occupato"]
        occupata_da = sala["occupata_da"]
        btn_sala = tk.Button(frame_elenco_sale, text=f"{i}. Sala: {desc}; Capienza: {cap}; Occupata: {occupata}; Occupata da: {occupata_da}; Orario: {orario}", command=lambda s=sala: prenota_sala_ui(s))
        btn_sala.pack(pady=25)



    

def impostazioni():
    #------------------------------------------------
    #|              [Impostazioni]                  |
    #------------------------------------------------
    #|                                              |
    #|  [Modifica Profilo]                          |
    #|  [Notifiche]                                 |
    #|  [Lingua]                                    |
    #|  [Tema]                                      |
    #------------------------------------------------
    #|  [Logout]                                    |
    #------------------------------------------------
    #frame_test_2 = tk.Frame(window, bg="white")
    #frame_test_2.pack(pady=20)

    #testo_di_conferma = tk.Label(frame_test_2, text="Test riuscito")
    #testo_di_conferma.grid(row=0, column=0, padx=10) 
    
    clear()
    button_back_widget = tk.Frame(window, bg="white")
    button_back_widget.pack(anchor="nw", padx=10, pady=10)  # Posizionamento a sinistra
    back_button = tk.Button(button_back_widget, text="⭠", font=("Arial", 18, "bold"),
                            bg="white", relief="flat", command=home)
    back_button.grid(row=0, column=0)


def home():
    clear()

    button_exit_widget = tk.Frame(window, bg="white")
    button_exit_widget.pack(anchor="nw", padx=10, pady=10)  # Posizionamento a sinistra
    back_exit = tk.Button(button_exit_widget, text="X", font=("Arial", 18, "bold"),
                            bg="white", relief="flat", command=exit)
    back_exit.grid(row=0, column=0)

    global impostazioni, benvenuto, frame_bottoni, prenota
    # --- SEZIONE TITOLO ---
    benvenuto = tk.Label(window, text="Benvenuto!", font=("Arial", 16), bg="white")
    benvenuto.pack(pady=20) 

    # --- SEZIONE BOTTONI ---
    frame_bottoni = tk.Frame(window, bg="white")
    frame_bottoni.pack(pady=50)

    prenota = tk.Button(frame_bottoni, text="Prenota Sala", relief="raised", command=prenota_sezione)
    prenota.grid(row=0, column=0, padx=10) 

    impostazioni = tk.Button(frame_bottoni, text="Impostazioni", relief="raised", command=impostazioni)
    impostazioni.grid(row=0, column=1, padx=10)

home()
if __name__ == "__main__":
    window.mainloop()
