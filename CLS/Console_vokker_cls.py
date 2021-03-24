from CLS.Vokker_cls import Vokker


class Vokker_Console:

    def __init__(self, vokker: Vokker):
        self._vokker_ = vokker

    def _menue_(self):

        self._menue_=list(
            '   Vokabeltrainer',
            '--------------------',
            '[ aktuelle Lektion]\n',
            '(1) öffnen',
            '(2) eingeben',
            '(3) auswerten',
            '(4) speichern',
            '(5) beenden'.
        )

    def show_menu(self):
        for line in self._vokker_:
            print(line)

    def imput_menue(self):
        pass
