from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    # TODO
    @staticmethod
    def leggi_musei():
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Connessione fallita")
            return None
        else:
            musei = []
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * 
                       FROM museo"""
            cursor.execute(query)
            for row in cursor:
                museo = Museo(row["id"],
                              row["nome"],
                              row["tipologia"],)
                musei.append(museo)
            cursor.close()
            cnx.close()
            return musei
    @staticmethod
    def leggi_museo_da_filtro(nome_museo):
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Connessione fallita")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT id 
                       FROM museo
                       WHERE nome = %s"""
            cursor.execute(query, (nome_museo,))
            id = cursor.fetchone()["id"]
            cursor.close()
            cnx.close()
            return id