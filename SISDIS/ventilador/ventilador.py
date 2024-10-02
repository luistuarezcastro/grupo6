import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import threading
import time
import random

class TemperatureSensor:
    def __init__(self):
        self.temperature = 20  # Temperatura inicial

    def read_temperature(self):
        # Simula la lectura de temperatura
        self.temperature = 20 + random.uniform(-5, 10)
        return self.temperature

class FanController:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        return "Encendido"

    def turn_off(self):
        self.is_on = False
        return "Apagado"

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Control de Ventilador")
        self.root.geometry("400x300")

        # Configuración de las imágenes
        self.load_images()

        self.sensor = TemperatureSensor()
        self.controller = FanController()

        # Etiquetas para temperatura y estado del ventilador
        self.temperature_label = ttk.Label(root, text="Temperatura: -- °C", font=("Arial", 16))
        self.temperature_label.pack(pady=10)

        self.fan_status_label = ttk.Label(root, text="Estado del Ventilador: --", font=("Arial", 16))
        self.fan_status_label.pack(pady=10)

        # Etiqueta para mostrar la imagen del ventilador
        self.fan_image_label = ttk.Label(root)
        self.fan_image_label.pack(pady=10)

        # Inicialización de la imagen del ventilador
        self.update_fan_image(fan_on=False)

        # Inicia el hilo para actualizar la interfaz gráfica
        self.update_thread = threading.Thread(target=self.update_display)
        self.update_thread.daemon = True
        self.update_thread.start()

    def load_images(self):
        try:
            # Carga las imágenes y mantiene referencias
            self.fan_on_image = Image.open("C:/Users/CompuStore/Pictures/fan_on.jpeg")
            self.fan_off_image = Image.open("C:/Users/CompuStore/Pictures/Fan_off.jpeg")
            self.fan_on_photo = ImageTk.PhotoImage(self.fan_on_image)
            self.fan_off_photo = ImageTk.PhotoImage(self.fan_off_image)
            
            # Mantener referencias a las imágenes para evitar que sean recolectadas
            self.image_refs = {
                "on": self.fan_on_photo,
                "off": self.fan_off_photo
            }
        except Exception as e:
            print(f"Error al cargar las imágenes: {e}")
            self.fan_on_photo = None
            self.fan_off_photo = None

    def update_display(self):
        while True:
            temp = self.sensor.read_temperature()
            self.root.after(0, self.update_temperature_label, temp)
            fan_status = self.controller.turn_on() if temp >= 23 else self.controller.turn_off()
            self.root.after(0, self.update_fan_status_label, fan_status)
            self.root.after(0, self.update_fan_image, temp >= 23)
            time.sleep(2)  # Actualiza cada 2 segundos

    def update_temperature_label(self, temp):
        self.temperature_label.config(text=f"Temperatura: {temp:.2f} °C")

    def update_fan_status_label(self, fan_status):
        self.fan_status_label.config(text=f"Estado del Ventilador: {fan_status}")

    def update_fan_image(self, fan_on):
        if self.fan_on_photo and self.fan_off_photo:
            image_to_show = self.fan_on_photo if fan_on else self.fan_off_photo
            self.fan_image_label.config(image=image_to_show)
        else:
            # Si no se cargaron las imágenes, muestra un texto de error
            self.fan_image_label.config(text="Imagen no disponible")

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()

