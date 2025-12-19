"""
Меню и настройки
"""

import pygame
from typing import List, Tuple
from constants import *

class Menu:
    """Класс для управления меню"""

    @staticmethod
    def draw_background_gradient(screen: pygame.Surface, screen_width: int, screen_height: int):
        """Рисует градиентный фон"""
        for y in range(screen_height):
            color_value = int(25 + (y / screen_height) * 20)
            pygame.draw.line(screen, (color_value, color_value + 5, color_value + 10),
                             (0, y), (screen_width, y))

    @staticmethod
    def draw_title(screen: pygame.Surface, font: pygame.font.Font,
                   title_font: pygame.font.Font, screen_width: int):
        """Рисует заголовок меню"""
        title_text = "MORTAL COMBAT 12 (на минималках)"
        title_shadow = title_font.render(title_text, True, (10, 10, 15))
        title_main = title_font.render(title_text, True, HIGHLIGHT_COLOR)

        title_rect = title_main.get_rect(center=(screen_width // 2, 120))
        shadow_rect = title_rect.copy()
        shadow_rect.x += 3
        shadow_rect.y += 3

        screen.blit(title_shadow, shadow_rect)
        screen.blit(title_main, title_rect)

        subtitle = font.render("Version 1.0", True, (160, 160, 180))
        subtitle_rect = subtitle.get_rect(center=(screen_width // 2, 190))
        screen.blit(subtitle, subtitle_rect)

    @staticmethod
    def draw_menu_items(screen: pygame.Surface, font: pygame.font.Font,
                       small_font: pygame.font.Font, menu_items: List[str],
                       selection: int, screen_width: int, screen_height: int):
        """Рисует пункты меню"""
        for i, item in enumerate(menu_items):
            # Определяем цвет и подсветку в зависимости от выбора и наведения мыши
            is_hovered = i == selection
            color = HIGHLIGHT_COLOR if is_hovered else WHITE
            bg_color = (60, 65, 70, 180) if is_hovered else (40, 45, 50, 0)

            # Создаем фоновую панель для пункта меню
            item_width = MENU_ITEM_WIDTH
            item_height = MENU_ITEM_HEIGHT
            item_x = screen_width // 2 - item_width // 2
            item_y = 275 + i * 60

            if is_hovered:
                # Рисуем фоновую панель для подсвеченного пункта
                panel = pygame.Surface((item_width, item_height), pygame.SRCALPHA)
                panel.fill(bg_color)
                screen.blit(panel, (item_x, item_y))

                # Рисуем рамку вокруг панели
                pygame.draw.rect(screen, HIGHLIGHT_COLOR,
                                 (item_x, item_y, item_width, item_height), 2, border_radius=5)

            text = font.render(item, True, color)
            text_rect = text.get_rect(center=(screen_width // 2, 300 + i * 60))
            screen.blit(text, text_rect)

            if is_hovered:
                # Анимированные маркеры выбора
                marker_size = abs(pygame.time.get_ticks() // 50 % 20 - 10) + 15
                left_marker = pygame.Rect(text_rect.left - 50, text_rect.centery - marker_size // 2,
                                          marker_size, marker_size)
                right_marker = pygame.Rect(text_rect.right + 50 - marker_size, text_rect.centery - marker_size // 2,
                                           marker_size, marker_size)
                pygame.draw.rect(screen, HIGHLIGHT_COLOR, left_marker, border_radius=marker_size // 2)
                pygame.draw.rect(screen, HIGHLIGHT_COLOR, right_marker, border_radius=marker_size // 2)