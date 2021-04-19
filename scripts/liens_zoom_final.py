from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5.uic import loadUi
from PyQt5 import QtGui
import sys
import base_donnees
from n_fenetre import Ui_Modificationlien
from new_zoom import Ui_MainWindow
import sqlite3
import webbrowser


# Fonction (maintenant obsolète) pour relancer le script et mettre à jour les combobox.
# def restart_program():
#     python = sys.executable
#     os.execl(python, python, * sys.argv)


# Création des tables, si elles n'existent pas
base_donnees.create_tab_cours()
base_donnees.create_tab_td()


# Fonction qui extrait les noms de la liste de tuples renvoyée par les fonctions de gestion de base de données
def create_list(liste_db):
    liste = []
    for cm in liste_db:
        i = cm[0]
        if len(i) != 0:
            liste.append(i)
    return liste

# ==================================================================================================================== #
#                                           Image de chargement
# ==================================================================================================================== #



# ==================================================================================================================== #
#                                           Fenêtre principale
# ==================================================================================================================== #


# Hérite de Ui_MainWindow, "class" d'un autre fichier juste pour faire l'interface
class ZoomWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  
        # self.setWindowFlag(qtc.Qt.FramelessWindowHint)  # Pour cacher les bprdes de fenêtre.
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('zoom_app.ico'))
        self.setFixedWidth(850)
        self.setFixedHeight(650)
        self.btn_ouv.setCursor(QtGui.QCursor(qtc.Qt.PointingHandCursor))
        self.btn_ouv_modif.setCursor(QtGui.QCursor(qtc.Qt.PointingHandCursor))
        # self.showMinimized()

        # Création des listes de cours et de leurs liens
        self.liste_cours = create_list(base_donnees.show_cm())
        self.url_cours = create_list(base_donnees.show_urlcm())
        # Création des listes de TD et de leurs liens
        self.liste_TD = create_list(base_donnees.show_td())
        self.url_TD = create_list(base_donnees.show_urltd())
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

    # Fonctions qui modifient la comobox si un signal de la fenêtre ajout est reçu
    @qtc.pyqtSlot(str, str)
    def update_combo_cm(self, nom, lien):
        self.box_cm.addItem(nom)
        self.dico_CM[nom] = lien

    @qtc.pyqtSlot(str, str)
    def update_combo_td(self, nom, lien):
        self.box_td.addItem(nom)
        self.dico_TD[nom] = lien


# ==================================================================================================================== #
#                                           Fenêtre d'ajout
# ==================================================================================================================== #

class Ajout(qtw.QWidget, Ui_Modificationlien):
    # Création des déclencheurs de signaux
    submitted_cours = qtc.pyqtSignal(str, str)
    submitted_td = qtc.pyqtSignal(str, str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('zoom_app.ico'))
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
            base_donnees.add_cm(nom1, url)  # Ajoute le nom et l'URL à la base de données
            # print('Valeurs ajoutées aux cm')
            self.submitted_cours.emit(nom1, url)  # Envoie le signal d'ajout

        if verif_td and not verif_ent:  # Même chose avec les TD
            # print('Ajout TD')
            nom2 = str(nom)
            base_donnees.add_td(nom2, url)
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

# ==================================================================================================================== #
#                                         Fenêtre de modification
# ==================================================================================================================== #


"""Ici pas de compilation du fichier interface modif.ui en Python, il est chargé directement. Ce qui est plus pratique 
car les changements sont pris en compte quand l'interface est modifiée sur QtDesigner, """

class ModifiyWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        loadUi('modif.ui', self)  # C'est ici que je charge l'interface, le nom des objets est conservé
        self.setWindowIcon(QtGui.QIcon('zoom_app.ico'))
        # self.modif_frame.resize(self.modif_frame.sizeHint())
        # self.modif_frame.addWidget(self.btn_modif)
        self.setFixedWidth(850)
        self.setFixedHeight(700)
        self.btn_modif.setStyleSheet("*{color: 'white';}"
                                     "*:hover{background-color : '#1e6282'}")
        self.btn_sup.setStyleSheet("*{color: 'white'}"
                                   "*:hover{background-color : '#1e6282'}")
        self.btn_term.setStyleSheet("*{color: 'white'}"
                                    "*:hover{background-color : '#1e6282'}")

        self.btn_term.setCursor(QtGui.QCursor(qtc.Qt.PointingHandCursor))
        self.btn_modif.setCursor(QtGui.QCursor(qtc.Qt.PointingHandCursor))
        self.btn_sup.setCursor(QtGui.QCursor(qtc.Qt.PointingHandCursor))

        self.btn_modif.clicked.connect(self.modifier)
        self.btn_sup.clicked.connect(self.supprimer)
        self.btn_term.clicked.connect(self.close)

        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 30)
        self.tableWidget.setColumnWidth(2, 200)
        self.tableWidget.setColumnWidth(3, 30)
        self.load_data()
        self.tableWidget.selectionModel().selectionChanged.connect(self.on_selection_changed)
        self.line_name.setReadOnly(True)

    # Fonction qui affiche dynamiquement ce qui a été séléctionné par l'utilisateur
    def on_selection_changed(self, selected):
        self.line_name.clear()
        self.line_url.clear()
        self.ident = -1
        self.colonne = -1

        for index in selected.indexes():
            self.ligne, self.colonne = index.row(), index.column()
            try:  # Si cellule non-vide, capte le texte de celle-ci
                self.valeur = self.tableWidget.item(self.ligne, self.colonne).text()
                self.ident = self.tableWidget.item(self.ligne, self.colonne + 1).text()
                self.label_id.setText(f"Identifiant: {self.ident}")
                self.label_id.setStyleSheet('color: white; font-size: 18px; font-weight: bold')
                self.line_name.setText(self.valeur)
            except AttributeError:
                pass
            if self.colonne == 0 and self.ident != -1:
                try:  # Avec le nom pris dans la cellule, on recherche le lien associé
                    lien_cm = base_donnees.recherche_url_cm(self.ident)[0][0]
                    self.line_url.setText(str(lien_cm))
                except IndexError:
                    self.line_url.setText("Pas de lien associé, cellule vide ou colonnne ID ?")
            if self.colonne == 2 and self.ident != -1:
                try:
                    lien_td = base_donnees.recherche_url_td(self.ident)[0][0]
                    self.line_url.setText(str(lien_td))
                except IndexError or AttributeError:
                    self.line_url.setText("Pas de lien associé, cellule vide ou colonne ID ?")

    def load_data(self):
        conn = sqlite3.connect('infozoom.db')
        c = conn.cursor()
        sqlquery1 = """SELECT rowid,nom_cours FROM info_cours"""
        sqlquery2 = """SELECT rowid,nom_td FROM infotd"""
        # Obligé de faire deux indications différentes car les deux tables ne "matchent" pas. Fonction FULL JOIN pas
        # dispo sur sqlite3
        item1 = c.execute(sqlquery1)
        lignes1 = c.fetchall()
        item2 = c.execute(sqlquery2)
        lignes2 = c.fetchall()
        lu = max([len(lignes1), len(lignes2)])  # Prends la longueur max entre les des deux tables.
        self.tableWidget.setRowCount(lu)  # Fixe le nombre de colonnes de la "tableWidget"

        tablerow1 = 0  # Indique à la "tableWidget" sur quelle ligne l'information est ajoutée
        for row1 in lignes1:
            ident1 = str(row1[0])
            self.tableWidget.setItem(tablerow1, 0, qtw.QTableWidgetItem(row1[1]))
            self.tableWidget.setItem(tablerow1, 1, qtw.QTableWidgetItem(ident1))
            tablerow1 += 1

        tablerow2 = 0
        for row2 in lignes2:
            ident2 = str(row2[0])
            self.tableWidget.setItem(tablerow2, 2, qtw.QTableWidgetItem(row2[1]))
            self.tableWidget.setItem(tablerow2, 3, qtw.QTableWidgetItem(ident2))
            tablerow2 += 1

    # Les fonctions "modifier" et "supprimer" fonctionnent à peu près comme "ajout"

    def modifier(self):
        # print('Fonction modification')
        nom = self.line_name.text()
        url = self.line_url.toPlainText()
        verif_ent = len(nom) == 0 or len(url) == 0  # Renvoie un booléen, vrai si champ vide

        if verif_ent:
            msg = qtw.QMessageBox()
            msg.setWindowTitle("Saisie incomplète")
            msg.setText("Veuillez remplir tous les champs")

            msg.setIcon(qtw.QMessageBox.Warning)
            x = msg.exec_()

        if self.colonne == 0 and not verif_ent:

            nom1 = str(nom)
            base_donnees.modify_cm(nom1, url, self.ident)
            msg = qtw.QMessageBox()
            msg.setWindowTitle('Lien modifié')
            msg.setText(f" Le lien de {nom} a été modifié avec succès")

            msg.setIcon(qtw.QMessageBox.Information)
            x = msg.exec_()

        if self.colonne == 2 and not verif_ent:

            nom2 = str(nom)
            base_donnees.modify_td(nom2, url, self.ident)
            msg = qtw.QMessageBox()
            msg.setWindowTitle('Lien modifié')
            msg.setText(f" Le lien de {nom} a été modifié avec succès")
            msg.setIcon(qtw.QMessageBox.Information)
            x = msg.exec_()

        self.line_name.clear()
        self.line_url.clear()

    def supprimer(self):
        nom = self.line_name.text()
        verif_ent = len(nom) == 0  # Renvoie un booléen, vrai si champ vide

        if verif_ent:

            msg = qtw.QMessageBox()
            msg.setWindowTitle("Saisie incomplète")
            msg.setText("Veuillez remplir tous les champs")
            msg.setIcon(qtw.QMessageBox.Warning)
            x = msg.exec_()

        if self.colonne == 0 and not verif_ent:

            base_donnees.delete_cm(self.ident)
            msg = qtw.QMessageBox()
            msg.setWindowTitle('Lien Supprimé')
            msg.setText(f" Le lien de {nom} a été supprimé avec succès. "
                        f"Il disparaitra de la table une fois que vous "
                        f"quitterez cette fenêtre.")
            msg.setIcon(qtw.QMessageBox.Information)
            x = msg.exec_()

        if self.colonne == 2 and not verif_ent:

            base_donnees.delete_td(self.ident)
            msg = qtw.QMessageBox()
            msg.setWindowTitle('Lien Supprimé')
            msg.setText(f" Le lien de {nom} a été supprimé avec succès. "
                        f"Il disparaitra de la table une fois que vous "
                        f"quitterez cette fenêtre.")
            msg.setIcon(qtw.QMessageBox.Information)
            x = msg.exec_()

        self.line_name.clear()
        self.line_url.clear()





if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    splash = qtw.QSplashScreen(QtGui.QPixmap('start_pic.jpg'))
    splash.show()
    qtc.QTimer.singleShot(7000, splash.close)
    # screen_resolution = app.desktop().screenGeometry()
    # width, height = screen_resolution.width(), screen_resolution.height()
    main_win = ZoomWindow()
    main_win.show()
    app.exec_()


