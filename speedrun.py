# ===============================================================
# IMPORT LIBRARIES
# ===============================================================
from colorama import Fore, Style, init
from PIL import Image, ImageTk
import tkinter as tk
import subprocess
import webbrowser
import os
import re
import json
import math
import customtkinter 

# =========== [ version type json ] =========== #
with open("version.json", "r") as file:
    data = json.load(file)

# ===============================================================
# VARIABEL
# ===============================================================

# INFO = Fore.BLUE + "INFO" + Style.RESET_ALL 
# DONE = Fore.GREEN + "DONE" + Style.RESET_ALL 
# WARNING = Fore.RED + "WARNING" + Style.RESET_ALL

INFO =  "INFO"
DONE =  "DONE"
WARNING =  "WARNING"

entry_width = 160
option_width = 160
entry_border_width = 0
entry_border_color = "#fff"
option_button_color = "#000"
string = "Hello world" 
print(f"[{INFO}] Finis variabel")

# ===============================================================
# MAIN WINDOW SETUP
# ===============================================================
app = customtkinter.CTk()
app.title("Locate Structure MC")
app.configure(bg="#111111")
# app.geometry("420x250")
app.resizable(False, False)
app.iconbitmap("icon.ico")
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
print(f"[{INFO}] Finis main windows setup")

# ===============================================================
# FUNCTION
# ===============================================================
def close_window():
    root.destroy()

def minimize_window():
    root.iconify()

def toggle_maximize():
    global is_maximized, old_geometry
    if not is_maximized:
        old_geometry = root.geometry()
        root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
        is_maximized = True
    else:
        root.geometry(old_geometry)
        is_maximized = False

# ---------- Fungsi Drag Window ----------
def start_move(event):
    root.x = event.x
    root.y = event.y

def stop_move(event):
    root.x = None
    root.y = None

def on_motion(event):
    deltax = event.x - root.x
    deltay = event.y - root.y
    x = root.winfo_x() + deltax
    y = root.winfo_y() + deltay
    root.geometry(f"+{x}+{y}")



# ============= [ Frame ] =============

frame = customtkinter.CTkFrame(app, fg_color="#222", corner_radius=0)
frame.pack(fill="x", padx=0, pady=0)

button_frame = customtkinter.CTkFrame(app, fg_color="#000", corner_radius=0)
button_frame.pack(fill="x", pady=0)

output_frame = customtkinter.CTkFrame(app, fg_color="#111", corner_radius=0)
output_frame.pack(fill="both", expand=True)

# -------- [ row : 0 ] -------- # 

label_font = customtkinter.CTkFont(family="Minecraft", size=12 )
label_output_font = customtkinter.CTkFont(family="Minecraft", size=13)

# INPUT : Seed
customtkinter.CTkLabel(frame, text="Seed",  font=label_font, anchor="w").grid(row=0, column=0, padx=5, sticky="w")

seed = customtkinter.StringVar(value="1234567890")
entry_seed = customtkinter.CTkEntry(
    frame,
    textvariable=seed,
    width=entry_width,
    fg_color="#000",
    corner_radius=0,
    border_width=entry_border_width,
    border_color=entry_border_color,
    font=label_font
)
entry_seed.grid(row=0, column=1, pady=0, padx=0)

# INPUT : version
customtkinter.CTkLabel(frame, text="Version",font=label_font, anchor="w").grid(row=0, column=2, padx=5, sticky="nswe")

version_values = []
for i in range(len(data["OptionMenu"])):
    version_values.append(data["OptionMenu"][i]["minecraft"])

optionmenu_version = customtkinter.StringVar(value="1.16")
optionmenu_version_widget = customtkinter.CTkOptionMenu(
    frame,
    values=version_values,
    variable=optionmenu_version,
    width=100,       
    height=26,        
    corner_radius=0,  
    fg_color=option_button_color, 
    button_color=option_button_color,
    button_hover_color="#222",
    text_color="#FFF",
    font=label_font 
)
optionmenu_version_widget.grid(row=0, column=3, padx=5, pady=3, sticky="w")

# -------- [ row : 1 ] -------- # 

