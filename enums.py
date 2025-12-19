"""
Перечисления (Enum-классы)
"""

from enum import Enum

class GameState(Enum):
    """Состояния игры"""
    MENU = "menu"
    CHARACTER_SELECT_P1 = "character_select_p1"  # Выбор персонажа для игрока 1
    CHARACTER_SELECT_P2 = "character_select_p2"  # Выбор персонажа для игрока 2
    PLAYER_VS_PLAYER = "player_vs_player"
    PLAYER_VS_BOT = "player_vs_bot"
    SETTINGS = "settings"
    CONTROLS = "controls"
    EXIT = "exit"

class BodyType(Enum):
    """Типы телосложения персонажей"""
    ATHLETIC = "athletic"     # Атлетическое (мускулистое)
    LEAN = "lean"             # Худощавое
    HEAVY = "heavy"           # Тяжелое (крупное)
    SUMO = "sumo"             # Сумоист
    NINJA = "ninja"           # Ниндзя (гибкое)
    ROBOTIC = "robotic"       # Роботизированное