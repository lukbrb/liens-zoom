import sqlite3


# ==================================================================================================================== #
#                                         Fonctions pour créer les tables
# ==================================================================================================================== #
def create_tab_cours():
    conn = sqlite3.connect('infozoom.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS info_cours (
            nom_cours TEXT,
            url_cours TEXT)""")


def create_tab_td():
    conn = sqlite3.connect('infozoom.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS infotd (
            nom_td TEXT ,
            url_td TEXT)""")


# ==================================================================================================================== #
#                               Fonctions pour séléctionner des éléments dans les tables
# ==================================================================================================================== #
def show_cm():
    conn = sqlite3.connect('infozoom.db')
    c = conn.cursor()
    c.execute("""SELECT nom_cours FROM info_cours
        ORDER BY nom_cours ASC """)
    items = c.fetchall()
    liste = list(items)
    conn.commit()
    conn.close()
    return liste


def show_urlcm():
    conn = sqlite3.connect('infozoom.db')
    c = conn.cursor()
    c.execute("SELECT url_cours FROM info_cours ")
    items = c.fetchall()
    liste = list(items)
    conn.commit()
    conn.close()
    return liste


def show_td():
    conn = sqlite3.connect('infozoom.db')
    c = conn.cursor()
    c.execute("""SELECT DISTINCT nom_td FROM infotd 
            ORDER BY nom_td ASC  """)
    items = c.fetchall()
    liste = list(items)
    conn.commit()
    conn.close()
    return liste


def show_urltd():
    conn = sqlite3.connect('infozoom.db')
    c = conn.cursor()
    c.execute("SELECT url_td FROM infotd ")
    items = c.fetchall()
    liste = list(items)
    conn.commit()
    conn.close()
    return liste


# ==================================================================================================================== #
#                                Fonctions pour ajouter un élément à une table
# ==================================================================================================================== #

def add_one(cours, td, urlcm, urltd):
    conn = sqlite3.connect('infozoom.db')
    c = conn.cursor()
    c.execute("INSERT INTO info_cours VALUES (?,?,?,?)", (cours, td, urlcm, urltd))
    conn.commit()
    conn.close()


def add_cm(nom, lien):
    conn = sqlite3.connect('infozoom.db')
    c = conn.cursor()
    c.execute("INSERT INTO info_cours VALUES (?,?)", (nom, lien,))
    conn.commit()
    conn.close()


def add_td(nom, lien):
    conn = sqlite3.connect('infozoom.db')
    c = conn.cursor()
    c.execute("INSERT INTO infotd VALUES (?,?)", (nom, lien,))
    conn.commit()
    conn.close()


# Exemple pour ajouter plusieurs éléments d'un coup
def add_many(lists):
    conn = sqlite3.connect('infozoom.db')
    c = conn.cursor()
    c.executemany("INSERT INTO info_cours VALUES (?,?,?,?)", lists)
    conn.commit()
    conn.close()

# ==================================================================================================================== #
#                                Fonctions pour supprimer un élément d'une table
# ==================================================================================================================== #


def delete_one(ids):
    conn = sqlite3.connect('infozoom.db')
    c = conn.cursor()
    c.execute("DELETE FROM info_cours WHERE rowid = (?)", ids)
    conn.commit()
    conn.close()


def delete_cm(ident):
    conn = sqlite3.connect('infozoom.db')
    c = conn.cursor()
    c.execute("DELETE FROM info_cours WHERE rowid = (?)", (ident,))
    conn.commit()
    conn.close()


def delete_td(ident):
    conn = sqlite3.connect('infozoom.db')
    c = conn.cursor()
    c.execute("DELETE FROM infotd WHERE rowid = (?)", (ident,))
    conn.commit()
    conn.close()


# Exemple pour supprimer plusieurs éléments d'un coup
def delete_many(lists):
    conn = sqlite3.connect('infozoom.db')
    c = conn.cursor()
    c.executemany("DELETE FROM info_cours WHERE rowid = (?)", lists)
    conn.commit()
    conn.close()


# ==================================================================================================================== #
#                                Fonctions pour modifier un élément d'une table
# ==================================================================================================================== #

def modify_td(nom, lien, ident):
    conn = sqlite3.connect('infozoom.db')
    c = conn.cursor()
    sql = """UPDATE infotd
                SET nom_td = ?, 
                url_td= ? 
                WHERE rowid=(?)"""
    c.execute(sql, (nom, lien, ident))
    conn.commit()


def modify_cm(nom, lien, ident):
    conn = sqlite3.connect('infozoom.db')
    c = conn.cursor()
    sql = """UPDATE info_cours 
                SET nom_cours = ?, 
                url_cours = ? 
                WHERE rowid=(?)"""
    c.execute(sql, (nom, lien, ident))
    conn.commit()


# ==================================================================================================================== #
#                                Fonctions pour chercher un élément dans une table
# ==================================================================================================================== #
def recherche_cm(objet):
    conn = sqlite3.connect('infozoom.db')
    c = conn.cursor()
    c.execute("SELECT * FROM info_cours WHERE nom_cours = (?)", (objet,))
    items = c.fetchall()
    conn.commit()
    conn.close()
    return items


def recherche_td(objet):
    conn = sqlite3.connect('infozoom.db')
    c = conn.cursor()
    c.execute("SELECT * FROM infotd WHERE nom_td = ?", (objet,))
    items = c.fetchall()
    conn.commit()
    conn.close()
    return items


def recherche_url_cm(ident):
    conn = sqlite3.connect('infozoom.db')
    c = conn.cursor()
    c.execute("SELECT url_cours FROM info_cours WHERE rowid = ?", (ident,))
    items = c.fetchall()
    conn.commit()
    conn.close()
    return items


def recherche_url_td(ident):
    conn = sqlite3.connect('infozoom.db')
    c = conn.cursor()
    c.execute("SELECT url_td FROM infotd WHERE rowid = ?", (ident,))
    items = c.fetchall()
    conn.commit()
    conn.close()
    return items
