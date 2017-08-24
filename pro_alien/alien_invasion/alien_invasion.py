# coding=utf-8

import pygame
from setting import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建Play 按钮
    play_button = Button(ai_setting, screen, "Play")

    # 创建存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_setting)
    sb = ScoreBoard(ai_setting, screen, stats)

    # 创建一艘飞船
    ship = Ship(ai_setting, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_setting, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_setting, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_setting, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_setting, stats, sb, screen, ship, aliens, bullets)

        gf.update_screen(ai_setting, stats, sb, screen, ship, aliens, bullets, play_button)


run_game()
