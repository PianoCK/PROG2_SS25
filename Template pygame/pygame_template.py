#########################################################################
# Import:     Alle Abhängigkeiten werden am Anfang eingebunden
#########################################################################

import pygame   # die Spiele-Engine
import random   # Zufallszahlen brauchen wir immer...
import os       # Das Dateisystem

#########################################################################
# Settings:   Hier stehen alle Konstanten Variablen für das Spiel.
#             Diese könnten auch ausgelagert werden in settings.py
#             und per import eingebunden werden
#########################################################################

WIDTH = 400       # Breite des Bildschirms in Pixeln
HEIGHT = 300       # Höhe des Bildschirms in Pixeln
FPS = 60        # Frames per Second (30 oder 60 FPS sind üblicher Standard)

#########################################################################
# Initialisierung:    pygame wird gestartet
#                     und eine Bildschirm-Ausgabe wird generiert
#########################################################################

pygame.init()           # pygame Initialisierung
pygame.mixer.init()     # Die Sound-Ausgabe wird initialisiert
pygame.display.set_caption("My Game")   # Überschrift des Fensters

#########################################################################
# Das Clock-Objekt:    Damit lassen sich Frames und Zeiten messen
#                      Sehr wichtig für Animationen etc.
#########################################################################

clock = pygame.time.Clock()

#########################################################################
# Das screen-Objekt:    Auf dem screen werden alle Grafiken gerendert
# Cooles Feature: pygame.SCALED(verdoppelte Auflösung für einen Retro-Effekt)
#########################################################################

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)

#########################################################################
# Grafiken:    Das Einbinden von Grafiken kann auch ausgelagert werden
#########################################################################

# Das Dateisystem ermittelt das aktuelle Verzeichnis
game_folder = os.path.dirname(__file__)

# Wir binden eine Grafik (Ball) ein
# convert_alpha lässt eine PNG-Datei transparent erscheinen
ball = pygame.image.load(os.path.join(game_folder, 'ball.png')).convert_alpha()
imageRect = ball.get_rect()

#########################################################################
# Game Loop:  Hier ist das Herzstück des Templates
# Im Game Loop laufen immer 5 Phasen ab:
# 1. Wait: Die Zeit zwischen 2 Frames wird mit Wartezeit gefüllt
# 2. Input: Alle (Input-)Events werden verarbeitet (Maus, Tastatur, etc.)
# 3. Update: Alle Sprites werden aktualisert inkl. Spiellogik
# 4. Render: Alle Sprites werden auf den Bildschirm gezeichnet
# 5. Double Buffering: Der Screen wird geswitcht und angezeigt
#########################################################################
running = True

while running:
    #########################################################################
    # 1. Wait-Phase:
    # Die pygame-interne Funktion clock.tick(FPS) berechnet die
    # tatsächliche Zeit zwischen zwei Frames und limitiert diese
    # auf einen Wert(z. B. 1/60). Diese tatsächliche verbrauchte
    # Zeit wird dann bei der Aktualisierung des Spiels benötigt,
    # um dieGeschwindigkeit der Objekte anzupassen.

    dt = clock.tick(FPS) / 1000

    #########################################################################
    # 2. Input-Phase:
    # Mit pygame.event.get() leeren wir den Event-Speicher.
    # Das ist wichtig, sonst läuft dieser voll und das Spiel stürzt ab.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # Windows Close Button?
            running = False             # dann raus aus dem Game Loop

    #########################################################################
    # 3. Update-Phase: Hier ist die komplette Game Logik untergebracht.
    imageRect.topleft = (40,80)


    #########################################################################
    # 4. Render-Phase: Zeichne alles auf den Bildschirm

    # Hintergrund
    screen.fill((255, 255, 255))    # RGB Weiß

    # Zeichne Objekte an Position auf den Screen
    screen.blit(ball, imageRect)

    #########################################################################
    # 5. Double Buffering

    pygame.display.flip()

###########################
# Spiel verlassen: quit

pygame.quit()
