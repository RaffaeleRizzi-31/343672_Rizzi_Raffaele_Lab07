import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None
    # POPOLA DROPDOWN
    # TODO
    def popola_epoche(self):
        lista_epoche = Model().get_epoche()
        for epoca in lista_epoche:
            self._view._seleziona_artefatti.options.append(ft.dropdown.Option(str(epoca)))
    def popola_musei(self):
        lista_musei = Model().get_musei()
        for museo in lista_musei:
            self._view._seleziona_musei.options.append(ft.dropdown.Option(str(museo)))
    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA ARTEFATTI
    # TODO
    def handler_btn_mostra_artefatti(self, e):
        self.museo_selezionato = self._view._seleziona_musei.value
        self.epoca_selezionata = self._view._seleziona_artefatti.value
        if self.epoca_selezionata == "Nessun filtro":
            self.epoca_selezionata = None
        if self.museo_selezionato == "Nessun filtro":
            self.museo_selezionato = None
        if self.epoca_selezionata is None:
            self._view._seleziona_artefatti.value = "Nessun filtro"
        if self.museo_selezionato is None:
                self._view._seleziona_musei.value = "Nessun filtro"
        self._view.update()
        artefatti_filtrati = Model().get_artefatti_filtrati(self.museo_selezionato, self.epoca_selezionata)
        self._view._lista_risultati.clean()
        if artefatti_filtrati:
            for artefatti in artefatti_filtrati:
                self._view._lista_risultati.controls.append(ft.Text(artefatti))
            self._view.update()
        else:
            self._view.show_alert("Errore")