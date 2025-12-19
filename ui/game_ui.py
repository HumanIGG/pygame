"""
Игровой интерфейс
"""

import pygame
import random
from typing import Tuple
from constants import *

class GameUI:
    """UI для игрового экрана"""

    @staticmethod
    def draw_ground(screen: pygame.Surface, screen_width: int, screen_height: int):
        """Рисует землю с текстурой"""
        ground_height = GROUND_HEIGHT
        ground_y = screen_height - ground_height

        # Текстура земли
        for y in range(ground_y, screen_height, 4):
            line_color = (40 + (y - ground_y)//2, 45 + (y - ground_y)//2, 50 + (y - ground_y)//2)
            pygame.draw.line(screen, line_color, (0, y), (screen_width, y))

        # Трава
        grass_color = (45, 65, 45)
        for x in range(0, screen_width, 10):
            grass_height = random.randint(5, 15)
            grass_points = [
                (x, ground_y),
                (x + 3, ground_y - grass_height),
                (x + 7, ground_y - grass_height//2),
                (x + 10, ground_y)
            ]
            pygame.draw.polygon(screen, grass_color, grass_points)

        # Центральная линия арены
        center_x = screen_width // 2
        line_length = 200
        pygame.draw.line(screen, (85, 90, 95, 150),
                        (center_x, ground_y - line_length),
                        (center_x, ground_y), 3)

    @staticmethod
    def draw_health_bar(screen: pygame.Surface, font: pygame.font.Font,
                       player_name: str, player_health: int, player_max_health: int,
                       x: int, y: int, is_right_aligned: bool = False):
        """Рисует полосу здоровья"""
        health_percent = player_health / player_max_health
        health_width = 300 * health_percent

        health_color = (70, 210, 90) if health_percent > 0.5 else (230, 210, 70) if health_percent > 0.25 else (230, 70, 70)

        if is_right_aligned:
            x -= 304

        pygame.draw.rect(screen, (40, 45, 50), (x, y, 304, 34), border_radius=6)
        pygame.draw.rect(screen, health_color, (x + 2, y + 2, health_width, 30), border_radius=5)
        pygame.draw.rect(screen, (190, 195, 200), (x, y, 304, 34), 2, border_radius=6)

        health_text = f"{player_name}: {player_health}/{player_max_health}"
        health_surface = font.render(health_text, True, WHITE)

        if is_right_aligned:
            text_x = x + 304 - health_surface.get_width() - 5
        else:
            text_x = x + 5

        screen.blit(health_surface, (text_x, y + 5))

    @staticmethod
    def draw_game_info(screen: pygame.Surface, font: pygame.font.Font, small_font: pygame.font.Font,
                      p1_name: str, p1_health: int, p1_max_health: int,
                      p2_name: str, p2_health: int, p2_max_health: int,
                      round_time: int, screen_width: int):
        """Рисует игровую информацию"""
        # Верхняя панель
        top_panel = pygame.Surface((screen_width, 80), pygame.SRCALPHA)
        top_panel.fill((20, 25, 30, 220))
        screen.blit(top_panel, (0, 0))

        # Время раунда
        minutes = round_time // 3600
        seconds = (round_time % 3600) // 60
        time_text = f"{minutes:02d}:{seconds:02d}"
        time_surface = font.render(time_text, True, (230, 190, 90))
        time_rect = time_surface.get_rect(center=(screen_width // 2, 40))
        screen.blit(time_surface, time_rect)

        # Здоровье игрока 1
        GameUI.draw_health_bar(screen, font, p1_name, p1_health, p1_max_health, 20, 20)

        # Здоровье игрока 2
        GameUI.draw_health_bar(screen, font, p2_name, p2_health, p2_max_health,
                              screen_width - 20, 20, is_right_aligned=True)

        # Информация об ударах до победы
        hits_to_win_p1 = max(0, (p1_health + 9) // 10)
        hits_to_win_p2 = max(0, (p2_health + 9) // 10)

        hits_text = f"Ударов до победы: {hits_to_win_p1} - {hits_to_win_p2}"
        hits_surface = small_font.render(hits_text, True, (250, 230, 110))
        hits_rect = hits_surface.get_rect(center=(screen_width // 2, 70))
        screen.blit(hits_surface, hits_rect)

    @staticmethod
    def draw_winner_screen(screen: pygame.Surface, winner: str,
                          stats_text: str, hits_text: str, time_text: str,
                          screen_width: int, screen_height: int):
        """Рисует экран победителя"""
        overlay = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 200))
        screen.blit(overlay, (0, 0))

        win_font = pygame.font.Font(None, 96)
        win_text = win_font.render("ПОБЕДА!", True, (250, 210, 90))
        win_rect = win_text.get_rect(center=(screen_width // 2, screen_height // 2 - 100))
        screen.blit(win_text, win_rect)

        winner_font = pygame.font.Font(None, 120)
        winner_text = winner_font.render(winner, True, HIGHLIGHT_COLOR)
        winner_rect = winner_text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(winner_text, winner_rect)

        stats_font = pygame.font.Font(None, 36)

        stats_surface = stats_font.render(stats_text, True, WHITE)
        hits_surface = stats_font.render(hits_text, True, WHITE)
        time_surface = stats_font.render(time_text, True, WHITE)

        stats_rect = stats_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 80))
        hits_rect = hits_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 120))
        time_rect = time_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 160))

        screen.blit(stats_surface, stats_rect)
        screen.blit(hits_surface, hits_rect)
        screen.blit(time_surface, time_rect)

        continue_text = stats_font.render("Нажмите ESC для возврата в меню", True, LIGHT_GRAY)
        continue_rect = continue_text.get_rect(center=(screen_width // 2, screen_height - 100))
        screen.blit(continue_text, continue_rect)