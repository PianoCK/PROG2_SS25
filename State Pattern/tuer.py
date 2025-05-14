
class TuerState:
    def __init__(self, context):
        self.context = context

    def oeffnen(self):
        pass

    def schliessen(self):
        pass

    def klopfen(self):
        print("Klopf klopf")


class OffenState(TuerState):
    def schliessen(self):
        # Hier passiert ein Zustandsübergang von OffenState --> GeschlossenState
        self.context.state = GeschlossenState(self.context)

    def klopfen(self):
        print("Klopf bei offener Tür")
    

class GeschlossenState(TuerState):
    def oeffnen(self):
        # Hier passiert ein Zustandsübergang von GeschlossenState --> OffenState
        self.context.state = OffenState(self.context)

    def klopfen(self):
        print("Klopf bei geschlossener Tür")

# Context
class Tuer:
    def __init__(self):
        #self.state = OffenState()
        self.state = GeschlossenState(self)

    def oeffnen(self):
        self.state.oeffnen()

    def schliessen(self):
        self.state.schliessen()

    def klopfen(self):
        self.state.klopfen()

haustuer = Tuer()
haustuer.klopfen()
haustuer.oeffnen()
haustuer.klopfen()
haustuer.schliessen()
