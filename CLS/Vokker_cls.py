class Vokker:
    datafile = None
    file_handle = None

    def __init__(self, file):
        self.datafile = file

    def open(self):
        try:
            self.file_handle = open('data/' + self.datafile, "a+")
        except FileNotFoundError:
            self.file_handle = open('data/' + self.datafile)
            self.file_handle.close()
            self.file_handle = open('data/' + self.datafile, "a+")


        return self.file_handle
