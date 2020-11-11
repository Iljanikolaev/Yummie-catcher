import sys
import pygame
from timer import Timer
from yummie import Yummie


def check_events(ai_settings, screen, hero, yummie_gr, stats, sb, timer, play_button):
	"""Обрабатывает нажатия клавиш и события мыши."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, hero)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, hero)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings, screen, hero, yummie_gr, stats, sb, timer, play_button, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, hero, yummie_gr, stats, sb, timer, play_button, mouse_x, mouse_y):
	"""Обрабатывает нажатие мышью на кнопку 'Play'."""
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		#Курсор мыши скрывется
		pygame.mouse.set_visible(False)
		#Сброс игровой статистики
		stats.reset_stats()
		stats.game_active = True
		#Сброс изображений счетов
		sb.prep_score_pizza()
		sb.prep_score_cheetos()
		sb.prep_score_cake()
		sb.prep_score_cola()
		sb.prep_record()
		#Очистка списка вкусняшек
		yummie_gr.empty()
		#Запуск секундомера
		timer.start_time()
		#Создание новых вкусняшек
		create_yummie(ai_settings, screen, hero, yummie_gr)


def check_keydown_events(event, hero):
	"""Реагирует на нажатие клавиш."""
	if event.key == pygame.K_RIGHT:
		hero.moving_right = True
	elif event.key == pygame.K_LEFT:
		hero.moving_left = True
	elif event.key == pygame.K_q:
		sys.exit()
	#Смена игрока
	elif event.key == pygame.K_1:
		hero.image_l = pygame.image.load('images/1.png').convert_alpha()
		hero.image_r = pygame.transform.flip(hero.image_l, True, False)
		hero.image = hero.image_l
	elif event.key == pygame.K_2:
		hero.image_r = pygame.image.load('images/2.png').convert_alpha()
		hero.image_l = pygame.transform.flip(hero.image_r, True, False)
		hero.image = hero.image_l


def check_keyup_events(event, hero):
	"""Реагираует на отпускание клавиш."""
	if event.key == pygame.K_RIGHT:
		hero.moving_right = False
	elif event.key == pygame.K_LEFT:
		hero.moving_left = False


def update_screen(ai_settings, screen, hero, yummie_gr, stats, sb, timer, play_button):
	"""Обновляет изображения на экране и отображает новый экран"""
	#При каждом проходе цикла перерисовывается экран
	screen.blit(ai_settings.bg, ai_settings.bg_rect)
	#Если игра активна, вывод секундомера, счета, героя, вкусняшек на экран
	if stats.game_active:
		timer.show_time()
		hero.blitme()
		yummie_gr.draw(screen)
		sb.show_score()
	#Если игра не активна, вывод на экран кнопки Play
	if not stats.game_active:
		play_button.draw_button()
	#Отображение послежнего отрисовнного экрана
	pygame.display.flip()

def create_yummie(ai_settings, screen, hero, yummie_gr):
	'''Создает вкуснятину'''
	for i in range(5):
		new_yummie = Yummie(ai_settings, screen, hero)
		yummie_gr.add(new_yummie)
def update_yummie(ai_settings, screen, yummie_gr, hero, stats, sb, timer, play_button):
	'''Проверяет коллизии вкуснятины с игроком, проверяет не достигла вкусняха края экрана,
	    , если условия выполнены удаляет и создает новые вкусняхи, после обновляет позиции вкуснях'''
	yummie_gr.update()
	for i in collision_hero_yummie(hero, yummie_gr, stats, sb):
		new_yummie = Yummie(ai_settings, screen, hero)
		yummie_gr.add(new_yummie)
	for yum in yummie_gr.copy():
		if yum.y >= ai_settings.screen_height:
			yummie_gr.remove(yum)
			new_yummie = Yummie(ai_settings, screen, hero)
			yummie_gr.add(new_yummie)
	game_over(stats, timer, play_button)


def collision_hero_yummie(hero, yummie_gr, stats, sb):
	'''Подсчитывает количество пойманных вкусняшек разного вида'''
	hits = pygame.sprite.spritecollide(hero, yummie_gr, True)
	for food in hits:
		if food.obj == 0:
			stats.score_pizza += 1
			sb.prep_score_pizza()
		if food.obj == 1:
			stats.score_cheetos += 1
			sb.prep_score_cheetos()
		if food.obj == 2:
			stats.score_cake += 1
			sb.prep_score_cake()
		if food.obj == 3:
			stats.score_cola += 1
			sb.prep_score_cola()
	return hits


def game_over(stats, timer, play_button):
	'''Игра заканчивается, как только игрок поймал 100 вкуснях каждого вида, предлагает сыграть ещё'''
	if (stats.score_pizza >= 100) and (stats.score_cheetos >= 100) and (stats.score_cake >= 100) and (stats.score_cola >= 100):
		stats.game_active = False
		pygame.mouse.set_visible(True)
		time_game_over = timer.game_over_time()
		if stats.record > int(time_game_over):
			stats.record = time_game_over
			with open('record.txt', 'w') as rec:
				rec.write(str(time_game_over))
		play_button.prep_msg('Вам удалось собрать все вкусняшки за ' + time_game_over + ' c.  Играть ещё?')
