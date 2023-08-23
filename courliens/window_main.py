from typing import List, Tuple
import webbrowser

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui


from base_donnees import show_db
from ui.UI_main import Ui_MainWindow
from window_add import Ajout
from window_modif import ModifiyWindow
from config import DB_PATH, WINDOW_ICON



# Fonction qui extrait les noms de la liste de tuples renvoyée par les fonctions de gestion de base de données
def create_list(liste_db: List[Tuple]):
    return {item: url for item, url in liste_db}

# ==================================================================================================================== #
#                                           Fenêtre principale
# ==================================================================================================================== #

class ZoomWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  
        # self.setWindowFlag(qtc.Qt.FramelessWindowHint)  # Pour cacher les bprdes de fenêtre.
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(WINDOW_ICON))
        self.setWindowTitle("Courliens")
        self.setFixedWidth(850)
        self.setFixedHeight(650)
        self.btn_ouv.setCursor(QtGui.QCursor(qtc.Qt.PointingHandCursor))
        self.btn_ouv_modif.setCursor(QtGui.QCursor(qtc.Qt.PointingHandCursor))
        # self.showMinimized()

        # Création des dico liant les listes et leurs liens respectifs
        self.dico_CM = create_list(show_db(DB_PATH, 'cm'))
        self.dico_TD = create_list(show_db(DB_PATH, 'td'))
        self.liste_cours = self.dico_CM.keys()
        self.liste_TD = self.dico_TD.keys()

        # Remplissage de la combobox cours
        for cours in self.liste_cours:
            self.box_cm.addItem(cours)
        # Remplissage de la combobox td
        for td in self.liste_TD:
            self.box_td.addItem(td)
        self.btn_ouv.clicked.connect(self.ouvre)  # Bouton qui ouvre la fenêtre d'ajout
        self.btn_ouv_modif.clicked.connect(self.ouvre_modif)  # Bouton qui ouvre fenêtre de modif
        # Connecte dès qu'on bouge la combobox
        self.box_cm.currentIndexChanged.connect(self.selec_CM)
        self.box_td.currentIndexChanged.connect(self.selec_TD)

    # Ouvre la fenêtre d'ajout
    def ouvre(self):
        # print('fonction ouvre activée')
        self.dialog = Ajout()
        # Pour faire passer les signaux dès qu'un cours ou TD est ajouté
        self.dialog.submitted_cours.connect(self.update_combo_cm)
        self.dialog.submitted_td.connect(self.update_combo_td)
        self.dialog.show()

    # Ouvre la fenêtre de modif
    def ouvre_modif(self):
        # print('fonction ouvre activée')
        self.dialog_modif = ModifiyWindow()
        self.dialog_modif.show()

    def selec_CM(self):
        select_cm = self.box_cm.currentText()
        if select_cm == 'Sélectionner Cours':  # Vérifie qu'un vrai cours est sélectionné
            # msg = qtw.QMessageBox()
            # msg.setWindowTitle("Sélection invalide")
            # msg.setText("Veuillez sélectionner un nom de cours valide")
            # msg.setIcon(qtw.QMessageBox.Critical)
            # x = msg.exec_()
            pass
        else:  # Lance l'URL dans le navigateur
            lien_CM = self.dico_CM[select_cm]
            webbrowser.open_new_tab(str(lien_CM))

    def selec_TD(self):
        select_td = self.box_td.currentText()
        if select_td == 'Sélectionner TD':
            # msg = qtw.QMessageBox()
            # msg.setWindowTitle("Sélection invalide")
            # msg.setText("Veuillez sélectionner un nom de TD valide")
            # msg.setIcon(qtw.QMessageBox.Critical)
            # x = msg.exec_()
            pass

        else:  # Lance l'URL dans le navigateur
            lien_TD = self.dico_TD[select_td]
            webbrowser.open_new_tab(str(lien_TD))

    # Fonctions qui modifient la combobox si un signal de la fenêtre ajout est reçu
    @qtc.pyqtSlot(str, str)
    def update_combo_cm(self, nom, lien):
        self.box_cm.addItem(nom)
        self.dico_CM[nom] = lien

    @qtc.pyqtSlot(str, str)
    def update_combo_td(self, nom, lien):
        self.box_td.addItem(nom)
        self.dico_TD[nom] = lien