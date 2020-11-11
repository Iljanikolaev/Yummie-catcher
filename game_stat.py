
class GameStats():
	'''Отслеживание статистики для игры Yummie catcher'''
	def __init__(self, ai_settings, screen):
		'''Инициализирет статистику'''
		self.reset_stats()
		self.game_active = False
		#Рекорд не сбрасывется
		with open('record.txt') as rec:
			self.record = int(rec.read())
	def reset_stats(self):
		'''Сброс статистики'''
		self.score_pizza = 0
		self.score_cola = 0
		self.score_cheetos = 0
		self.score_cake = 0
