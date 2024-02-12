import tkinter as tk
import random

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

        self.etiqueta_frase = tk.Label(root, text="¡Bienvenido! Haz clic en 'Obtener Frase'")
        self.etiqueta_frase.pack(pady=10)

        self.boton_obtener_frase = tk.Button(root, text="Obtener Frase", command=self.obtener_frase)
        self.boton_obtener_frase.pack(pady=10)

    def obtener_frase(self):
        frase_aleatoria = random.choice(self.frases)
        self.etiqueta_frase.config(text=frase_aleatoria)

if __name__ == "__main__":
    root = tk.Tk()
    app = GalletaDeLaSuerteApp(root)
    root.mainloop()
