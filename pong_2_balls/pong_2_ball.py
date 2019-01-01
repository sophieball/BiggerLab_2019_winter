import pygame
from util import *
import time
from ball import *

pygame.init()

# your game
width = 500
height = 500
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Pong 2")

# variable
keep_going = True
lose = False
close = False

text_pos = (width / 2, height / 2)
text_size = 100

# circle
radius = 10
spot = (width / 2, 450)
delta_x = 1
delta_y = 2

# board
board_width = 60
board_height = 10
board_x = width / 2 - board_width / 2
board_y = height - board_height
board_dis = 15

collide = False

# constants
RED = (255, 0, 0) # tuple
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# produce 2 balls
ball1 = Ball(RED, 10, -2, -3, (width / 2, height / 2))
ball2 = Ball(WHITE, 5, -1, -2, (width / 2, height - 5 - board_height))

while not lose:
	screen.fill(BLACK)

	for event in pygame.event.get(): # [CLICK, CLICK, QUIT]
		# if click quit:
		if event.type == pygame.QUIT: 
			# 	quit()
			close = True
		if event.type == pygame.KEYDOWN:
			# if left key
			if event.key == pygame.K_LEFT:
				board_x = max(0, board_x - board_dis)
			elif event.key == pygame.K_RIGHT:
				board_x = min(width - board_width, board_x + board_dis)
	
	# automatically moves 2 balls
	lose1 = ball1.move_ball(width, height, board_x, board_width, board_height)
	lose2 = ball2.move_ball(width, height, board_x, board_width, board_height)
	lose = close or (lose1 and lose2)

	#spot = auto_move(spot, width, height, radius, delta_x, delta_y)
	#pygame.draw.circle(screen, RED, spot, radius) # spot = (x, y)
	ball1.draw_ball(screen)
	ball2.draw_ball(screen)

	# display points
	points = ball1.print_points() + ball2.print_points()
	myfont = pygame.font.SysFont("times", 20)
	label = myfont.render("points: " + str(points), 1, YELLOW)
	screen.blit(label, (1, 2))

	# draw board
	pygame.draw.rect(screen, WHITE, [board_x, board_y, board_width, board_height])

	pygame.display.update() # refresh screen
	#time.sleep(0.5)

while keep_going and not close:
	# display win or lose image
	for event in pygame.event.get(): # [CLICK, CLICK, QUIT]
		# if click quit:
		if event.type == pygame.QUIT: 
			# 	quit()
			keep_going = False

	screen.fill(BLACK)

	# render text
	myfont = pygame.font.SysFont("times", text_size)
	label = myfont.render("You lose!", 1, YELLOW)
	screen.blit(label, text_pos)
	pygame.display.update()

pygame.quit()