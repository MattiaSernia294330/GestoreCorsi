import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Esercizio Gestore Corsi"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self.title=None
        self.dd_periodo=None
        self.btn_corsi_periodo=None
        self.btn_studenti_periodo=None
        self.txt_codice=None
        self.btn_studenti_corso=None
        self.btn_dettaglio_corso=None
        self.list_result = None

    def load_interface(self):#mettere contenuti
        # title
        self._title = ft.Text("Gestione Corsi", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        #row1
        self.dd_periodo=ft.Dropdown(
            label="Periodo",
            options=[ft.dropdown.Option(key="1"),
                     ft.dropdown.Option(key="2")],
            width=200,
            hint_text="selezionare periodo didattico",
            on_change=self._controller.leggi_tendina
        )
        self.btn_corsi_periodo=ft.ElevatedButton(
            text="Corsi periodo",
            tooltip="metodo per stampare i corsi del periodo didattico",
            width=200,
            on_click=self._controller.get_corsi_periodo
        )
        self.btn_studenti_periodo = ft.ElevatedButton(
            text="Studenti Periodo",
            tooltip="metodo per stampare gli studenti iscritti ai corsi del periodo didattico",
            width=200,
            on_click=self._controller.get_studenti_periodo
        )
        row1=ft.Row([self.dd_periodo,self.btn_corsi_periodo,self.btn_studenti_periodo], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        self._page.update()

        #riga 2
        self.txt_codice=ft.TextField(
            label="Codice corso",
            hint_text="inserire codice di corso",
            width=200,
            on_change=self._controller.leggi_testo
        )
        self.btn_studenti_corso=ft.ElevatedButton(
            text="Studenti corso",
            tooltip="metodo per stampare gli studenti iscritti ad un corso",
            width=200,
            on_click=self._controller.get_studenti_corso
        )
        self.btn_dettaglio_corso = ft.ElevatedButton(
            text="Dettaglio corso",
            tooltip="metodo per stampare il detteglio degli studenti iscritti ad un corso",
            width=200,
            on_click=self._controller.get_dettaglio_corso
        )
        row2=ft.Row([self.txt_codice, self.btn_studenti_corso,self.btn_dettaglio_corso], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)
        self._page.update()
        #result
        self.list_result=ft.ListView(
            expand=1,
            spacing=10,
            padding=20,
            auto_scroll=True
        )
        row3 = ft.Row([self.list_result],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)
        self._page.update()



    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
