class Vokker:
    _datafile = None
    _file_handle = None
    _vok_dict_ = dict()
    _datafolder_ = "data"

    def __init__(self, file):
        self._datafile = file

    def open(self, mode: str = "r"):
        try:
            self._file_handle = open('data/' + self._datafile, mode)
        except FileNotFoundError:
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

    def write_vok(self):
        for key in self._vok_dict_:
            data = f'{key} {self._vok_dict_[key]}\n'
            self._file_handle.write(data)

    def read_vok(self):
        if self._vok_dict_ is not None:
            for data in self._file_handle:
                vok = data.split(" ")
                self._vok_dict_[vok[0]] = vok[1].strip()
                return True
        else:
            # Datafield is not empty, don`t read
            return False

    def close(self):
        self._file_handle.close()
