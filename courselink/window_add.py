from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5.uic import loadUi
from PyQt5 import QtGui


import resources.base_donnees as base_donnees
from resources.UI_modif import Ui_Modificationlien

from config import DB_PATH, WINDOW_ICON


class Ajout(qtw.QWidget, Ui_Modificationlien):
    # Création des déclencheurs de signaux
    submitted_cours = qtc.pyqtSignal(str, str)
    submitted_td = qtc.pyqtSignal(str, str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(WINDOW_ICON))
        self.setFixedWidth(450)
        self.setFixedHeight(450)
        self.btn_add.setStyleSheet("*{color: 'white';}"
                                   "*:hover{background-color : '#1e6282'}")
        self.btn_off.setStyleSheet("*{color: 'white'}"
                                   "*:hover{background-color : '#1e6282'}")

        self.btn_add.setCursor(QtGui.QCursor(qtc.Qt.PointingHandCursor))
        self.btn_off.setCursor(QtGui.QCursor(qtc.Qt.PointingHandCursor))

        self.btn_add.clicked.connect(self.ajouter)
        self.btn_off.clicked.connect(self.close)

# TODO: Si aucune case remplie, désactiver les boutons

    def ajouter(self):
        # print('Fonction ajout')
        nom = self.edit_cours.text()
        url = self.edit_url.text()

        verif_cm = self.check_cm.isChecked()
        verif_td = self.checktd.isChecked()
        verif_ent = len(nom) == 0 or len(url) == 0  # Renvoie un booléen, vrai si champ vide

        if verif_ent:  # Vérifie que tous les champs sont remplis
            msg = qtw.QMessageBox()
            msg.setWindowTitle("Saisie incomplète")
            msg.setText("Veuillez remplir tous les champs")
            msg.setIcon(qtw.QMessageBox.Warning)
            x = msg.exec_()

        if verif_cm and not verif_ent:  # Si toutes les cases remplies et checkbox CM cochée
            nom1 = str(nom)
            base_donnees.add_cm(nom1, url, DB_PATH)  # Ajoute le nom et l'URL à la base de données
            # print('Valeurs ajoutées aux cm')
            self.submitted_cours.emit(nom1, url)  # Envoie le signal d'ajout

        if verif_td and not verif_ent:  # Même chose avec les TD
            # print('Ajout TD')
            nom2 = str(nom)
            base_donnees.add_td(nom2, url, DB_PATH)
            # print('Données ajoutées aux TD')
            self.submitted_td.emit(nom2, url)

        elif not verif_td and not verif_cm:  # Vérifie qu'au moins une checkbox est cochée

            msg = qtw.QMessageBox()
            msg.setWindowTitle("Erreur de saisie")
            msg.setText("Veuillez cocher au moins une case")
            msg.setIcon(qtw.QMessageBox.Critical)
            x = msg.exec_()

        # Efface le texte entré et décoche les checkbox
        self.edit_cours.clear()
        self.edit_url.clear()
        self.check_cm.setChecked(False)
        self.checktd.setChecked(False)
