import time
import pyautogui
import subprocess
import os


raw_path = "C:/Users/Lucas/AppData/Roaming/Zoom/bin/Zoom.exe"
os.chdir('../')

def sign_in(reunion_id, mdp):
    # Ouvre Zoom et fait une pause de 5s
    subprocess.Popen(raw_path)
    time.sleep(1)

    # Clique le bouton "rejoindre"
    rejoin_btn = pyautogui.locateCenterOnScreen('images/btn_join.png')
    pyautogui.moveTo(rejoin_btn)
    pyautogui.click()
    # time.sleep(3)
    # Entre le code ou URL de la réunion
    reunion_id_btn = pyautogui.locateCenterOnScreen('images/champ_id.png')
    pyautogui.moveTo(reunion_id_btn)
    # pyautogui.click()
    pyautogui.typewrite(reunion_id)

    # Désactive caméra et micro
    media_btn = pyautogui.locateAllOnScreen('images/case.png')
    for btn in media_btn:
        pyautogui.moveTo(btn)
        pyautogui.click()

    # Clique sur le bouton rejoindre
    # time.sleep(2)
    join_btn = pyautogui.locateCenterOnScreen('images/btn_join2.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    # Entre le mot de passe
    mdp_ent = pyautogui.locateCenterOnScreen('images/champ_mdp.png')
    pyautogui.moveTo(mdp_ent)
    # pyautogui.click()
    pyautogui.write(mdp)
    pyautogui.press('enter')




