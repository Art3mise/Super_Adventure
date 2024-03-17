import PySimpleGUI as sg
import sys
import lev2_v2

def run_level(level_file):
    try:
        # Utilisez exec pour exécuter la commande
        #exec("python3 lev2.py")
        lev2_v2.lancement()

    except Exception as e:
        print(f"Erreur lors du lancement du jeu : {e}")

layout = [
    [sg.Button('Niveau 1', key='lev1'), sg.Button('Niveau 2', key='lev2'), sg.Button('Niveau 3', key='lev3')],
    [sg.Button('Quitter')]
]

window = sg.Window('Menu', layout)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Quitter'):
        break
    elif event == 'lev1':
        run_level('lev1.py')
    elif event == 'lev2':
        run_level('lev2.py')
    elif event == 'lev3':
        run_level('lev3.py')

window.close()
