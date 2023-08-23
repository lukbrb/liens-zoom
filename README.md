# Courlien

Premier vrai projet de programmation. Crée dans l'idée de sauvegarder les liens Zoom de mes cours lors du confinement.
`Courlien` peut également être utilisé pour sauvegarder ses favoris ou quoique ce soit d'autre de la forme `clé : valeur`. **Attention** néanmoins,
la valeur n'est pas crypté lors de la sauvegarde dans la base de données.

Lors du lancement du logiciel, la page suivante s'affiche :

![Page d'accueil](courliens/imgs/accueil.png)

`Courlien` propose plusieurs fonctionnalités :

## 1 - Ajout

On peut ajouter des liens en cliquant sur le texte `Ajouter`. La page suivante s'ouvrira alors :

![Ajouter lien](courliens/imgs/ajout.png)

Il suffit ensuite d'entrer le nom du cours, ou une quelconque `clé`, d'y associer une `valeur` ainsi qu'une catégorie (cours, TD ou les deux) puis de cliquer sur `Ajouter` pour enregistrer ce qui a été saisi. Il est possible d'enregistrer plusieurs liens à la suite. Une fois les liens désirés enregistrés, il suffit de cliquer sur `Terminé` pour quitter la fenêtre d'ajout.

## 2 - Modification/Suppression

En cliquant sur le texte `Modifier/Supprimer`, on accède à la pgae suivante :

![Modification lien](courliens/imgs/modifier.png)

Cette page nous donne un aperçu de la base de données, et nous permet d'éditer le lien séléctionné, qui apparaît d'une couleur différente.

Pour modifier, on clique sur l'item à modifier, on change les valeurs souhaitées dans les champs de texte à droite, puis l'on clique sur `Modifier`.

Pour supprimer, il suffit de cliquer sur l'item souhaité et d'ensuité cliquer sur `Supprimer`.

### Note du 23/08/2023

Les liens ne correspondent pas aux titres de la combobox. Corriger la manière dont les combobox sont créées.
Réparé.

## Note dy 24/08/2023

1. Enlever ou modifier les élements supprimés ou modifiés de la combobox lorque retour à page d'accueil
2. Réduire redondance des fonctions TD puis CM dans le code UI, et dans les fonctions de la base de données.
