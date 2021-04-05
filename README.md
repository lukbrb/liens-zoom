# Liens Zoom
Application avec interface permettant d'enregistrer dans une base de données des liens Zoom liés à des cours (peut servir pour enregisrer des liens quelconques sinon).
Il est possible d'ajouter, modifier et supprimer des liens/cours. Il est également possible d'intéragir directement avec la base de données dans la fenêtre "modifier".

#### L'installateur LiensZoom.exe permet de télécharger et d'installer l'application sur tout appareil Windows

## STRUCTURE


### SCRIPTS

- liens_zoom_final.py est le script principal
- bases_donnees.py est le script dans lequel sont écrites les fonctions intéregissant avec la base de données
- auto_connect.py est un script qui ouvre l'application de Bureau Zoom et intéragit automatiquement avec l'application en cliquant sur les boutons et en écrivant les informations nécessaires au lancement d'une réunion. N'est pour l'instant pas intégré au script principal "liens_zoom_final.py" car le processus est trop lent. Il est également compliqué de pouvoir déterminer génériquement où se trouve le fichier de lancement de Zoom.

  #### INTERFACES
  - new_zoom.py est un script généré automatiquement via QtDesigner, c'est l'interface de la fenêtre principale
  - new_fenetre.py est un script généré automatiquement via QtDesigner, c'est l'interface de la fenêtre d'ajout
  - modif.ui est le fichier crée par QtDesigner, il génère l'interface de la fenêtre de modification/supression

### IMAGES

- start_pic.jpg est une image de chargement
- zoom_app.ico est l'icône présente sur chacune des fenêtres
- btn_join, btn_join2, case, champ_id, champ_mdp sont les images nécessaires nécessaires au fonctionnement de "pyautogui" dans le script "auto_connect.py"
