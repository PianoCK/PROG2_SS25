from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self):
        pass

class ObserverSubject:
    def __init__(self):
        self.abonnenten = []

    def register(self, abonnent):
        self.abonnenten.append(abonnent)

    def unregister(self, abonnent):
        self.abonnenten.remove(abonnent)

    def notify(self):
        for abonnent in self.abonnenten:
            abonnent.update(self)

class SnapchatClient(ObserverSubject, Observer):
    def __init__(self, name):
        ObserverSubject.__init__(self)
        self.name = name
        self.snaps = []

    def macheSnap(self, post: str):
        self.snaps.append(post)
        self.notify()

    def update(self, subject):
        print(f"{self.name} hat von {subject.name} einen Snap erhalten:")
        print(f"Der Snap ist >>{subject.snaps[-1]}<<")
        print()

tina = SnapchatClient("Tina")
joerg = SnapchatClient("Jörg")
haman = SnapchatClient("Haman")

tina.register(haman)
tina.register(joerg)

tina.macheSnap("Hi Leute. Ich bin neu hier.")
tina.unregister(joerg)
tina.macheSnap("Ich bin gerade in Paris.")
