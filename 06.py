# Reio Viikmaa 06.02.25
# Ülesanne 6

import tkinter as tk


aken = tk.Tk()
aken.geometry("400x200")
font = "Arial 10"
padx = 5
pady = 5

nupp_00 = tk.Button(aken, text="Pildid", font=font)
nupp_00.grid(row=1, column=0, rowspan=5, columnspan=2, padx=padx, pady=pady, sticky="nsew")

#sildid
label = tk.Label(  text="Palun sisestage oma andmed:")
label.grid(row=0, column=2,columnspan=2, padx=padx, pady=pady, sticky="nsew")

nimi = tk.Label(text="Nimi")
nimi.grid(row=1, column=2, padx=padx, pady=pady, sticky="nsew")

nimi = tk.Label(text="Silmade värv")
nimi.grid(row=2, column=2, padx=padx, pady=pady, sticky="nsew")

nimi = tk.Label(text="Pikkus")
nimi.grid(row=3, column=2, padx=padx, pady=pady, sticky="nsew")

nimi = tk.Label(text="Kaal")
nimi.grid(row=4, column=2, padx=padx, pady=pady, sticky="nsew")

#sisestused
sis1 = tk.Entry()
sis1.grid(row=1, column=3, padx=padx, pady=pady, sticky="nsew")

sis2 = tk.Entry()
sis2.grid(row=2, column=3, padx=padx, pady=pady, sticky="nsew")

sis3 = tk.Entry()
sis3.grid(row=3, column=3, padx=padx, pady=pady, sticky="nsew")

sis4 = tk.Entry()
sis4.grid(row=4, column=3, padx=padx, pady=pady, sticky="nsew")

nupp_13 = tk.Button(aken, text="Salvesta", font=font)
nupp_13.grid(row=5, column=2, padx=padx, pady=pady, sticky="nsew")




# Nuppude seadistamine
aken.grid_rowconfigure(0, weight=1)
aken.grid_rowconfigure(1, weight=1)
aken.grid_rowconfigure(2, weight=1)
aken.grid_columnconfigure(0, weight=1)
aken.grid_columnconfigure(1, weight=1)
aken.grid_columnconfigure(2, weight=1)
aken.grid_columnconfigure(3, weight=1)

aken.mainloop()