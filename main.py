from __future__ import annotations
import pygame
from classes.game import Game


def main():
    window = pygame.display.set_mode((1199, 750))
    game = Game(window, 2)
    game.play()


main()
