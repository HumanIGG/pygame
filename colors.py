"""
Цветовые палитры
"""

from typing import Dict, List, Tuple

class ColorPalette:
    """Цветовые палитры для персонажей"""
    PALETTES = {
        "default": {
            "body": (30, 30, 40),
            "highlight": (60, 60, 80),
            "attack": (220, 60, 60),
            "block": (60, 120, 220),
        },
        "red": {
            "body": (50, 20, 25),
            "highlight": (80, 40, 45),
            "attack": (240, 80, 80),
            "block": (80, 160, 240),
        },
        "blue": {
            "body": (20, 30, 50),
            "highlight": (40, 60, 90),
            "attack": (240, 100, 60),
            "block": (100, 180, 250),
        },
        "green": {
            "body": (25, 40, 25),
            "highlight": (45, 70, 45),
            "attack": (230, 80, 80),
            "block": (80, 180, 230),
        },
        "purple": {
            "body": (40, 20, 50),
            "highlight": (70, 40, 80),
            "attack": (240, 120, 60),
            "block": (120, 80, 240),
        },
        "gold": {
            "body": (60, 50, 30),
            "highlight": (90, 80, 50),
            "attack": (240, 140, 60),
            "block": (140, 200, 240),
        }
    }

    @staticmethod
    def get_palette(name: str) -> Dict[str, Tuple[int, int, int]]:
        """Возвращает цветовую палитру по имени"""
        return ColorPalette.PALETTES.get(name, ColorPalette.PALETTES["default"])

    @staticmethod
    def get_palette_names() -> List[str]:
        """Возвращает список имен всех палитр"""
        return list(ColorPalette.PALETTES.keys())

    @staticmethod
    def get_display_names() -> List[str]:
        """Возвращает отображаемые имена палитр"""
        return ["По умолчанию", "Красный", "Синий", "Зеленый", "Фиолетовый", "Золотой"]