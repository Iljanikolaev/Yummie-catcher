import time
import pygame.font

class Timer():
	'''Секундомер'''
	def __init__(self, ai_settings, screen):
		'''Инициализируем атрибуты секундомера'''
		self.ai_settings = ai_settings
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.t_0 = time.time()
		#Настройка шрифта секундомера
		self.font = pygame.font.SysFont(None, 60)
		self.text_color = (30, 30, 30)
		
	def start_time(self):
		'''Старт секундомера'''
		self.t_0 = time.time()

	def show_time(self):
		'''Выводит время секундомера на экран'''
		self.image_time = self.font.render(str(round(time.time() - self.t_0)), True, self.text_color).convert_alpha()
		self.rect_time = self.image_time.get_rect()
		self.rect_time.centerx = self.screen_rect.centerx
		self.rect_time.top = self.screen_rect.top + 20

		self.screen.blit(self.image_time, self.rect_time)
	def game_over_time(self):
		'''Возвращает время секундомера в конце игры'''
		return str(round(time.time() - self.t_0))
