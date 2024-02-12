import tkinter as tk
import random
import pyttsx3

class GalletaDeLaSuerteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Galleta de la Suerte")

        self.frases = [
            "Hoy es un buen día para aprender algo nuevo.",
            "La paciencia es la clave del éxito.",
            "Confía en ti mismo y todo será posible.",
            "La vida es como andar en bicicleta, para mantener el equilibrio, debes seguir adelante.",
            "El único lugar donde el éxito viene antes del trabajo es en el diccionario.",
            "La suerte es lo que sucede cuando la preparación se encuentra con la oportunidad.",
        ]

        self.contador = 0  # Inicializar el contador

        self.etiqueta_frase = tk.Label(root, text="¡Bienvenido! Haz clic en 'Obtener Frase'")
        self.etiqueta_frase.pack(pady=10)

        self.etiqueta_contador = tk.Label(root, text=f"Frases entregadas: {self.contador}")
        self.etiqueta_contador.pack(pady=5)

        self.boton_obtener_frase = tk.Button(root, text="Obtener Frase", command=self.obtener_frase)
        self.boton_obtener_frase.pack(pady=10)

        self.engine = pyttsx3.init()

    def obtener_frase(self):
        frase_aleatoria = random.choice(self.frases)
        self.etiqueta_frase.config(text=frase_aleatoria)
        self.leer_frase(frase_aleatoria)
        self.contador += 1  # Incrementar el contador
        self.etiqueta_contador.config(text=f"Frases entregadas: {self.contador}")  # Actualizar la etiqueta del contador

    def leer_frase(self, frase):
        self.engine.say(frase)
        self.engine.runAndWait()

if __name__ == "__main__":
    root = tk.Tk()
    app = GalletaDeLaSuerteApp(root)
    root.mainloop()
