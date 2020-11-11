import pygame

class Hero():
	'''Класс героя'''
	def __init__(self, ai_settings, screen):
		'''Инициализирует героя и задает его начальную позицию'''
		self.screen = screen
		self.ai_settings = ai_settings

		#Загрузка изображения героя и получения его прямоугольника
		self.image_l = pygame.image.load('images/1.png').convert_alpha()
		#Заркально отражаем героя при движении в противоположную сторону
		self.image_r = pygame.transform.flip(self.image_l, True, False)
		self.image = self.image_l
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

		#Герой появляется у нижнего края экрана
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		#Сохранение вещественной координаты героя
		self.center = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		#Флаг перемещения
		self.moving_right = False
		self.moving_left = False

	def update(self):
		'''Обновляет позицию героя с учетом флага'''
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.speed_hero  
			self.image = self.image_r
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.speed_hero
			self.image = self.image_l
		self.rect.centerx = self.center
	def blitme(self):
		'''Рисует героя в текущей позиции'''
		self.screen.blit(self.image, self.rect)