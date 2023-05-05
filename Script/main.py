# To install all the needed dependencies please run 'pip install -r dependencies.txt'
# To do .exe run 'pyinstaller --noconsole --add-data "warning.jpg;." --add-data "beep.mp3;." script/test_script.py --icon=owo_girl.png'
import requests, random, time, os, pygame, threading, sys, json
import tkinter as tk
from PIL import Image
from pathlib import Path
from tkinter import ttk
from tkinter import messagebox

# Save user given data to JSON file
def save_data_to_json():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    script_dir = os.path.join(parent_dir, "Saved_Data")

    if not os.path.exists(script_dir):
        os.makedirs(script_dir)

    json_path = os.path.join(script_dir, "data.json")

    data = {
        "HANDICAP": HANDICAP.get(),
        "HOLE_1": HOLE_1.get(),
        "HOLE_2": HOLE_2.get(),
        "HOLE_3": HOLE_3.get(),
        "HOLE_4": HOLE_4.get(),
        "HOLE_5": HOLE_5.get(),
        "HOLE_6": HOLE_6.get(),
        "HOLE_7": HOLE_7.get(),
        "HOLE_8": HOLE_8.get(),
        "HOLE_9": HOLE_9.get(),
        "HOLE_10": HOLE_10.get(),
        "HOLE_11": HOLE_11.get(),
        "HOLE_12": HOLE_12.get(),
        "HOLE_13": HOLE_13.get(),
        "HOLE_14": HOLE_14.get(),
        "HOLE_15": HOLE_15.get(),
        "HOLE_16": HOLE_16.get(),
        "HOLE_17": HOLE_17.get(),
        "HOLE_18": HOLE_18.get(),
    }

    with open(json_path, 'w') as file:
        json.dump(data, file)

    messagebox.showinfo("Importante!", "Datos guardados")

# Loads data from JSON files from Saved_Data folder
def load_data_from_json():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    script_dir = os.path.join(parent_dir, "Saved_Data")

    json_path = os.path.join(script_dir, "data.json")

    if os.path.exists(json_path):
        with open(json_path, 'r') as file:
            data = json.load(file)
    else:
        data = {
            "HANDICAP": "",
            "HOLE_1": "",
            "HOLE_2": "",
            "HOLE_3": "",
            "HOLE_4": "",
            "HOLE_5": "",
            "HOLE_6": "",
            "HOLE_7": "",
            "HOLE_8": "",
            "HOLE_9": "",
            "HOLE_10": "",
            "HOLE_11": "",
            "HOLE_12": "",
            "HOLE_13": "",
            "HOLE_14": "",
            "HOLE_15": "",
            "HOLE_16": "",
            "HOLE_17": "",
            "HOLE_18": "",
        }

    return data


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def print_to_text_widget(text):
    output_text.insert(tk.END, text + '\n')
    output_text.see(tk.END)

#----------------------------------------------------------#
# Main script
def run_script():
    data = load_data_from_json()
    HANDICAP = data["HANDICAP"]
    HOLE_1 = data["HOLE_1"]

    # Pago Chico user scores
    PagoChico_scores = [HOLE_1]
    # Pago Chico par scores
    PagoChico_pars = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

    # Count variables init
    Hen1Count, AlbCount, BirdieCount, ParCount, BogeyCount, DobleBCount , TripleBCount , CuadrupleBCount = 0
    
    # Calculations
    for hole_score, hole_par in zip(PagoChico_scores, PagoChico_pars):
        difference = hole_score - hole_par
        if difference == 1:
            Hen1Count += 1
        elif difference == -2:
            AlbCount += 1
        elif difference == -1:
            BirdieCount += 1
        elif difference == 0:
            ParCount += 1
        elif difference == 1:
            BogeyCount += 1
        elif difference == 2:
            DobleBCount += 1
        elif difference == 3:
            TripleBCount += 1
        elif difference == 4:
            CuadrupleBCount += 1

    print_to_text_widget('     -------------------------------------------------      ')
    print_to_text_widget('                                                            ')         
    print_to_text_widget(f'      Bienvenido al contador de Golf {firstName} {lastName}')
    print_to_text_widget('                                                            ') 
    print_to_text_widget('     -------------------------------------------------      ')
    print_to_text_widget('                                                            ')
    print_to_text_widget(f'    Tu handicap es {HANDICAP}                              ')
    print_to_text_widget(f'    Hoyo en 1 = {Hen1Count}                                ')
    print_to_text_widget(f'    Albatros = {AlbCount}                                  ')
    print_to_text_widget(f'    Birdies =  {BirdieCount}                               ')
    print_to_text_widget(f'    Par =  {ParCount}                                      ')
    print_to_text_widget(f'    Bogey =  {BogeyCount}                                  ')
    print_to_text_widget(f'    Doble Bogey =  {DobleBCount}                           ')
    print_to_text_widget(f'    Triple Bogey =  {TripleBCount}                         ')
    print_to_text_widget(f'    Cuadruple Bogey =  {CuadrupleBCount}                   ')

