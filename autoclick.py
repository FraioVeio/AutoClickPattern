import time
import pyautogui
import cv2
import numpy as np
from PIL import Image

def take_screenshot():
    # Scatta uno screenshot dell'intero schermo
    print("[INFO] Scattando screenshot...")
    screenshot = pyautogui.screenshot()
    # Converti lo screenshot in formato OpenCV
    screenshot_np = np.array(screenshot)
    screenshot_cv = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
    print("[INFO] Screenshot acquisito con successo.")
    return screenshot_cv

def match_template(screenshot, template_path, threshold=0.8):
    print(f"[INFO] Caricamento del template: {template_path}")
    # Carica il template (l'immagine da cercare) in scala di grigi
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    if template is None:
        print(f"[ERRORE] Impossibile caricare il template: {template_path}")
        return None, None, 0

    print("[INFO] Convertendo screenshot in scala di grigi...")
    # Converte lo screenshot in scala di grigi
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    
    print("[INFO] Cercando il template nello screenshot...")
    # Cerca il template nello screenshot
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    
    # Trova le posizioni con un match superiore alla soglia
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    if max_val >= threshold:
        print(f"[INFO] Match trovato con confidenza {max_val} (>= {threshold})")
        # Restituisce la posizione (coordinate) del match, dimensioni e confidenza
        return max_loc, template.shape[::-1], max_val
    else:
        print(f"[INFO] Nessun match trovato. Confidenza massima trovata: {max_val}")
        return None, None, max_val

def perform_action(match_location, template_size):
    x, y = match_location
    width, height = template_size

    # Calcola il centro dell'area trovata
    center_x = x + width // 2
    center_y = y + height // 2

    print(f"[INFO] Spostando il mouse al centro del match: ({center_x}, {center_y})")
    # Sposta il mouse
    pyautogui.moveTo(center_x, center_y)

    # Aggiungi un ritardo di 1 secondo prima di cliccare
    print("[INFO] Attesa di 1 secondo prima di cliccare...")
    time.sleep(1)

    # Esegui il clic
    print(f"[INFO] Eseguendo clic al centro del match: ({center_x}, {center_y})")
    pyautogui.click()

def main(template_path):
    print("[INFO] Avvio del ciclo principale. Cercherò il template ogni 5 secondi.")
    while True:
        print("[INFO] Inizio del nuovo ciclo di rilevamento...")
        screenshot = take_screenshot()
        match_location, template_size, max_confidence = match_template(screenshot, template_path)
        
        if match_location is not None:
            perform_action(match_location, template_size)
        else:
            print(f"[INFO] Nessuna azione eseguita. Confidenza massima: {max_confidence}")
        
        time.sleep(5)  # Attende 5 secondi prima di fare il prossimo screenshot
        print("[INFO] Pausa di 5 secondi conclusa, riprendo.")

if __name__ == "__main__":
    # Il percorso del template immagine è cambiato in image1.png
    template_path = "image1.png"
    print(f"[INFO] Utilizzo del template: {template_path}")
    main(template_path)
