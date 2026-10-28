
import pyautogui
import time
import winsound

# =========================
# CONFIGURACIÓN
# =========================

SCAN_BUTTON = (-97, 1254)
ADD_PAGE_BUTTON = (-84, 130)
SAVE_FILE_BUTTON = (-134, 1246)

# Tiempo de escaneo
FIRST_SCAN_DURATION = 45  # Primera hoja
SCAN_DURATION = 25        # Resto de hojas

USER_DELAY = 10           # Tiempo para cambiar hoja


# =========================
# FUNCIONES
# =========================

def click(pos):
    pyautogui.click(pos[0], pos[1])


def beep_aviso():
    # Dos pitidos para cambiar la hoja
    for _ in range(2):
        winsound.Beep(1000, 300)
        time.sleep(0.2)


def beep_final():
    # Tres pitidos al terminar
    for _ in range(3):
        winsound.Beep(800, 500)
        time.sleep(0.2)


# =========================
# PROGRAMA PRINCIPAL
# =========================

def main():

    hojas = int(input("¿Cuántas hojas vas a escanear?: "))

    if hojas < 1:
        print("Debes introducir al menos una hoja.")
        return

    print("\nEmpieza en 5 segundos...")
    print("Coloca HP Smart en primer plano.")
    time.sleep(5)

    for i in range(hojas):

        print(f"\nEscaneando hoja {i + 1}/{hojas}")

        # Pulsar ESCANEAR
        click(SCAN_BUTTON)

        # Mayor espera en el primer escaneo
        if i == 0:
            espera = FIRST_SCAN_DURATION
        else:
            espera = SCAN_DURATION

        print(f"Esperando {espera} segundos...")
        time.sleep(espera)

        # Si quedan más hojas
        if i < hojas - 1:

            print("Preparando siguiente hoja...")

            # Aviso sonoro
            beep_aviso()

            # Pulsar AGREGAR
            click(ADD_PAGE_BUTTON)

            print(f"Tienes {USER_DELAY} segundos para cambiar la hoja.")
            time.sleep(USER_DELAY)

    print("\n¡Escaneo completado!")
    print("Revisa las páginas en HP Smart antes de guardar.")

    beep_final()


if __name__ == "__main__":
    main()
