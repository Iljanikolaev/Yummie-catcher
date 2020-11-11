import pygame

class Settings():
	'''Класс для хранения всех настроек игры Yummie Catcher(Ловец Вкусняшек)'''
	def __init__(self):
		'''Инициализирует настройк игры'''
		#Параметры экрана
		self.screen_width = 1024
		self.screen_height = 688
		self.bg = pygame.image.load('images/bg.bmp')
		self.bg_rect = self.bg.get_rect()
		#Настройка скорости героя
		self.speed_hero = 12
		#Настройка скорости падения вкусняшек
		self.speed_yummie = 15