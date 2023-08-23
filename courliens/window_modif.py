import sqlite3

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5.uic import loadUi
from PyQt5 import QtGui


from base_donnees import delete_cm, delete_td, modify_cm, modify_td, recherche_url_cm, recherche_url_td
from config import DB_PATH, MODIF_UI, WINDOW_ICON


# ==================================================================================================================== #
#                                         Fenêtre de modification
# ==================================================================================================================== #


"""Ici pas de compilation du fichier interface modif.ui en Python, il est chargé directement. Ce qui est plus pratique 
car les changements sont pris en compte quand l'interface est modifiée sur QtDesigner, """

class ModifiyWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        loadUi(MODIF_UI, self)  # C'est ici que je charge l'interface, le nom des objets est conservé
        self.setWindowIcon(QtGui.QIcon(WINDOW_ICON))
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
                    lien_cm = recherche_url_cm(self.ident, DB_PATH)[0][0]
                    self.line_url.setText(str(lien_cm))
                except IndexError:
                    self.line_url.setText("Pas de lien associé, cellule vide ou colonnne ID ?")
            if self.colonne == 2 and self.ident != -1:
                try:
                    lien_td = recherche_url_td(self.ident, DB_PATH)[0][0]
                    self.line_url.setText(str(lien_td))
                except IndexError or AttributeError:
                    self.line_url.setText("Pas de lien associé, cellule vide ou colonne ID ?")

    def load_data(self):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        sqlquery1 = """SELECT rowid,nom_cm FROM info_cm"""
        sqlquery2 = """SELECT rowid,nom_td FROM info_td"""
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
            modify_cm(nom1, url, self.ident, DB_PATH)
            msg = qtw.QMessageBox()
            msg.setWindowTitle('Lien modifié')
            msg.setText(f" Le lien de {nom} a été modifié avec succès")

            msg.setIcon(qtw.QMessageBox.Information)
            x = msg.exec_()

        if self.colonne == 2 and not verif_ent:

            nom2 = str(nom)
            modify_td(nom2, url, self.ident, DB_PATH)
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

            delete_cm(self.ident, DB_PATH)
            msg = qtw.QMessageBox()
            msg.setWindowTitle('Lien Supprimé')
            msg.setText(f" Le lien de {nom} a été supprimé avec succès. "
                        f"Il disparaitra de la table une fois que vous "
                        f"quitterez cette fenêtre.")
            msg.setIcon(qtw.QMessageBox.Information)
            x = msg.exec_()

        if self.colonne == 2 and not verif_ent:

            delete_td(self.ident, DB_PATH)
            msg = qtw.QMessageBox()
            msg.setWindowTitle('Lien Supprimé')
            msg.setText(f" Le lien de {nom} a été supprimé avec succès. "
                        f"Il disparaitra de la table une fois que vous "
                        f"quitterez cette fenêtre.")
            msg.setIcon(qtw.QMessageBox.Information)
            x = msg.exec_()

        self.line_name.clear()
        self.line_url.clear()
