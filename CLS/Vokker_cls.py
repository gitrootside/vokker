class Vokker:
    datafile = None
    file_handle = None

    def __init__(self, file):
        self.datafile = file

    def open(self):
        self.file_handle = open('data/' + self.datafile, "a+")
        return self.file_handle
