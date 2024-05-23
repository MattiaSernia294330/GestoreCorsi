import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._pd=None
        self._codice=None
    def leggi_tendina(self,e):
        self._pd=e.control.value
    def leggi_testo(self,e):
        self._codice=e.control.value
    def get_corsi_periodo(self,e):
        if self._pd==None:
            self._view.create_alert("Selezionare un periodo didattico")
            return
        corsi=self._model.get_corsi_periodo(self._pd )
        self._view.list_result.controls.clear()
        for corso in corsi:
            self._view.list_result.controls.append(ft.Text(corso))
        self._view.update_page()
    def get_studenti_periodo(self,e):
        if self._pd==None:
            self._view.create_alert("Selezionare un periodo didattico")
            return
        studenti=self._model.get_studenti_periodo(self._pd )
        self._view.list_result.controls.clear()
        self._view.list_result.controls.append(ft.Text(f"Gli srudenti iscritti a corsi del periodo didattico {self._pd} sono: {studenti}"))
        self._view.update_page()
    def get_studenti_corso(self,e):
        if self._codice==None:
            self._view.create_alert("Selezionare un  corso")
        studenti=self._model.get_studenti_corso(self._codice)
        self._view.list_result.controls.clear()
        if studenti !=[]:
                for studente in studenti:
                    self._view.list_result.controls.append(ft.Text(studente))
        else:
            self._view.list_result.controls.append(ft.Text("Il corso selezionato non ha iscritti o non esiste"))
        self._view.update_page()
    def get_dettaglio_corso(self,e):
        corso=""
        if self._codice==None:
            self._view.create_alert("Selezionare un  corso")
        studenti=self._model.get_studenti_corso(self._codice)
        self._view.list_result.controls.clear()
        if studenti !=[]:
            studenti.sort(key=lambda studente: studente.CDS)
            for studente in studenti:
                if studente.CDS=="":
                    self._view.list_result.controls.append(ft.Text("QUESTI STUDENTI NON SONO ISCRITTI A NESSUN CORSO DI STUDI"))
                    self._view.list_result.controls.append(ft.Text(studente))
                elif studente.CDS!=f"{corso}":
                    corso=studente.CDS
                    self._view.list_result.controls.append(ft.Text(f"QUESTI STUDENTI SONO ISCRITTI AL CORSO {corso}"))
                    self._view.list_result.controls.append(ft.Text(studente))
                else:
                    self._view.list_result.controls.append(ft.Text(studente))
        else:
            self._view.list_result.controls.append(ft.Text("Il corso selezionato non ha iscritti o non esiste"))
        self._view.update_page()

