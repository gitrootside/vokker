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
            '[filename]',
            '(1) öffnen',
            '(2) eingeben',
            '(3) auswerten',
            '(4) speichern',
            '(5) beenden\n',
        ]

    def show_menu(self):
        for line in self._menue_:
            if line == '[filename]':
                print(str(self._vokker_.datafile).center(20),'\n')
            else:
                print(line)

    def imput_menue(self):
        pass
