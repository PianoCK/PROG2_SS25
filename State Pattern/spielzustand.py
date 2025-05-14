class ISpielState:
    def update(self):
        pass

    def render(self):
        pass

class TitelBildschirm(ISpielState):
    pass

class ImSpiel(ISpielState):
    def update(self):
        for sprite in sprites:
            sprite.update()

class Achievement(ISpielState):
    pass

class GameOver(ISpielState):
    pass



