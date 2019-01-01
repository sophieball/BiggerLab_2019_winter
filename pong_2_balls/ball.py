import pygame

class Ball:
	def __init__(self, c, r, d_x, d_y, i_p):
		self.color = c
		self.radius = r
		self.delta_x = d_x
		self.delta_y = d_y
		self.spot = i_p
		self.lose = False
		self.point = 0

	def draw_ball(self, screen):
		pygame.draw.circle(screen, self.color, self.spot, self.radius)

	def move_ball(self, width, height, board_x, board_width, board_height):
		# if lost, no need to move
		if self.lose:
			return self.lose

		collide = False

		# automatically moves the circle
		x = self.spot[0]
		y = self.spot[1]

		x = x + self.delta_x
		# within board range
		if (x < self.radius) or (x > width - self.radius):
			self.delta_x = -1 * self.delta_x

		y = y + self.delta_y
		# check collision
		if board_x <= x and x <= board_x + board_width and \
			y >= height - board_height - self.radius:
			collide = True
			self.point += 1
		
		# bounce if hits board
		if (y < self.radius) or collide:
			self.delta_y = -1 * self.delta_y
			collide = False
		# game over if not hits board
		elif y > height + self.radius:
			self.lose = True

		self.spot = (x, y)

		return self.lose

	def print_points(self):
		return self.point



class Dog:
	def __init__(self, n, h, w):
		self.name = n
		self.height = h
		self.weight = w
		print self.name, self.height

	def call(self):
		print self.name

qiuqiu = Dog("qiuqiu", 0.5, 30)
qiuqiu.call()

yongshi = Dog("yongshi", 0.8, 10)
yongshi.call()

xiquan = Dog("xiquan", 0.2, 30)