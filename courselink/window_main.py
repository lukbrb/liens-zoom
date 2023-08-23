import webbrowser

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui


from resources import base_donnees
from resources.UI_main import Ui_MainWindow
from window_add import Ajout
from window_modif import ModifiyWindow
from config import DB_PATH, WINDOW_ICON



# Fonction qui extrait les noms de la liste de tuples renvoyée par les fonctions de gestion de base de données
def create_list(liste_db):
    liste = []
    for cm in liste_db:
        i = cm[0]
        if len(i) != 0:
            liste.append(i)
    return liste

# ==================================================================================================================== #
#                                           Fenêtre principale
# ==================================================================================================================== #


# Hérite de Ui_MainWindow, "class" d'un autre fichier juste pour faire l'interface
class ZoomWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  
        # self.setWindowFlag(qtc.Qt.FramelessWindowHint)  # Pour cacher les bprdes de fenêtre.
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(WINDOW_ICON))
        self.setFixedWidth(850)
        self.setFixedHeight(650)
        self.btn_ouv.setCursor(QtGui.QCursor(qtc.Qt.PointingHandCursor))
        self.btn_ouv_modif.setCursor(QtGui.QCursor(qtc.Qt.PointingHandCursor))
        # self.showMinimized()

        # Création des listes de cours et de leurs liens
        self.liste_cours = create_list(base_donnees.show_cm(DB_PATH))
        self.url_cours = create_list(base_donnees.show_urlcm(DB_PATH))
        # Création des listes de TD et de leurs liens
        self.liste_TD = create_list(base_donnees.show_td(DB_PATH))
        self.url_TD = create_list(base_donnees.show_urltd(DB_PATH))
        # Création des dico liant les listes et leurs liens respectifs
        self.dico_CM = dict(zip(self.liste_cours, self.url_cours))
        self.dico_TD = dict(zip(self.liste_TD, self.url_TD))

        # Remplissage de la combobox cours
        for i in self.liste_cours:
            self.box_cm.addItem(i)
        # Remplissage de la combobox td
        for j in self.liste_TD:
            self.box_td.addItem(j)
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
            msg = qtw.QMessageBox()
            msg.setWindowTitle("Sélection invalide")
            msg.setText("Veuillez sélectionner un nom de cours valide")
            msg.setIcon(qtw.QMessageBox.Critical)
            x = msg.exec_()
        else:  # Lance l'URL dans le navigateur
            lien_CM = self.dico_CM[select_cm]
            webbrowser.open_new_tab(str(lien_CM))
            # print("Let's go")

    def selec_TD(self):
        select_td = self.box_td.currentText()
        if select_td == 'Sélectionner TD':
            msg = qtw.QMessageBox()
            msg.setWindowTitle("Sélection invalide")
            msg.setText("Veuillez sélectionner un nom de TD valide")
            msg.setIcon(qtw.QMessageBox.Critical)
            x = msg.exec_()

        else:  # Lance l'URL dans le navigateur
            lien_TD = self.dico_TD[select_td]
            webbrowser.open_new_tab(str(lien_TD))
            # print("Let's go")

    # Fonctions qui modifient la combobox si un signal de la fenêtre ajout est reçu
    @qtc.pyqtSlot(str, str)
    def update_combo_cm(self, nom, lien):
        self.box_cm.addItem(nom)
        self.dico_CM[nom] = lien

    @qtc.pyqtSlot(str, str)
    def update_combo_td(self, nom, lien):
        self.box_td.addItem(nom)
        self.dico_TD[nom] = lien