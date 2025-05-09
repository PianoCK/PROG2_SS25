class IWerkzeug:
    def benutze(self):
        print("Das geht nicht")

class Schaufel(IWerkzeug):
    def benutze(self):
        print("...graben...")

class Hacke(IWerkzeug):
    def benutze(self):
        print("...hacken...")

class Bagger(IWerkzeug):
    def benutze(self):
        print("...bagger...")

class Knecht:
    def __init__(self, werkzeug: IWerkzeug):
        self.werkzeug = werkzeug

    def benutzeWerkzeug(self):
        self.werkzeug.benutze()

    def nehmeWerkzeug(self, werkzeug: IWerkzeug):
        self.werkzeug = werkzeug

hacke = Hacke()

hein = Knecht(hacke)
hein.benutzeWerkzeug()
bagger = Bagger()
hein.nehmeWerkzeug(bagger)
hein.benutzeWerkzeug()