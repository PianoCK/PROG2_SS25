from state import *

# Hier ist die spezielle State Machine für einen ATM
# Ich habe dabei die Methoden nicht abstrakt definiert, so dass diese in den Kindklassen vorhanden sind.
class ATMState(State):
    def kontoauszug(self):
        pass
    
    def geld_abheben(self):
        pass
    
    def karte_rein(self):
        pass
    
    def karte_raus(self):
        pass
    
    def problem(self):
        # hier wechseln wir in den Zustand ATMDefekt
        self.context.transition_to(ATMDefekt())

# Der Context ist der ATM selber, der die Befehle an den State deligiert
class ATM(Context):
    def __init__(self, state: State, kontostand: float):
        Context.__init__(self, state)
        self.kontostand = kontostand

    def geld_abheben(self, amount):
        self._state.geld_abheben(amount)

    def karte_einstecken(self):
        self._state.karte_rein()

    def karte_rausnehmen(self):
        self._state.karte_raus()

    def kontoauszug(self):
        self._state.kontoauszug()

    def problem(self):
        self._state.problem()

# Jetzt definieren wir die einzelnen Zustände und was diese im Context machen dürfen 

class ATMDefekt(ATMState):
    pass

class ATMIdle(ATMState):
    def karte_rein(self):
        # hier wechseln wir in den Zustand ATMHatKarte
        self.context.transition_to(ATMHatKarte())

class ATMHatKarte(ATMState):
    def karte_raus(self):
        self.context.transition_to(ATMIdle())

    def kontoauszug(self):
        print(f"Sie haben {self.context.kontostand} Euro auf dem Konto")

    def geld_abheben(self, amount):
        if amount > 0:
            self.context.kontostand -= amount
            print(f"Sie haben {amount} Euro abgehoben")
        else:
            print("Das geht nicht.")

# Automat erstellen und anwenden
print("1. ATM")
atm = ATM(ATMIdle(), 5000)
atm.karte_rausnehmen()
atm.kontoauszug()
atm.karte_einstecken()
atm.kontoauszug()
atm.geld_abheben(2000)
atm.kontoauszug()
atm.karte_rausnehmen()

print()
print("2. ATM")
atm2 = ATM(ATMIdle(), 1000)
atm2.karte_einstecken()
atm2.kontoauszug()
atm2.geld_abheben(150)
atm2.kontoauszug()
atm2.karte_rausnehmen()

