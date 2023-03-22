from tkinter import *
import pygame
import os

# Inicializar pygame
pygame.init()

# Crear la ventana
ventana = Tk()
ventana.title("Reproductor de música")

# Crear etiquetas de volumen
volumen_label = Label(ventana, text="Volumen:")
volumen_label.grid(row=0, column=0, padx=5, pady=5)

volumen_value = DoubleVar()
volumen_value.set(0.5)

volumen_slider = Scale(ventana, from_=0, to=1, resolution=0.1, orient=HORIZONTAL, variable=volumen_value)
volumen_slider.grid(row=0, column=1, padx=5, pady=5)

# Crear botones de control de la música
play_button = Button(ventana, text="Play")
play_button.grid(row=1, column=0, padx=5, pady=5)

pause_button = Button(ventana, text="Pause")
pause_button.grid(row=1, column=1, padx=5, pady=5)

atras_button = Button(ventana, text="Atrás")
atras_button.grid(row=1, column=2, padx=5, pady=5)

siguiente_button = Button(ventana, text="Siguiente")
siguiente_button.grid(row=1, column=3, padx=5, pady=5)

# Crear botón para seleccionar archivo de música
def seleccionar_archivo():
    archivo = filedialog.askopenfilename(initialdir=os.getcwd(), title="Seleccionar archivo de música", filetypes=(("Archivos MP3", "*.mp3"),))
    if archivo:
        pygame.mixer.music.load(archivo)
        pygame.mixer.music.play()

archivo_button = Button(ventana, text="Seleccionar archivo", command=seleccionar_archivo)
archivo_button.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

# Funciones para controlar la música
def play():
    pygame.mixer.music.unpause()

def pause():
    pygame.mixer.music.pause()

def atras():
    pygame.mixer.music.stop()
    pygame.mixer.music.play()

def siguiente():
    pygame.mixer.music.stop()

# Asociar las funciones a los botones
play_button.config(command=play)
pause_button.config(command=pause)
atras_button.config(command=atras)
siguiente_button.config(command=siguiente)

# Iniciar la ventana
ventana.mainloop()
