class Vokker:
    _datafile = None
    _file_handle = None
    _vok_dict_ = dict()

    def __init__(self, file):
        self._datafile = file

    def open(self):
        try:
            self._file_handle = open('data/' + self._datafile, "a+")
        except FileNotFoundError:
            self._file_handle = open('data/' + self._datafile)
            self._file_handle.close()
            self._file_handle = open('data/' + self._datafile, "a+")

        return self._file_handle

    def add_vok(self, source, translate):

        if source not in self._vok_dict_:
            self._vok_dict_[source] = translate
            return True
        else:
            return False

    def get_vok_dict(self):
        return self._vok_dict_
