import time
import pyautogui
import schedule

def activar_ventana_outlook():
    while not pyautogui.getWindowsWithTitle("Microsoft Outlook"):  # Espera a que aparezca la ventana de Outlook
        time.sleep(1)

    ventana_outlook = pyautogui.getWindowsWithTitle("Microsoft Outlook")[0]
    ventana_outlook.activate()

def realizar_acciones():
    for _ in range(2):
        time.sleep(1)
        pyautogui.press('tab')
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    for _ in range(3):
        pyautogui.press('down')
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

def ejecutar_tareas():
    activar_ventana_outlook()
    realizar_acciones()


if __name__ == "__main__":
    schedule.every(1).minutes.do(ejecutar_tareas)

    while True:
        schedule.run_pending()
        time.sleep(1)