# INPUT : Structure
customtkinter.CTkLabel(frame, text="Structure", font=label_font, anchor="w").grid(row=1, column=0, padx=5, sticky="w")

Structure_value = ["bastion", "fortress", "stronghold"]
optionmenu_structure = customtkinter.StringVar(value="bastion")
structure = customtkinter.CTkOptionMenu(
    frame,
    values=Structure_value,
    variable=optionmenu_structure,
    width=option_width,
    height=26,
    corner_radius=0,
    fg_color=option_button_color,   
    button_color=option_button_color,
    button_hover_color="#222",
    text_color="#FFF",
    font=label_font)
structure.grid(row=1, column=1, padx=5, pady=3, sticky="w")

# INPUT : Dimension
customtkinter.CTkLabel(frame, text="Dimension", font=label_font, anchor="w").grid(row=1, column=2, padx=5, sticky="W")

dimensions = ["overworld", "nether", "the_end"]
optionmenu_dimension = customtkinter.StringVar(value="nether")
dimension = customtkinter.CTkOptionMenu(
    frame,values=dimensions, 
    variable=optionmenu_dimension, 
    width=100,      
    height=26,       
    corner_radius=0,  
    fg_color=option_button_color,  
    button_color=option_button_color,
    button_hover_color="#222",
    text_color="#FFF",
    font=label_font)
dimension.grid(row=1, column=3, padx=5, pady=3, sticky="w")

# -------- [ row : 2 ] -------- # 

# INPUT : Jarak Min
customtkinter.CTkLabel(frame, text="Jarak Min", font=label_font, anchor="w").grid(row=2, column=0, pady=5, padx=5, sticky="w")

block_min = customtkinter.StringVar(value="0")
entry_min = customtkinter.CTkEntry(frame,textvariable=block_min, width=entry_width, fg_color="#000", text_color="#fff", font=label_font, corner_radius=0, border_width=entry_border_width, border_color=entry_border_color)
entry_min.grid(row=2, column=1, pady=5)

# INPUT : Jarak Max
customtkinter.CTkLabel(frame, text="Jarak Max", font=label_font, anchor="w").grid(row=2, column=2, pady=5, padx=5, sticky="w")

block_max = customtkinter.StringVar(value="512")
entry_max = customtkinter.CTkEntry(frame, textvariable=block_max, width=100, fg_color="#000", text_color="#fff", font=label_font, corner_radius=0, border_width=entry_border_width, border_color=entry_border_color)
entry_max.grid(row=2, column=3, pady=5)

