import pygame
from hero import Hero
from timer import Timer
from button import Button
import game_functions as gf
from settings import Settings
from game_stat import GameStats
from yummie import load_yum_img
from scoreboard import ScoreBoard

def run_game():
	#Инициализирует игру и создает объект экрана
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Ловец вкусняшек")
	#Назначение фона
	ai_settings.bg = pygame.image.load('images/bg.bmp').convert()
	#Создание группы для вкусняшек
	yummie_gr = pygame.sprite.Group()
	#Загрузка изображений вкусняшек
	load_yum_img()
	#Создание кнопки Play
	play_button = Button(screen, 'Играть')
	#Создание героя
	hero = Hero(ai_settings, screen)
	#Создание секундомера
	timer = Timer(ai_settings, screen)
	#Создание экзмепляров GameStats и ScoreBoard
	stats = GameStats(ai_settings, screen)
	sb = ScoreBoard(ai_settings, screen, stats)
	#Фиксируем fps
	clock = pygame.time.Clock()
	FPS = 60
	#Запуск основого цикла игры
	while True:
		clock.tick(FPS)
		#Отслеживание событий клавиатуры и мыши.
		#print(clock.get_fps())
		gf.check_events(ai_settings, screen, hero, yummie_gr, stats, sb, timer, play_button)
		#Если игра активна, обновление героя и вкусняшек
		if stats.game_active:
			hero.update()
			gf.update_yummie(ai_settings, screen,  yummie_gr, hero, stats, sb, timer, play_button)
		#Обновление экрана
		gf.update_screen(ai_settings, screen, hero, yummie_gr, stats, sb, timer, play_button)

run_game()

