# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fenetremodif.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Modificationlien(object):
    def setupUi(self, Modificationlien):
        Modificationlien.setObjectName("Modificationlien")
        Modificationlien.resize(457, 457)
        Modificationlien.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.edit_cours = QtWidgets.QLineEdit(Modificationlien)
        self.edit_cours.setGeometry(QtCore.QRect(230, 100, 181, 22))
        self.edit_cours.setStyleSheet("color: rgb(244, 244, 244);")
        self.edit_cours.setObjectName("edit_cours")
        self.edit_url = QtWidgets.QLineEdit(Modificationlien)
        self.edit_url.setGeometry(QtCore.QRect(230, 150, 181, 22))
        self.edit_url.setStyleSheet("color: rgb(244, 244, 244);")
        self.edit_url.setObjectName("edit_url")
        self.label = QtWidgets.QLabel(Modificationlien)
        self.label.setGeometry(QtCore.QRect(170, 30, 131, 21))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Modificationlien)
        self.label_2.setGeometry(QtCore.QRect(70, 100, 110, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Modificationlien)
        self.label_3.setGeometry(QtCore.QRect(140, 150, 51, 18))
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Modificationlien)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 330, 261, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_off = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_off.setFont(font)
        self.btn_off.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_off.setObjectName("btn_off")
        self.horizontalLayout.addWidget(self.btn_off)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Modificationlien)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(50, 200, 221, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.check_cm = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.check_cm.setFont(font)
        self.check_cm.setStyleSheet("color: rgb(255, 255, 255);")
        self.check_cm.setObjectName("check_cm")
        self.horizontalLayout_2.addWidget(self.check_cm)
        self.checktd = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checktd.setFont(font)
        self.checktd.setStyleSheet("color: rgb(255, 255, 255);")
        self.checktd.setObjectName("checktd")
        self.horizontalLayout_2.addWidget(self.checktd)
        self.btn_add = QtWidgets.QPushButton(Modificationlien)
        self.btn_add.setGeometry(QtCore.QRect(280, 230, 126, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_add.setFont(font)
        self.btn_add.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_add.setObjectName("btn_add")

        self.retranslateUi(Modificationlien)
        QtCore.QMetaObject.connectSlotsByName(Modificationlien)

    def retranslateUi(self, Modificationlien):
        _translate = QtCore.QCoreApplication.translate
        Modificationlien.setWindowTitle(_translate("Modificationlien", "Ajout lien"))
        self.label.setText(_translate("Modificationlien", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#f0f0f0;\">Ajouter un lien</span></p></body></html>"))
        self.label_2.setText(_translate("Modificationlien", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Nom du cours :</span></p></body></html>"))
        self.label_3.setText(_translate("Modificationlien", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">URL :</span></p></body></html>"))
        self.btn_off.setText(_translate("Modificationlien", "Terminé"))
        self.check_cm.setText(_translate("Modificationlien", "Cours"))
        self.checktd.setText(_translate("Modificationlien", "TD"))
        self.btn_add.setText(_translate("Modificationlien", "Ajouter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Modificationlien = QtWidgets.QWidget()
    ui = Ui_Modificationlien()
    ui.setupUi(Modificationlien)
    Modificationlien.show()
    sys.exit(app.exec_())
