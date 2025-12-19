"""
Класс Settings и настройки
"""

from typing import List, Tuple
import constants

class Settings:
    """Класс для хранения настроек игры"""
    def __init__(self):
        self.screen_width = constants.SCREEN_WIDTH
        self.screen_height = constants.SCREEN_HEIGHT
        self.fullscreen = False
        self.borderless = False
        self.current_resolution = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

        # Доступные разрешения
        self.available_resolutions = constants.AVAILABLE_RESOLUTIONS

    def set_resolution(self, width: int, height: int):
        """Установка разрешения экрана"""
        self.current_resolution = (width, height)
        self.screen_width = width
        self.screen_height = height

    def set_fullscreen(self, fullscreen: bool):
        """Установка полноэкранного режима"""
        self.fullscreen = fullscreen
        self.borderless = False

    def set_borderless(self, borderless: bool):
        """Установка режима без рамок"""
        self.borderless = borderless
        self.fullscreen = False

    def get_current_resolution_str(self) -> str:
        """Получение строки текущего разрешения"""
        return f"{self.current_resolution[0]}x{self.current_resolution[1]}"