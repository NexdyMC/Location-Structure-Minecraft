import customtkinter as ctk
import subprocess
import re
import os

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("Dark")
        self.title("Speedrun MC Tool")
        self.geometry("400x550")

        self.label = ctk.CTkLabel(self, text="Masukkan Seed:")
        self.label.pack(pady=10)

        self.entry = ctk.CTkEntry(self, placeholder_text="Contoh: 123456789")
        self.entry.pack(pady=5, padx=20, fill="x")

        self.btn = ctk.CTkButton(self, text="Cari Struktur", command=self.run_engine)
        self.btn.pack(pady=5, padx=20, fill="x")

        self.textbox = ctk.CTkTextbox(self, height=250)
        self.textbox.pack(pady=10, padx=20, fill="both", expand=True)
        
        self.status = ctk.CTkLabel(self, text="Siap", text_color="gray")
        self.status.pack(pady=5)

    def run_engine(self):
        seed = self.entry.get()
        if not seed:
            self.status.configure(text="Masukkan seed dulu!", text_color="red")
            return

        self.status.configure(text="Mencari...", text_color="yellow")
        self.update()

        # Memastikan end_city.exe ada di folder yang sama
        exe_path = "end_city.exe"
        if not os.path.exists(exe_path):
            self.textbox.insert("end", "Error: end_city.exe tidak ditemukan!\n")
            self.status.configure(text="Gagal", text_color="red")
            return

        try:
            cmd = [exe_path, seed, "--radius:3000"]
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            output = result.stdout
            pola = r"[A-Za-z_]+:\s*(-?\d+),\s*(-?\d+)"
            matches = re.findall(pola, output)

            self.textbox.delete("1.0", "end")
            if not matches:
                self.textbox.insert("end", "Tidak ditemukan.\n")
            else:
                for x, z in matches:
                    self.textbox.insert("end", f"Found: {x}, {z}\n")
            
            self.status.configure(text="Selesai", text_color="green")
        except Exception as e:
            self.textbox.insert("end", f"Error: {str(e)}\n")
            self.status.configure(text="Error", text_color="red")

if __name__ == "__main__":
    app = App()
    app.mainloop()