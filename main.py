# AUTORE: Christian Lancini
# Data inizio sviluppo: 9/11/25
# Versione: 1.0 (16/11/25)

import tkinter as tk
import json
from plyer import notification

window = tk.Tk()
window.geometry("1200x700")
window.title("Gestione di prenotazione")
window.configure(background="white")

# OTTIMIZZAZIONE
def hover_effect(button, bg_color, relief_style):
    button.config(bg=bg_color, relief=relief_style)

def applica_hover(button):
    button.bind("<Enter>", lambda e: hover_effect(button, "#778899", "raised"))
    button.bind("<Leave>", lambda e: hover_effect(button, "#808080", "flat"))

# --- FUNZIONI ---
def clear():
    for widget in window.winfo_children():
        widget.pack_forget()
        widget.grid_forget()
        widget.place_forget()


def invia_dati(utente, h_inizio, h_fine, sala):
    clear() 
    #* Usa .get() per i input
    button_back_widget = tk.Frame(window, bg="white")
    button_back_widget.pack(anchor="nw", padx=10, pady=10)  # Posizionamento a sinistra
    back_button = tk.Button(button_back_widget, text="⭠", font=("Arial", 18, "bold"),
                                bg="white", relief="flat", command=prenota_sezione)
    back_button.grid(row=0, column=0)

    success_widget = tk.Frame(window, bg="white")
    success_widget.pack(padx=20, pady=20)

    success_text = tk.Label(success_widget, bg="white", text="Prenotazione avvenuta con successo!", font=("Arial", 16, "bold"))
    success_text.pack(pady=10)

    if check_notifiche() == "true":
            notification.notify(
            title=f"Sala prenotata '{sala['nome']}'",
            message='La sala è stata prenotata correttamente',
            timeout=10 
        )
    else:
        pass

    try:
        with open('sale.json', 'r') as file:
            sale = json.load(file)

        for s in sale:
            if s['nome'] == sala['nome']:
                s['occupata'] = True
                s['orario-occupato'] = f"{h_inizio} - {h_fine}"  
                s['occupata_da'] = utente  
                break

        with open('sale.json', 'w') as file:
            json.dump(sale, file, indent=4)

    except FileNotFoundError as e:
        print(f"Errore: il file sale.json non è stato trovato. {e}")
  
def dati_sala(sala):
    clear()

    button_back_widget = tk.Frame(window, bg="white")
    button_back_widget.pack(anchor="nw", padx=10, pady=10)  # Posizionamento a sinistra
    back_button = tk.Button(button_back_widget, text="⭠", font=("Arial", 18, "bold"),
                                bg="white", relief="flat", command=prenota_sezione)
    back_button.grid(row=0, column=0)

    info_widget = tk.Frame(window, bg="white")
    info_widget.pack(padx=20, pady=20)

    utente_text = tk.Label(info_widget, bg="white", text="Nome & Cognome: ")
    utente_text.pack(pady=10)
    utente = tk.Entry(info_widget, width=30)
    utente.pack(pady=10)

    h_inizio_text = tk.Label(info_widget, bg="white", text="Inserisci ora di inizio (HH:MM): ")
    h_inizio_text.pack(pady=10)
    h_inizio = tk.Entry(info_widget, width=30)
    h_inizio.pack(pady=10)

    h_fine_text = tk.Label(info_widget, bg="white", text="Inserisci ora di fine (HH:MM): ")
    h_fine_text.pack(pady=10)
    h_fine = tk.Entry(info_widget, width=30)
    h_fine.pack(pady=10)

    button = tk.Button(info_widget, text="Conferma prenotazione", command=lambda: invia_dati(utente.get(), h_inizio.get(), h_fine.get(), sala))
    button.pack(pady=10)




def prenota_sala_ui(sala_selezionata):
    with open("sale.json", "r", encoding="utf-8") as file:
        sale_data = json.load(file)

    sala_trovata = None
    for s in sale_data:
        if s["descrizione"] == sala_selezionata["descrizione"]:
            sala_trovata = s
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

        conferma_btn = tk.Button(frame_titolo_prenota, text="Conferma Prenotazione", font=("Helvetica", 14), bg="#808080",  fg="white", relief="flat", width=20, height=2, command=lambda: dati_sala(sala_selezionata))
        conferma_btn.pack(pady=20)

        # Effetto hover
        applica_hover(conferma_btn)
    else:
        errore_label = tk.Label(window, text="Sala non trovata. Riprova.", fg="red", bg="white")
        errore_label.pack(pady=10)

def occupata_sala():
    clear()
    button_back_widget = tk.Frame(window, bg="white")
    button_back_widget.pack(anchor="nw", padx=10, pady=10)  # Posizionamento a sinistra
    back_button = tk.Button(button_back_widget, text="⭠", font=("Arial", 18, "bold"),
                            bg="white", relief="flat", command=prenota_sezione)
    back_button.grid(row=0, column=0)

    occupata_widget = tk.Frame(window, bg="white")
    occupata_widget.pack(pady=25)

    occupata_text = tk.Label(occupata_widget, bg="white", text="Sala Occupata", font=("Arial", 20))
    occupata_text.pack(pady=25)


