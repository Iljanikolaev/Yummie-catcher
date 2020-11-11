import pygame.font

class Button():
	'''Класс кнопки'''
	def __init__(self, screen, msg):
		'''Инициализирует атрибуты кнопки'''
		self.screen = screen
		self.screen_rect = screen.get_rect()
		#Назначения размера и свойств кнопки
		self.width, self.height = 1000, 100
		self.text_color = (255, 255 ,255)
		self.button_color = (0, 50, 120)
		self.font = pygame.font.SysFont(None, 48)
		#Построение объекта rect и выравнивание его по центру
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		#Создание сообщения кнопки
		self.prep_msg(msg)

	def prep_msg(self, msg):
		'''Преобразует msg в прямоугольник и выравнивает текс по центру'''
		self.msg_image = self.font.render(msg, True, self.text_color).convert_alpha()
		self.msg_rect = self.msg_image.get_rect()
		self.msg_rect.center = self.screen_rect.center

	def draw_button(self):
		'''Отображение пустой кнопки и вывод сообщения'''
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_rect)