def errase_script():
    print("still working on this part")

#-----------------------------------------------------------#
def stop_script():
    root.destroy()
    sys.exit(0)

# GUI starts here
root = tk.Tk()
root.title("Contador de Golf")
root.geometry("1200x800")

data = load_data_from_json()

# Variables
HANDICAP= tk.StringVar(value=data["HANDICAP"])
HOLE_1= tk.StringVar(value=data["HOLE_1"])
HOLE_2= tk.StringVar(value=data["HOLE_2"])
HOLE_3= tk.StringVar(value=data["HOLE_3"])
HOLE_4= tk.StringVar(value=data["HOLE_4"])
HOLE_5= tk.StringVar(value=data["HOLE_5"])
HOLE_6= tk.StringVar(value=data["HOLE_6"])
HOLE_7= tk.StringVar(value=data["HOLE_7"])
HOLE_8= tk.StringVar(value=data["HOLE_8"])
HOLE_9= tk.StringVar(value=data["HOLE_9"])
HOLE_11= tk.StringVar(value=data["HOLE_10"])
HOLE_10= tk.StringVar(value=data["HOLE_11"])
HOLE_12= tk.StringVar(value=data["HOLE_12"])
HOLE_13= tk.StringVar(value=data["HOLE_13"])
HOLE_14= tk.StringVar(value=data["HOLE_14"])
HOLE_15= tk.StringVar(value=data["HOLE_15"])
HOLE_16= tk.StringVar(value=data["HOLE_16"])
HOLE_17= tk.StringVar(value=data["HOLE_17"])
HOLE_18= tk.StringVar(value=data["HOLE_18"])

# Labels
ttk.Label(root, text="Handicap:").grid(column=0, row=0, padx=1, pady=3, sticky=tk.W)
ttk.Label(root, text="Hoyo 1:").grid(column=0, row=1, padx=1, pady=3, sticky=tk.W)
ttk.Label(root, text="Hoyo 2:").grid(column=0, row=2, padx=1, pady=3, sticky=tk.W)
ttk.Label(root, text="Hoyo 3:").grid(column=0, row=3, padx=1, pady=3, sticky=tk.W)
ttk.Label(root, text="Hoyo 4:").grid(column=0, row=4, padx=1, pady=3, sticky=tk.W)
ttk.Label(root, text="Hoyo 5:").grid(column=0, row=5, padx=1, pady=3, sticky=tk.W)
ttk.Label(root, text="Hoyo 6:").grid(column=0, row=6, padx=1, pady=3, sticky=tk.W)
ttk.Label(root, text="Hoyo 7:").grid(column=0, row=7, padx=1, pady=3, sticky=tk.W)
ttk.Label(root, text="Hoyo 8:").grid(column=0, row=8, padx=1, pady=3, sticky=tk.W)
ttk.Label(root, text="Hoyo 9:").grid(column=0, row=9, padx=1, pady=3, sticky=tk.W)
ttk.Label(root, text="Hoyo 10:").grid(column=1, row=1, padx=1, pady=3, sticky=tk.W)
ttk.Label(root, text="Hoyo 11:").grid(column=1, row=2, padx=1, pady=3, sticky=tk.W)
ttk.Label(root, text="Hoyo 12:").grid(column=1, row=3, padx=1, pady=3, sticky=tk.W)
ttk.Label(root, text="Hoyo 13:").grid(column=1, row=4, padx=1, pady=3, sticky=tk.W)
ttk.Label(root, text="Hoyo 14:").grid(column=1, row=5, padx=1, pady=3, sticky=tk.W)
ttk.Label(root, text="Hoyo 15:").grid(column=1, row=6, padx=1, pady=3, sticky=tk.W)
ttk.Label(root, text="Hoyo 16:").grid(column=1, row=7, padx=1, pady=3, sticky=tk.W)
ttk.Label(root, text="Hoyo 17:").grid(column=1, row=8, padx=1, pady=3, sticky=tk.W)
ttk.Label(root, text="Hoyo 18:").grid(column=1, row=9, padx=1, pady=3, sticky=tk.W)

