# Reio Viikmaa  04.02.25
# Ülesanne 1

import tkinter as tk
import ctypes

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
   
    label = tk.Label(aken, text="Tere, maailm!").pack()
    button = tk.Button(aken, text="Sulge", command=aken.destroy).pack()
   
    aken.mainloop()

if __name__ == "__main__":
    main()