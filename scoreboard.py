import pygame.font

class ScoreBoard():
	'''Класс вывода игровой информации'''
	def __init__(self, ai_settings, screen, stats):
		'''Инициализирует атрибуты подсчета очков.'''
		self.ai_settings = ai_settings
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.stats = stats

		#Настройка шрифт для вывода счета
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)
		#Создание объектов счета
		self.prep_score_pizza()
		self.prep_score_cheetos()
		self.prep_score_cake()
		self.prep_score_cola()
		#Создание иконок вкусняшек
		self.pizza()
		self.cheetos()
		self.cake()
		self.cola()
		#Создание объекта рекорда
		self.prep_record()


	def prep_score_pizza(self):
		#Создание объекта счета пойманной игроком пиццы
		self.score_image_pizza = self.font.render(str(self.stats.score_pizza)+ '/100', True, self.text_color).convert_alpha()
		self.score_rect_pizza = self.score_image_pizza.get_rect()
		#Счет располагается в верхнем левом углу
		self.score_rect_pizza.top = 20
		self.score_rect_pizza.left = 50


	def prep_score_cheetos(self):
		#Создание объекта счета пойманных игроком пачек чипсов
		self.score_image_cheetos = self.font.render(str(self.stats.score_cheetos) + '/100', True, self.text_color).convert_alpha()
		self.score_rect_cheetos = self.score_image_cheetos.get_rect()
		#Счет располагается слева, под счетом пиццы
		self.score_rect_cheetos.top = self.score_rect_pizza.bottom
		self.score_rect_cheetos.left = self.score_rect_pizza.left


	def prep_score_cake(self):
		#Создание объекта счета пойманных игроком кусков торта
		self.score_image_cake = self.font.render(str(self.stats.score_cake)+ '/100', True, self.text_color).convert_alpha()
		self.score_rect_cake = self.score_image_cake.get_rect()
		#Счет располагается слева, под счетом чипсов
		self.score_rect_cake.top = self.score_rect_cheetos.bottom
		self.score_rect_cake.left = self.score_rect_cheetos.left


	def prep_score_cola(self):
		#Создание объекта счета пойманных игроком стаканов колы
		self.score_image_cola = self.font.render(str(self.stats.score_cola)+ '/100', True, self.text_color).convert_alpha()
		self.score_rect_cola = self.score_image_cola.get_rect()
		#Счет располагается слева, под счетом кусков торта
		self.score_rect_cola.top = self.score_rect_cake.bottom
		self.score_rect_cola.left = self.score_rect_cake.left


	def pizza(self):
		#Создание иконки пиццы
		self.image_pizza = pygame.image.load('images/3.png').convert_alpha()
		self.image_pizza = pygame.transform.scale(self.image_pizza, (40, 40))
		self.rect_pizza = self.image_pizza.get_rect()
		#Иконка пиццы располагается слева от счета пиццы
		self.rect_pizza.bottom = self.score_rect_pizza.bottom
		self.rect_pizza.right = self.score_rect_pizza.left
		#Создание галочки, в случае сбора необходимого количества пиццы
		self.its_ok_pizza_image = pygame.image.load('images/7.png').convert_alpha()
		self.its_ok_pizza_image = pygame.transform.scale(self.its_ok_pizza_image, (40, 40))
		self.rect_its_ok_pizza_image = self.its_ok_pizza_image.get_rect()
		#Галочка располагается справа от счета пиццы
		self.rect_its_ok_pizza_image.bottom = self.rect_pizza.bottom 
		self.rect_its_ok_pizza_image.left = self.score_rect_pizza.right + 35


	def cheetos(self):
		#Создание иконки чипсов
		self.image_cheetos = pygame.image.load('images/4.png').convert_alpha()
		self.image_cheetos = pygame.transform.scale(self.image_cheetos, (40, 40))
		self.rect_cheetos = self.image_cheetos.get_rect()
		#Иконка чипсов распполагается слева от счета чипсов
		self.rect_cheetos.bottom = self.score_rect_cheetos.bottom
		self.rect_cheetos.right = self.score_rect_cheetos.left
		#Создание галочки, в случае сбора необходимого количества пачек чипсов
		self.its_ok_cheetos_image = pygame.image.load('images/7.png').convert_alpha()
		self.its_ok_cheetos_image = pygame.transform.scale(self.its_ok_cheetos_image, (40, 40))
		self.rect_its_ok_cheetos_image = self.its_ok_cheetos_image.get_rect()
		#Галочка располагается справа от счета пачек чипсов
		self.rect_its_ok_cheetos_image.bottom = self.rect_cheetos.bottom 
		self.rect_its_ok_cheetos_image.left = self.score_rect_cheetos.right + 35


	def cake(self):
		#Создание иконки куска торта
		self.image_cake = pygame.image.load('images/5.png').convert_alpha()
		self.image_cake = pygame.transform.scale(self.image_cake, (40, 40))
		self.rect_cake = self.image_cake.get_rect()
		#Иконка куска торта распполагается слева от счета кусков торта
		self.rect_cake.bottom = self.score_rect_cake.bottom
		self.rect_cake.right = self.score_rect_cake.left
		#Создание галочки, в случае сбора необходимого количества кусков торта
		self.its_ok_cake_image = pygame.image.load('images/7.png').convert_alpha()
		self.its_ok_cake_image = pygame.transform.scale(self.its_ok_cake_image, (40, 40))
		self.rect_its_ok_cake_image = self.its_ok_cake_image.get_rect()
		#Галочка располагается справа от счета кусков торта
		self.rect_its_ok_cake_image.bottom = self.rect_cake.bottom 
		self.rect_its_ok_cake_image.left = self.score_rect_cake.right + 35


	def cola(self):
		#Создание иконки стакана колы
		self.image_cola = pygame.image.load('images/6.png').convert_alpha()
		self.image_cola = pygame.transform.scale(self.image_cola, (40, 40))
		#Иконка стакана колы располагается слева от счета стаканов колы
		self.rect_cola = self.image_cola.get_rect()
		self.rect_cola.bottom = self.score_rect_cola.bottom
		self.rect_cola.right = self.score_rect_cola.left
		#Создание галочки, в случае сбора необходимого количества стаканов колы
		self.its_ok_cola_image = pygame.image.load('images/7.png').convert_alpha()
		self.its_ok_cola_image = pygame.transform.scale(self.its_ok_cake_image, (40, 40))
		self.rect_its_ok_cola_image = self.its_ok_cola_image.get_rect()
		#Галочка располагается справа от счета стаканов колы
		self.rect_its_ok_cola_image.bottom = self.rect_cola.bottom 
		self.rect_its_ok_cola_image.left = self.score_rect_cola.right + 35


	def prep_record(self):
		#Создание объекта рекорда
		self.image_record = self.font.render('Рекорд : ' + str(self.stats.record) + ' c.', True, self.text_color)
		self.record_rect = self.image_record.get_rect()
		#Рекорд располагается справа сверху
		self.record_rect.right = self.screen_rect.right - 10
		self.record_rect.top = self.score_rect_pizza.top
		
	
	def show_score(self):
		'''Выводит игровую информацию на экран'''
		#Выводит на экран счет
		self.screen.blit(self.score_image_pizza, self.score_rect_pizza)
		self.screen.blit(self.score_image_cheetos, self.score_rect_cheetos)
		self.screen.blit(self.score_image_cake, self.score_rect_cake)
		self.screen.blit(self.score_image_cola, self.score_rect_cola)
		#Выводит на экран иконки вкусняшек
		self.screen.blit(self.image_pizza, self.rect_pizza)
		self.screen.blit(self.image_cheetos, self.rect_cheetos)
		self.screen.blit(self.image_cake, self.rect_cake)
		self.screen.blit(self.image_cola, self.rect_cola)
		#В случае сбора необходимого количества вкусняшки, выводит галочку
		if self.stats.score_pizza >= 100: 
			self.screen.blit(self.its_ok_pizza_image, self.rect_its_ok_pizza_image)
		if self.stats.score_cheetos >= 100:
			self.screen.blit(self.its_ok_cheetos_image, self.rect_its_ok_cheetos_image)
		if self.stats.score_cake>= 100:
			self.screen.blit(self.its_ok_cake_image, self.rect_its_ok_cake_image)
		if self.stats.score_cola >= 100:
			self.screen.blit(self.its_ok_cola_image, self.rect_its_ok_cola_image)
		#Выводит рекорд на экран
		self.screen.blit(self.image_record, self.record_rect)
