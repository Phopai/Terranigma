import os
import PyInstaller.__main__
# File Python yang ingin dikonversi
script_file = "terranigmaSP.py"  # Ganti dengan nama file Python Anda
# Direktori output
output_dir = "dist"
# Jalankan PyInstaller
PyInstaller.__main__.run([
    script_file,
    '--onefile',  # Menggabungkan semua ke dalam satu file .exe
    '--noconsole',  # Jangan tampilkan konsol (untuk aplikasi GUI)
    '--distpath', output_dir,  # Direktori output untuk file .exe
    '--name', 'TerranigmaSP'  # Nama aplikasi .exe
])
print(f"Konversi selesai! File .exe Anda ada di folder: {os.path.abspath(output_dir)}")