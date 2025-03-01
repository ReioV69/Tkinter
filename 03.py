# Reio Viikmaa 04.02.25
# Ülesanne 3

import tkinter as tk

def main():
    aken = tk.Tk()
    aken.geometry("300x300")

    # Funktsioon, mis kuvab sisestused
    def kuva_sisestus():
        laenusumma = int(sisestus1.get())  # Võtab esimese sisestuse
        kuuintressimäär = float(sisestus2.get())/12/100  # Võtab teise sisestuse
        maksete_arv = int(sisestus3.get())*12  # Võtab kolmanda sisestuse
        igakuine_makse = laenusumma * kuuintressimäär / (1 - (1 + kuuintressimäär) ** -maksete_arv)
        print(f"Igakuine makse: {igakuine_makse:.2f}")
       
        # vastus = tk.Label(aken, text=f"Esimene sisestus: {tekst1}, Teine sisestus: {tekst2}, Kolmas sisestus: {tekst3}")
        # vastus.pack()
        
        
   
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