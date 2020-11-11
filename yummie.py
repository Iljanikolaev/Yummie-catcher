import pygame
from pygame.sprite import Sprite
import random

#Список,в который будет содержать изображения вкусняшек
yummie_img = []
def load_yum_img():
	'''Функция загрузки изображений вкусняшек'''
	for i in range(3, 7):
		yummie_img.append(pygame.image.load('images/' + str(i) + '.png').convert_alpha())

class Yummie(Sprite):
	'''Класс представляющий одну вкусняшку'''
	def __init__(self, ai_settings, screen, hero):
		'''Инициализирует случайную вкусняшку и задает её начальную поцизию'''
		super().__init__()
		self.ai_settings = ai_settings
		self.screen = screen
		self.obj = random.randint(0, 3)
		self.image = yummie_img[self.obj]
		self.rect = self.image.get_rect()
		#Вкусняшка появляется в случайном месте над экраном
		self.rect.centerx = random.randint(10, ai_settings.screen_width - 10)
		self.rect.centery = random.randint(-ai_settings.screen_height, 0)
		#Сохранение точной позиции вкусняхи
		self.y = float(self.rect.y)

	def update(self):
		'''Осуществляет падение вниз вкусняшки'''
		self.y += self.ai_settings.speed_yummie
		self.rect.y = self.y

	def blitme(self):
		'''Выводит вкусняшку в текущем положении'''
		pygame.screen.blit(self.image, self.rect)