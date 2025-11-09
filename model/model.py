from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        # TODO
        if museo is not None and epoca is not None:
            id_museo = MuseoDAO.leggi_museo_da_filtro(museo)
            artefatti_museo_epoca_specifica = ArtefattoDAO.leggi_artefatto_museo_epoca_specifici(id_museo, epoca)
            return artefatti_museo_epoca_specifica
        elif museo is None and epoca is None:
            artefatti = ArtefattoDAO.leggi_artefatti()
            return artefatti
        elif museo is not None and epoca is None:
            id_museo = MuseoDAO.leggi_museo_da_filtro(museo)
            artefatti_museo_specifico = ArtefattoDAO.leggi_artefatti_museo_specifico(id_museo)
            return artefatti_museo_specifico
        elif museo is None and epoca is not None:
            artefatti_epoca_specifica = ArtefattoDAO.leggi_artefatti_epoca_specifica(epoca)
            return artefatti_epoca_specifica
        else:
            return None
    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        # TODO
        lista_epoche = []
        iniseme_epoche = set()
        artefatti = ArtefattoDAO.leggi_artefatti()
        for artefatto in artefatti:
            iniseme_epoche.add(artefatto.epoca)
        for epoca in iniseme_epoche:
            lista_epoche.append(epoca)
        return lista_epoche
    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        # TODO
        lista_musei = []
        musei = MuseoDAO.leggi_musei()
        for museo in musei:
            lista_musei.append(museo.nome)
        return lista_musei