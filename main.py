# AUTORE: Christian Lancini
# Data inizio sviluppo: 9/11/25


import tkinter as tk
import json

window = tk.Tk()
window.geometry("1200x700")
window.title("Gestione di prenotazione")
window.configure(background="white")

# --- FUNZIONI ---

def clear():
    benvenuto.destroy()
    frame_bottoni.destroy()
    prenota.destroy()
    impostazioni.destroy()

def prenota_sala(sala_selezionata):
    #! BUG: I Button quando premuti non funzionano, cercare un metodo per cercare la sala giusta

    with open("sale.json", "r", encoding="utf-8") as file:
        sale_data = json.load(file) 

    sala_trovata = None
    for s in sale_data:
        if s["descrizione"] == sala_selezionata["descrizione"]:
            sala_trovata = s
            break
    
    if sala_trovata:
        clear()
        
        frame_titolo_prenota = tk.Frame(window, bg="white")
        frame_titolo_prenota.pack(pady=20)
        titolo_prenota = tk.Label(frame_titolo_prenota, text="Prenotazione Sala", bg="white", font=("Arial", 20))
        titolo_prenota.pack(pady=50)

        descrizione = sala_trovata["descrizione"]
        capienza = sala_trovata["capienza"]
        orario = sala_trovata["orario-occupato"]
        
        testo_sala = f"Sala: {descrizione}\nCapienza: {capienza} persone\nOrario: {orario}"
        conferma_label = tk.Label(frame_titolo_prenota, text=testo_sala, bg="white", font=("Arial", 16))
        conferma_label.pack(pady=20)

        conferma_btn = tk.Button(frame_titolo_prenota, text="Conferma Prenotazione", command=lambda s=sala_trovata: conferma_prenotazione(s))
        conferma_btn.pack(pady=20)

    else:
        # Se la sala non viene trovata
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

    clear()

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
        btn_sala = tk.Button(frame_elenco_sale, text=f"{i}. Sala: {desc}; Capienza: {cap}; Occupata: {occupata}; Occupata da: {occupata_da}; Orario: {orario}", command=lambda s=sala: prenota_sala(s))
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
    #TODO: Creare schermata impostazioni

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

if __name__ == "__main__":
    window.mainloop()
