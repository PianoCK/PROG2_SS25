from __future__ import annotations
from observer import Observer, Subject

class SnapchatUser(Observer, Subject):
    def __init__(self, benutzername):
        Subject.__init__(self)
        self.benutzername = benutzername
        self.snaps = []

    def update(self, user: SnapchatUser):
        print(f"{self.benutzername}: {user.benutzername} hat einen Snap gesendet: {user.letzter_snap()}")

    def post(self, snap):
        self.snaps.append(snap)
        self.notify()

    def letzter_snap(self):
        return self.snaps[-1]

claire = SnapchatUser("Clairy")
tom = SnapchatUser("Tommy")
marie = SnapchatUser("Marie")
claire.register(tom)
claire.register(marie)
claire.post("Hi. Ich bin gerade in Schwerin!")
claire.post("Happy Helloween")
tom.post("Hi. Wir auf Tour.")