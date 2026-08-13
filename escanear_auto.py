import pyautogui
import time
import winsound

# =========================
# CONFIGURACIÓN
# =========================

SCAN_BUTTON = (-97, 1254)
ADD_PAGE_BUTTON = (-84, 130)
SAVE_FILE_BUTTON = (-134, 1246)

SCAN_DURATION = 20  
USER_DELAY = 10  


# =========================
# FUNCIONES
# =========================

def click(pos):
    pyautogui.click(pos[0], pos[1])

def beep_aviso():
    # Hace "beep beep"
    for _ in range(2):
        winsound.Beep(1000, 300)  # frecuencia (Hz), duración (ms)
        time.sleep(0.2)


# =========================
# SCRIPT
# =========================

def main():
    hojas = int(input("¿Cuántas hojas vas a escanear?: "))

    print("Empieza en 5 segundos... coloca HP Smart en primer plano")
    time.sleep(5)

    for i in range(hojas):
        print(f"Escaneando hoja {i+1}/{hojas}")

        click(SCAN_BUTTON)

        time.sleep(SCAN_DURATION)

        if i < hojas - 1:
            print("Cambia la hoja...")

            # AVISO SONORO
            beep_aviso()

            click(ADD_PAGE_BUTTON)

            time.sleep(USER_DELAY)

    print("Escaneo completado.")

    # beep final más largo
    for _ in range(3):
        winsound.Beep(800, 500)
        time.sleep(0.2)


if __name__ == "__main__":
    main()