# Entry widgets
ttk.Entry(root, textvariable=HANDICAP, width=3).grid(column=0, row=0, padx=60, pady=3, sticky=tk.W)
ttk.Entry(root, textvariable=HOLE_1, width=3).grid(column=0, row=1, padx=60, pady=3, sticky=tk.W)
ttk.Entry(root, textvariable=HOLE_2, width=3).grid(column=0, row=2, padx=60, pady=3, sticky=tk.W)
ttk.Entry(root, textvariable=HOLE_3, width=3).grid(column=0, row=3, padx=60, pady=3, sticky=tk.W)
ttk.Entry(root, textvariable=HOLE_4, width=3).grid(column=0, row=4, padx=60, pady=3, sticky=tk.W)
ttk.Entry(root, textvariable=HOLE_5, width=3).grid(column=0, row=5, padx=60, pady=3, sticky=tk.W)
ttk.Entry(root, textvariable=HOLE_6, width=3).grid(column=0, row=6, padx=60, pady=3, sticky=tk.W)
ttk.Entry(root, textvariable=HOLE_7, width=3).grid(column=0, row=7, padx=60, pady=3, sticky=tk.W)
ttk.Entry(root, textvariable=HOLE_8, width=3).grid(column=0, row=8, padx=60, pady=3, sticky=tk.W)
ttk.Entry(root, textvariable=HOLE_9, width=3).grid(column=0, row=9, padx=60, pady=3, sticky=tk.W)
ttk.Entry(root, textvariable=HOLE_10, width=3).grid(column=1, row=1, padx=60, pady=3, sticky=tk.W)
ttk.Entry(root, textvariable=HOLE_11, width=3).grid(column=1, row=2, padx=60, pady=3, sticky=tk.W)
ttk.Entry(root, textvariable=HOLE_12, width=3).grid(column=1, row=3, padx=60, pady=3, sticky=tk.W)
ttk.Entry(root, textvariable=HOLE_13, width=3).grid(column=1, row=4, padx=60, pady=3, sticky=tk.W)
ttk.Entry(root, textvariable=HOLE_14, width=3).grid(column=1, row=5, padx=60, pady=3, sticky=tk.W)
ttk.Entry(root, textvariable=HOLE_15, width=3).grid(column=1, row=6, padx=60, pady=3, sticky=tk.W)
ttk.Entry(root, textvariable=HOLE_16, width=3).grid(column=1, row=7, padx=80, pady=3, sticky=tk.W)
ttk.Entry(root, textvariable=HOLE_17, width=3).grid(column=1, row=8, padx=80, pady=3, sticky=tk.W)
ttk.Entry(root, textvariable=HOLE_18, width=3).grid(column=1, row=9, padx=80, pady=3, sticky=tk.W)

# Add a text widget to the output
output_text = tk.Text(root, wrap=tk.WORD, height=15, width=60)
output_text.grid(column=0, row=11, columnspan=1, padx=60, pady=20, sticky=tk.W)

# Add a scrollbar to the text widget
scrollbar = ttk.Scrollbar(root, command=output_text.yview)
scrollbar.grid(column=2, row=11, padx=(0, 10), pady=10, sticky=tk.N+tk.S)
output_text.config(yscrollcommand=scrollbar.set)

# Save button
ttk.Button(root, text="Guardar datos", command=save_data_to_json).grid(column=0, row=10, padx=65, pady=5, sticky=tk.W)
ttk.Button(root, text="Calcular", command=lambda: threading.Thread(target=run_script).start()).grid(column=0, row=10, padx=263, pady=5, sticky=tk.W)
ttk.Button(root, text="Exit", command=stop_script).grid(column=10, row=6, padx=465, pady=5, sticky=tk.W)

# Run the application
root.mainloop()