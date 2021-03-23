class Vokker:
    _datafile_ = None
    _file_handle_ = None
    _vok_dict_ = dict()
    _datafolder_ = "data"

    def __init__(self, file):
        self._datafile_ = file

    def open(self, mode: str = "r"):
        """
        open a vok-file and hold the connection, store the instance in _file_handle_

        :param mode: like in standard-python open
        :return: False if connection failed.... True if connection successful applied
        """
        try:
            self._file_handle_ = open('data/' + self._datafile_, mode)
        except FileNotFoundError:
            return False

        return True

    def add(self, *args):
        if args and len(args) == 2:
            source = args[0]
            translate = args[1]
        else:
            return False  # more than two words

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
            self._file_handle_.write(data)

    def read(self):
        if self._vok_dict_ is not None:
            for data in self._file_handle_:
                vok = data.split(" ")
                self._vok_dict_[vok[0]] = vok[1].strip()
                return True
        else:
            # Datafield is not empty, don`t read
            return False

    def close(self):
        self._file_handle_.close()
