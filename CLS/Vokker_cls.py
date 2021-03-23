class Vokker:
    _datafile = None
    _file_handle = None
    _vok_dict_ = dict()

    def __init__(self, file):
        self._datafile = file

    def open(self, mode: str = "r"):
        try:
            self._file_handle = open('data/' + self._datafile, mode)
        except FileNotFoundError:
            # self._file_handle = open('data/' + self._datafile)
            # self._file_handle.close()
            # self._file_handle = open('data/' + self._datafile, "a")
            pass

        return self._file_handle

    def add_vok(self, source, translate):
        if source not in self._vok_dict_:
            self._vok_dict_[source] = translate
            return True
        else:
            return False

    def get_vok_dict(self):
        return self._vok_dict_

    def write(self):

        for key in self._vok_dict_:
            data = f'{key} {self._vok_dict_[key]}\n'
            self._file_handle.write(data)
            print(key, self._vok_dict_[key])

    def close(self):
        pass
