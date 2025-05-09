from __future__ import annotations
from abc import ABC, abstractmethod

class Context:
    _state = None

    def __init__(self, state):
        self.transition_to(state)

    def transition_to(self, newState: State):
        print(f"Context: Transition to {type(newState).__name__}")

        # Die exit()-Methode des alten Zustandes wird noch aufgerufen
        if self._state != None:
            self._state.exit()

        # Der neue Zustand wird gesetzt
        self._state = newState

        # Diese Methode ist am elegantesten, da der ATM ein Context ist und damit self schon bekannt ist.
        # Wir brauchen daher beim Zustandsübergang das eigene Objekt nicht übergeben - es ist schon da.
        self._state.context = self

        # Beim Übergang in einen neuen Zustand wird als erstes enter() aufgerufen
        self._state.enter()

class State(ABC):
    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    def enter(self):
        pass

    def exit(self):
        pass