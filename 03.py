# Reio Viikmaa 04.02.25
# Ülesanne 3

import tkinter as tk

def main():
    aken = tk.Tk()
    aken.geometry("300x300")

    # Funktsioon, mis kuvab sisestused
    def kuva_sisestus():
        tekst1 = sisestus1.get()  # Võtab esimese sisestuse
        tekst2 = sisestus2.get()  # Võtab teise sisestuse
        tekst3 = sisestus3.get()  # Võtab kolmanda sisestuse
        # vastus = tk.Label(aken, text=f"Esimene sisestus: {tekst1}, Teine sisestus: {tekst2}, Kolmas sisestus: {tekst3}")
        vastus = tk.Label(aken, text=f"Igakuine_makse: {tekst1})")
        vastus.pack()
        igakuine_makse = ([sisestus1] * [sisestus2] / (1 - (1 + [sisestus2]) ** -[sisestus3]))
    # Esimene sisestusväli
    sisestus1 = label = tk.Label(aken, text="Laenusumma (€):").pack()
    sisestus1 = tk.Entry(aken)
    sisestus1.pack()
    
   
    # Teine sisestusväli
    sisestus2 = label = tk.Label(aken, text="Aastane intressimäär (%):").pack()
    sisestus2 = tk.Entry(aken)
    sisestus2.pack()
    
    sisestus3 = label = tk.Label(aken, text="Laenuperiood (aastates): ").pack()
    sisestus3 = tk.Entry(aken)
    sisestus3.pack()
   
   
    # Nupp, mis käivitab funktsiooni kuva_sisestus
    nupp = tk.Button(aken, text="Arvuta", command=kuva_sisestus)
    nupp.pack()

    aken.mainloop()

if __name__ == "__main__":
    main()