import tkinter as tk
import json

window = tk.Tk()
window.geometry("1200x600")
window.title("Hello TkInter!")
window.configure(background="white")

def clear():
    benvenuto.destroy()
    frame_bottoni.destroy()
    prenota.destroy()
    impostazioni.destroy()

# --- FUNZIONI ---
def prenota_sezione():
    #TODO: Cancella schermata
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

    # TODO: Christian controlla la gestione per le sale nel json.

    with open("sale.json", "r", encoding="utf-8") as file:
        sale = json.load(file)

    print(sale)


    

def impostazioni():
    #TODO: Cancella schermata
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
