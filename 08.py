import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from PIL import Image, ImageOps
import os

filename = "Vali enne fail"
thumb_directory = 'img/thumb'

def open_file():
    global filename
    documents_path = Path.home() / "Desktop"
    filename = filedialog.askopenfilename(
        initialdir=documents_path,
        filetypes=(
            ("Pythoni failid", ("*.jpg", "*.jpeg", "*.jfif")),
            ("Kõik failid", "*.*")
        ),
        title="Vali failikene"
    )
    if filename:
        inputtxt.insert(tk.END,filename)
        file_label.config(text=f"Valitud fail: {filename}")
    else:
        file_label.config(text="Faili ei valitud.")

def save_directory():
    source_directory = os.path.dirname(filename)
    thumb_directory = 'img/thumb'
        
    # # Kontrolli, kas thumb kataloog on olemas, kui ei ole, siis loo see
    # if not os.path.exists(thumb_dir):
    #     os.makedirs(thumb_dir)

    # # Kõikide JPG failide leidmine kataloogis
    # for filename in os.listdir(source_dir):
    #     if filename.lower().endswith(".jpg"):
    #         img_path = (open_file)
    #         img = Image.open(img_path)
           
    #         # Pisipildi loomine
    #         thumb_img = ImageOps.fit(img, size, centering=(0.5, 0.5))
    #         img.close()
           
    #         # Pisipildi salvestamine
    #         thumb_path = os.path.join(thumb_dir, filename)
    #         thumb_img.save(thumb_path, "JPEG")
           
    #         print(f"Pisipilt salvestatud: {thumb_path}")


aken = tk.Tk()
aken.title("Peamine aken")
aken.geometry("450x400")

label = tk.Label(aken, text="Pildi suurus 200x200", font="Arial 24")
label.pack(pady=10)

inputtxt = tk.Text(aken, height=10, width=50)
inputtxt.pack(pady=10)

salvesta_pildid = tk.Button(aken, text="Salvesta pildid", command=save_directory)
salvesta_pildid.pack(pady=10, side="bottom")

open_button = tk.Button(aken, text="Vali failid", command=open_file)
open_button.pack(pady=10, side="bottom")

file_label = tk.Label(aken, text="")
file_label.pack(pady=10)


aken.mainloop()