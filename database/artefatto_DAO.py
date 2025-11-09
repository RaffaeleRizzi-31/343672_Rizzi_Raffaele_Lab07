from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto
from model.museoDTO import Museo

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    # TODO
    @staticmethod
    def leggi_artefatti():
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Connessione fallita")
            return None
        else:
            artefatti = []
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * 
                       FROM artefatto"""
            cursor.execute(query)
            for row in cursor:
                artefatto = Artefatto(row["id"],
                                      row["nome"],
                                      row["tipologia"],
                                      row["epoca"],
                                      row["id_museo"])
                artefatti.append(artefatto)
            cursor.close()
            cnx.close()
            return artefatti

    @staticmethod
    def leggi_artefatti_museo_specifico(id_msueo):
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Connessione fallita")
            return None
        else:
            artefatti_museo_specifico = []
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * 
                       FROM artefatto
                       WHERE id_museo = %s"""
            cursor.execute(query, (id_msueo,))
            for row in cursor:
                artefatto = Artefatto(row["id"],
                                      row["nome"],
                                      row["tipologia"],
                                      row["epoca"],
                                      row["id_museo"])
                artefatti_museo_specifico.append(artefatto)
            cursor.close()
            cnx.close()
            return artefatti_museo_specifico

    @staticmethod
    def leggi_artefatto_museo_epoca_specifici(id_museo, epoca):
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Connessione fallita")
            return None
        else:
            artefatti_filtrati = []
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * 
                       FROM artefatto
                       WHERE id_museo = %s AND epoca = %s"""
            cursor.execute(query, (id_museo, epoca))
        for row in cursor:
            artefatto = Artefatto(row["id"],
                                  row["nome"],
                                  row["tipologia"],
                                  row["epoca"],
                                  row["id_museo"])
            artefatti_filtrati.append(artefatto)
        cursor.close()
        cnx.close()
        return artefatti_filtrati

    @staticmethod
    def leggi_artefatti_epoca_specifica(epoca):
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Connessione fallita")
            return None
        else:
            artefatti_epoca_specifico = []
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * 
                       FROM artefatto
                       WHERE epoca = %s"""
            cursor.execute(query, (epoca,))
            for row in cursor:
                artefatto = Artefatto(row["id"],
                                      row["nome"],
                                      row["tipologia"],
                                      row["epoca"],
                                      row["id_museo"])
                artefatti_epoca_specifico.append(artefatto)
            cursor.close()
            cnx.close()
            return artefatti_epoca_specifico