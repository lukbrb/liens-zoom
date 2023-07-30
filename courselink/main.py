import sys
from PyQt5 import QtCore, QtGui, QtWidgets as qtw


import resources.base_donnees as base_donnees
from config import DB_PATH, START_ICON
from window_main import ZoomWindow


if __name__ == '__main__':
    
    # Création des tables, si elles n'existent pas
    base_donnees.create_tab_cours(DB_PATH)
    base_donnees.create_tab_td(DB_PATH)

    app = qtw.QApplication(sys.argv)
    splash = qtw.QSplashScreen(QtGui.QPixmap(START_ICON))
    splash.show()
    QtCore.QTimer.singleShot(5000, splash.close)
    # screen_resolution = app.desktop().screenGeometry()
    # width, height = screen_resolution.width(), screen_resolution.height()
    main_win = ZoomWindow()
    main_win.show()
    app.exec_()
