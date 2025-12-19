"""
Выбор персонажа
"""

import pygame
from typing import List, Tuple
from constants import *
from enums import BodyType
from colors import ColorPalette

class CharacterSelectUI:
    """UI для выбора персонажа"""

    @staticmethod
    def draw_background(screen: pygame.Surface):
        """Рисует фон для выбора персонажа"""
        screen.fill((30, 35, 40))

    @staticmethod
    def draw_title(screen: pygame.Surface, title_font: pygame.font.Font,
                  font: pygame.font.Font, player_name: str,
                  mode_text: str, screen_width: int):
        """Рисует заголовок выбора персонажа"""
        title = title_font.render(f"ВЫБОР ПЕРСОНАЖА - {player_name}", True, (230, 110, 110))
        title_rect = title.get_rect(center=(screen_width // 2, 80))
        screen.blit(title, title_rect)

        subtitle = font.render(f"Режим: {mode_text}", True, HIGHLIGHT_COLOR)
        subtitle_rect = subtitle.get_rect(center=(screen_width // 2, 140))
        screen.blit(subtitle, subtitle_rect)

    @staticmethod
    def draw_arrows(screen: pygame.Surface, screen_width: int,
                   left_hovered: bool, right_hovered: bool):
        """Рисует стрелки для навигации"""
        left_arrow_rect = pygame.Rect(screen_width // 2 - 200, 400, 50, 50)
        right_arrow_rect = pygame.Rect(screen_width // 2 + 150, 400, 50, 50)

        # Левая стрелка
        left_color = HIGHLIGHT_COLOR if left_hovered else WHITE
        pygame.draw.polygon(screen, left_color, [
            (left_arrow_rect.centerx + 10, left_arrow_rect.top + 10),
            (left_arrow_rect.centerx + 10, left_arrow_rect.bottom - 10),
            (left_arrow_rect.left + 10, left_arrow_rect.centery)
        ])
        pygame.draw.rect(screen, left_color, left_arrow_rect, 2, border_radius=5)

        # Правая стрелка
        right_color = HIGHLIGHT_COLOR if right_hovered else WHITE
        pygame.draw.polygon(screen, right_color, [
            (right_arrow_rect.centerx - 10, right_arrow_rect.top + 10),
            (right_arrow_rect.centerx - 10, right_arrow_rect.bottom - 10),
            (right_arrow_rect.right - 10, right_arrow_rect.centery)
        ])
        pygame.draw.rect(screen, right_color, right_arrow_rect, 2, border_radius=5)

    @staticmethod
    def draw_color_palette(screen: pygame.Surface, screen_width: int,
                          color_selection: int, mouse_pos: Tuple[int, int],
                          small_font: pygame.font.Font):
        """Рисует палитру цветов"""
        color_names = ColorPalette.get_palette_names()
        color_display_names = ColorPalette.get_display_names()
        color_values = [ColorPalette.get_palette(name)["body"] for name in color_names]

        color_start_x = screen_width // 2 - (len(color_names) * 50) // 2
        for i, (color, name) in enumerate(zip(color_values, color_display_names)):
            color_x = color_start_x + i * 50
            color_rect = pygame.Rect(color_x, 650, 45, 45)

            # Проверяем наведение на цвет
            color_hovered = color_rect.collidepoint(mouse_pos)

            border_color = HIGHLIGHT_COLOR if (i == color_selection or color_hovered) else LIGHT_GRAY
            border_width = 3 if (i == color_selection or color_hovered) else 1

            pygame.draw.rect(screen, color, color_rect, border_radius=10)
            pygame.draw.rect(screen, border_color, color_rect, border_width, border_radius=10)

            if i == color_selection or color_hovered:
                name_text = small_font.render(name, True, HIGHLIGHT_COLOR)
                name_rect = name_text.get_rect(center=(color_rect.centerx, color_rect.bottom + 20))
                screen.blit(name_text, name_rect)

    @staticmethod
    def draw_button(screen: pygame.Surface, medium_font: pygame.font.Font,
                   button_text: str, button_y: int, button_width: int,
                   button_height: int, screen_width: int,
                   is_hovered: bool):
        """Рисует кнопку"""
        button_x = screen_width // 2 - button_width // 2

        button_color = HIGHLIGHT_COLOR if is_hovered else (70, 75, 80)
        button_text_color = WHITE if is_hovered else LIGHT_GRAY

        # Рисуем кнопку
        pygame.draw.rect(screen, button_color,
                         (button_x, button_y, button_width, button_height), border_radius=10)
        pygame.draw.rect(screen, WHITE,
                         (button_x, button_y, button_width, button_height), 2, border_radius=10)

        button_surface = medium_font.render(button_text, True, button_text_color)
        button_rect = button_surface.get_rect(
            center=(screen_width // 2, button_y + button_height // 2))
        screen.blit(button_surface, button_rect)