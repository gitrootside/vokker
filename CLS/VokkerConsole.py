import os
import sys

from CLS.Vokker import Vokker


class VokkerConsole:
    _menue_: list = list()

    def __init__(self, vokker: Vokker):
        self._vokker_ = vokker
        self._menue_()

    def _menue_(self):
        self._menue_ = [
            '',
            '',
            '   Vokabeltrainer',
            '--------------------',
            '[filename]',
            '(1) öffnen',
            '(2) eingeben',
            '(3) auswerten',
            '(4) speichern',
            '(5) beenden',
            '--------------------',
        ]

    def show_menu(self):

        try:
            s = sys.winver
            os.system("cls")
        except:
            os.system("clear")

        for line in self._menue_:
            if line == '[filename]':
                print('\t\t', str(self._vokker_.datafile).center(20), '\n')
            else:
                print('\t\t',line)

    def imput_menue(self):
        pass
