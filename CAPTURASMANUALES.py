#pip install keyboard
#pip install pyautogui pillow fpdf

import pyautogui
import keyboard
import time
from fpdf import FPDF
from PIL import Image
import os

folder = "capturas_manual"
os.makedirs(folder, exist_ok=True)

num_capturas = 0
print("Listo para capturar. Presiona la tecla RIGHT (flecha derecha) para tomar una captura. Presiona ESC para salir.")


while True:
    if keyboard.is_pressed('right'):
        num_capturas += 1
        nombre = os.path.join(folder, f"captura_{num_capturas}.png")
        screenshot = pyautogui.screenshot()
        screenshot.save(nombre)
        print(f"[{num_capturas}] Captura guardada.")

        while keyboard.is_pressed('right'):
            time.sleep(0.05)

    elif keyboard.is_pressed('esc'):
        print("Captura finalizada.")
        break

# Crear PDF sin deformar imágenes
pdf = FPDF()
for i in range(1, num_capturas + 1):
    imagen_path = os.path.join(folder, f"captura_{i}.png")
    image = Image.open(imagen_path)

    width, height = image.size
    width_mm = width * 0.264583
    height_mm = height * 0.264583

    if width_mm > 210:
        ratio = 210 / width_mm
        width_mm *= ratio
        height_mm *= ratio
    if height_mm > 297:
        ratio = 297 / height_mm
        width_mm *= ratio
        height_mm *= ratio

    pdf.add_page()
    pdf.image(imagen_path, x=0, y=0, w=width_mm, h=height_mm)

pdf.output("capturas_manual.pdf", "F")
print(f"PDF creado con {num_capturas} capturas: capturas_manual.pdf")