def jalankan_dataexe():
    if optionmenu_structure.get().lower() == "stronghold":
        block_max.set(value="2800")
        optionmenu_dimension.set(value="overworld")
    
    structure   = optionmenu_structure.get().lower()
    dimension   = optionmenu_dimension.get().lower()
    version     = optionmenu_version.get().strip()
    seed_value  = entry_seed.get().strip()   
    
    
    print(f"[{INFO}] Struktur: {structure}, Dimensi: {dimension}, Versi: {version}, Seed: {seed_value}")

    label_hasil.delete("0.5", "end")
    try:
        # === Cari versi yang sesuai ===
        selected_version = None
        for v in data["OptionMenu"]:
            if v["minecraft"] == version:
                selected_version = v
                break

        if not selected_version:
            label_hasil.insert("end", f"❌ Versi {version} tidak ditemukan di version.json", text_color="red")
            print(f"[{WARNING}] Versi {version} tidak ditemukan di version.json")
            return

        # === Ambil data dimensi (overworld/nether/dst) ===
        dimensi_data = selected_version["data"].get(dimension)
        if not dimensi_data:
            label_hasil.insert("end", f"❌ Dimensi '{dimension}' tidak ditemukan!", text_color="red")
            print(f"[{WARNING}] Dimensi '{dimension}' tidak ditemukan!", text_color="red")
            return

        exe_path = None

        # ======================
        # CASE 1: format lama (dict)
        # ======================
        if isinstance(dimensi_data, dict):
            exe_path = dimensi_data.get(structure)

        # ======================
        # CASE 2: format baru (list of objects)
        # ======================
        elif isinstance(dimensi_data, list):
            for item in dimensi_data:
                if item.get("type") == structure:
                    exe_path = item.get(structure)
                    break

        # Jika tidak ditemukan
        if not exe_path:
            label_hasil.insert(
                "end", f"❌ Structure '{structure}' tidak ditemukan di dimensi '{dimension}'!")
            print(f"[{WARNING}] Structure '{structure}' tidak ditemukan di dimensi '{dimension}'!")
            return

        # === Cek file fisik ===
        if not os.path.exists(exe_path):
            label_hasil.insert("end", f"❌ File tidak ditemukan:\n{exe_path}")
            print(f"[{WARNING}] File tidak ditemukan:\n{exe_path}")
            return

        # === Jalankan .exe ===
        hasil = subprocess.run(
            [exe_path, seed_value, "30"],
            capture_output=True,
            text=True
        )

        output = hasil.stdout.strip()
        semua = re.findall(r"[A-Za-z]+:\s*(-?\d+),\s*(-?\d+)", output)

        if semua:
            try:
                min_dist = float(entry_min.get())
            except ValueError:
                min_dist = 0
            try:
                max_dist = float(entry_max.get())
            except ValueError:
                max_dist = 100000
                
            print(f"[{INFO}] set jarak min: {min_dist} jarak max: {max_dist}")

            teks = f"{structure.title()}"
            found = False
            

            for i, (coordinatX, coordinatZ) in enumerate(semua, start=1):
                x = int(coordinatX)
                z = int(coordinatZ)
                
                distance = math.sqrt(x**2 + z**2)
                if min_dist <= distance <= max_dist:
                    teks += f"\n#{i}: {x}, {z} = {int(distance)} blok"
                    found = True
                    print(f"[{DONE}] #{i}: {x}, {z} = {int(distance)} blok")

            if not found:
                teks += "\nTidak ditemukan koordinat dalam jarak yang ditentukan."

            label_hasil.insert("end", f"{teks}")

        else:
            label_hasil.insert("end", "❌ Tidak ditemukan koordinat.")
            print(f"[{WARNING}] Tidak ditemukan koordinat.")

    except FileNotFoundError:
        label_hasil.insert("end",  "❌ File version.json tidak ditemukan!")
        print(f"[{WARNING}] File version.json tidak ditemukan!")
    except KeyError as e:
        label_hasil.insert("end",  f"❌ Struktur JSON tidak sesuai! ({e})")
        print(f"[{WARNING}] Struktur JSON tidak sesuai! ({e})")
    except Exception as e:
        label_hasil.insert("end",  f"❌ Error: {e}")
        print(f"[{WARNING}] : {e}")


def delete_input():
    seed.set("")
    optionmenu_structure.set("bastion")
    optionmenu_dimension.set("nether")
    optionmenu_version.set("1.16")
    block_max.set("512")
    block_min.set("0")
    label_hasil.insert("end", "")
    print(f"[{INFO}] restart value input")

    
# ============= [ Button ] ============= #

btn_Search = customtkinter.CTkButton(button_frame, command=jalankan_dataexe, text="Search", fg_color="#00a41a", hover_color="#2F7D30", font=label_font, corner_radius=0)
btn_Search.grid(row=0, column=0, padx=5, pady=5)

btn_Delete = customtkinter.CTkButton(button_frame, command=delete_input, text="Delete", fg_color="#C4322C", hover_color="#982520", font=label_font, corner_radius=0)
btn_Delete.grid(row=0, column=1, padx=5, pady=5)

# btn_refresh = customtkinter.CTkButton(button_frame, text="refresh",  fg_color="#008fd1", hover_color="#0164e6", font=label_font, corner_radius=0)
# btn_refresh.grid(row=0, column=2, padx=4)
# ============= [ Output ] ============= #

label_hasil = customtkinter.CTkTextbox(
    output_frame,
    font=label_output_font, 
    text_color="#090",
    width=420, 
    height=100
)
label_hasil.grid(row=0, column=0, sticky="nswe")
app.bind("<Return>", lambda event: jalankan_dataexe())

print(f"[{INFO}] run aplication mainloop")
app.mainloop()
print(f"[{INFO}] exit aplication mainloop")


