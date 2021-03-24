from CLS.Vokker import Vokker


class VokkerConsole:
    _menue_: list = list()

    def __init__(self, vokker: Vokker):
        self._vokker_ = vokker
        self._menue_()

    def _menue_(self):
        self._menue_ = [
            '   Vokabeltrainer',
            '--------------------',
            '[ aktuelle Lektion]\n',
            '(1) öffnen',
            '(2) eingeben',
            '(3) auswerten',
            '(4) speichern',
            '(5) beenden',
        ]

    def show_menu(self):
        for line in self._menue_:
            print(line)

    def imput_menue(self):
        pass