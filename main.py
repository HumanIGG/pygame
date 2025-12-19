"""
Duelist Game - 2D fighting game with bot and player vs player modes
Main entry point
"""

import pygame
import sys
from game_state import Game
from settings import Settings

def main():

    pygame.init()

    settings = Settings()
    game = Game(settings)
    game.run()

if __name__ == "__main__":
    main()