def prenota_sezione():
    global frame_titolo_prenotazioni, frame_elenco_sale
    clear()

    button_back_widget = tk.Frame(window, bg="white")
    button_back_widget.pack(anchor="nw", padx=10, pady=10)  # Posizionamento a sinistra
    back_button = tk.Button(button_back_widget, text="⭠", font=("Arial", 18, "bold"),
                            bg="white", relief="flat", command=home)
    back_button.grid(row=0, column=0)

    frame_titolo_prenotazioni = tk.Frame(window, bg="white")
    frame_titolo_prenotazioni.pack(pady=20)

    titolo_prenotazione = tk.Label(frame_titolo_prenotazioni, text="PRENOTA", bg="white", font=("Arial", 20))
    titolo_prenotazione.pack(pady=50)

    frame_elenco_sale = tk.Frame(window, bg="white")
    frame_elenco_sale.pack(pady=15)

    with open("sale.json", "r", encoding="utf-8") as file:
        sale = json.load(file)

    i = 0

    for sala in sale:   
        i += 1
        nome = sala["nome"]
        cap = sala["capienza"]
        occupata = sala["occupata"]
        orario = sala["orario-occupato"]
        occupata_da = sala["occupata_da"]

        if occupata == True:
            btn_sala = tk.Button(frame_elenco_sale, 
                            text=f"{i}. Sala: {nome}; Occupata da: {occupata_da}; Orario: {orario}", 
                            command=occupata_sala,
                            bg="red", fg="white", relief="flat", width=100, height=2)
        
            btn_sala.pack(pady=25)

        else:
            btn_sala = tk.Button(frame_elenco_sale, 
                                text=f"{i}. Sala: {nome}; Capienza: {cap}", 
                                command=lambda s=sala: prenota_sala_ui(s),
                                bg="#808080", fg="white", relief="flat", width=100, height=2)
            
            btn_sala.pack(pady=25)
        
            applica_hover(btn_sala)

def check_notifiche():
    try:
        with open('notifiche.txt', 'r') as file:
            contenuto = file.read()
            if "true" in contenuto:
                return "true"
            else:
                return "false"
    except FileNotFoundError:
        with open('notifiche.txt', 'w') as file:
            file.write('false')
        return "false"


def attiva_notifiche():
    with open('notifiche.txt', 'r') as file:
        contenuto = file.read()

        if "false" in contenuto:
            with open('notifiche.txt', 'w') as file:
                contenuto = 'true'
                file.write(contenuto)
            if check_notifiche() == "true":
                    notification.notify(
                    title=f"Notifiche Attivate",
                    timeout=10 
                )
            else:
                pass
        elif "true" in contenuto:
            print("Notifiche già avviate")
        else:
            print("Dispositivo alterato, recupero del file...")
            with open('notifiche.txt', 'w') as file:
                contenuto = 'true'
                file.write(contenuto)

def disattiva_notifiche():
    with open('notifiche.txt', 'r') as file:
        contenuto = file.read()

        if "false" in contenuto:
            print("Notifiche già disattivate")
        elif "true" in contenuto:
            with open('notifiche.txt', 'w') as file:
                contenuto = 'false'
                file.write(contenuto)
            
            if check_notifiche() == "false":
                    notification.notify(
                    title=f"Notifiche da ora disattivate",
                    timeout=10 
                )
            else:
                pass
        else:
            print("Dispositivo alterato, recupero del file...")
            with open('notifiche.txt', 'w') as file:
                contenuto = 'false'
                file.write(contenuto)

def impostazioni():
    #|  [Lingua]                      |
    #|  [Tema]                        |
    
    clear()
    button_back_widget = tk.Frame(window, bg="white")
    button_back_widget.pack(anchor="nw", padx=10, pady=10)  # Posizionamento a sinistra
    back_button = tk.Button(button_back_widget, text="⭠", font=("Arial", 18, "bold"),
                            bg="white", relief="flat", command=home)
    back_button.grid(row=0, column=0)

    titolo_widget = tk.Frame(window, bg="white")
    titolo_widget.pack(pady=20)

    titolo_impostazioni = tk.Label(titolo_widget, bg="white", text="IMPOSTAZIONI", font=("Arial", 20))
    titolo_impostazioni.pack(pady=20)

    notifiche_widget = tk.Frame(window, bg="white")
    notifiche_widget.pack(pady=20)

    notifiche_text = tk.Label(notifiche_widget, bg="white", text="Notifiche:")
    notifiche_text.pack(pady=20)

    notifiche_button = tk.Button(text="Attiva Notifiche", command=attiva_notifiche, bg="#808080", fg="white", relief="flat", width=100, height=2)
    notifiche_button.pack(pady=20)

    notifiche_button_dis = tk.Button(text="Disattiva Notifiche", command=disattiva_notifiche, bg="#808080", fg="white", relief="flat", width=100, height=2)
    notifiche_button_dis.pack(pady=20)

    applica_hover(notifiche_button)
    applica_hover(notifiche_button_dis)

def home():
    clear()

    button_exit_widget = tk.Frame(window, bg="white")
    button_exit_widget.pack(anchor="nw", padx=10, pady=10)  # Posizionamento a sinistra
    back_exit = tk.Button(button_exit_widget, text="X", font=("Arial", 18, "bold"),
                            bg="white", relief="flat", command=window.quit)
    back_exit.grid(row=0, column=0)

    # --- SEZIONE TITOLO ---
    benvenuto = tk.Label(window, text="Benvenuto!", font=("Arial", 20), bg="white")
    benvenuto.pack(pady=20) 

    # --- SEZIONE BOTTONI ---
    frame_bottoni = tk.Frame(window, bg="white")
    frame_bottoni.pack(pady=50)

    prenota_btn = tk.Button(frame_bottoni, text="Prenota Sala", relief="raised", command=prenota_sezione, bg="#808080", fg="white", width=20, height=2)
    prenota_btn.grid(row=0, column=0, padx=10) 

    impostazioni_btn = tk.Button(frame_bottoni, text="Impostazioni", relief="raised", command=impostazioni, bg="#808080", fg="white", width=20, height=2)
    impostazioni_btn.grid(row=0, column=1, padx=10)

    # Bind hover events
    applica_hover(prenota_btn)
    applica_hover(impostazioni_btn)


home()

if __name__ == "__main__":
    window.mainloop()