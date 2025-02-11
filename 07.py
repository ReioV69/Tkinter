import tkinter as tk



def valideeriTeksti(*args):
    text = entry_var.get()
    if len(text) == 11:
        if int(text[0])%2==0:
            sugu = "Naine"
        else:
            sugu = "Mees"
        sp = f"{text[5]}{text[6]}.{text[3]}{text[4]}.{text[1]}{text[2]}"
        label1 = tk.Label(text=f"Sugu: {sugu}",fg="green").pack()
        label = tk.Label(text=f"sünniaeg: {sp}", fg="green").pack()
    else:
        validation_label.config(text="Sisesta vähemalt 5 märki!", fg="red")

aken = tk.Tk()
aken.title("Validaator")
aken.geometry("400x400")

label = tk.Label(aken, text="isikukood", font="Arial 16").pack(pady=(10,0))

entry_var = tk.StringVar()
entry_var.trace_add("write", valideeriTeksti)

entry = tk.Entry(aken, textvariable=entry_var)
entry.pack()

validation_label = tk.Label(aken, text="Sisesta vähemalt 5 märki!", fg="red")
validation_label.pack()

aken.mainloop()