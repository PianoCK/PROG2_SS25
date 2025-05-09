import abc

class Observer(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def update(self):
        pass

class Subject:
    def __init__(self):
        self.abonennten = []

    def notify(self):
        for abonennt in self.abonennten:
            abonennt.update(self)

    def register(self, user):
        self.abonennten.append(user)

    def unregister(self, user):
        self.abonennten.remove(user)

