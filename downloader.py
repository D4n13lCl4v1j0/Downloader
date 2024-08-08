import tkinter as tk
from tkinter import messagebox
import yt_dlp

def descargar_lista_reproduccion(url, formato):
    try:
        ydl_opts = {
            'format': 'bestaudio/best' if formato == "MP3" else 'best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }] if formato == "MP3" else {},
            'outtmpl': '%(title)s.%(ext)s',
            'ffmpeg_location': 'C:/ffmpeg/bin'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        messagebox.showinfo("Completado", "Descarga completa!")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

def iniciar_descarga():
    url = url_entry.get()
    formato = formato_var.get()
    if url:
        descargar_lista_reproduccion(url, formato)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa una URL")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Descargador de YouTube")

# Crear widgets
url_label = tk.Label(ventana, text="URL de la lista de reproducción:")
url_label.pack(pady=5)

url_entry = tk.Entry(ventana, width=50)
url_entry.pack(pady=5)

formato_var = tk.StringVar(value="MP4")
mp4_radio = tk.Radiobutton(ventana, text="MP4", variable=formato_var, value="MP4")
mp3_radio = tk.Radiobutton(ventana, text="MP3", variable=formato_var, value="MP3")

mp4_radio.pack(pady=5)
mp3_radio.pack(pady=5)

descargar_button = tk.Button(ventana, text="Descargar", command=iniciar_descarga)
descargar_button.pack(pady=20)

# Iniciar la aplicación
ventana.mainloop()