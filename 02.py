# Reio Viikmaa  04.02.25
# Ülesanne 2

import tkinter as tk
from PIL import Image, ImageTk
import ctypes
def loe_fail(failinimi):
    with open(failinimi, 'r', encoding='utf-8') as file:
        return file.read()
    
def main():
    # DPI teadlikkuse seadistamine kõrge DPI ekraanide jaoks
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception as e:
        print(e)

    aken = tk.Tk()
    aken.title("Reio ülesanded")
    aken.geometry("400x400")
    aken.resizable(False, True)

    pilt = Image.open("Allalaaditud fail.jfif")
    foto = ImageTk.PhotoImage(pilt)
    


    label = tk.Label(aken, text="Michael Jackson", font=("Arial", 16, "bold"), fg="blue").pack()
   
    label = tk.Label(aken, image=foto)
    label.image = foto
    label.pack()
    #Tekst
    tekst = tk.Text(aken, wrap=tk.WORD, font=("Arial", 12, "bold"), fg="blue")
    scrollbar = tk.Scrollbar(aken, command=tekst.yview)
    tekst.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tekst.pack(expand=True, fill=tk.BOTH)

    failisisu = loe_fail("tekst.txt")
    tekst.insert(tk.INSERT, failisisu)
    button = tk.Button(aken, text="Sulge", command=aken.destroy).pack()
    
    aken.mainloop()

if __name__ == "__main__":
    main()