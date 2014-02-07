import pygame
import sys
from pygame.locals import *
from random import choice

class Game:

	def __init__(self):
		pygame.init()
		# COLORS
		self.wow = (200, 180, 250)
		self.black = (	0, 	 0,	  0)
		self.blue =  (	0,	 0,	255)
		self.green = (	0, 255,   0)
		self.red =   (255,   0,   0)
		# BOARD
		self.xb = 600 # board height 
		self.yb = 480 # board width
		self.BOARD = pygame.display.set_mode((self.xb,self.yb))
		self.d = ""

		# PLAYER/ GAME
		self.level = 1
		self.image = self.d+"lemon.png"
		self.score = 0 #points for food
		self.x = 45#360 # x position
		self.y = 5#50 # y position
		self.w = 12# width
		self.h = 12 # height

		self.head = 0 #syntactic sugar

		self.FPS = 12
		self.coords =  [{'x':self.x, "y":self.y},
		{'x':self.x+1, "y":self.y},
		{'x':self.x+2, "y":self.y},
		{'x':self.x+3, "y":self.y},
		{'x':self.x+4, "y":self.y},
		{'x':self.x+5, "y":self.y}]
		#GAME
		self.musicImg = pygame.image.load(self.d+'music.png')
		self.clock = pygame.time.Clock() #test
		self.snake = pygame.Surface((self.w,self.h))


		assert self.xb % self.w == 0 and self.yb % self.h == 0

		# FOOD
		self.xf = 12 # food height
		self.yf = 12 # food width
		self.random = choice(self.makecoords())
		self.makefood = pygame.Surface((self.xf,self.yf))

		assert self.xf == self.w and self.yf == self.h

	def intro(self):
		BOARD = pygame.display.set_mode((self.xb,self.yb))
		WHITE = (255, 255, 255)
		BOARD.fill(WHITE)
		font = pygame.font.SysFont('Comic Sans MS',40)
		text = font.render('Press Key to start', True, self.black, WHITE)
		textrect = text.get_rect()
		textrect.topleft = (200,200)
		self.BOARD.blit(text,textrect)


		while True:	
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				if event.type == KEYDOWN:
					return	
			pygame.display.update()			
			
		
	def startgame(self):
		self.intro()
		self.run()	


	def run(self):
		pygame.init()
		font = pygame.font.SysFont('Comic Sans MS',40)
		fontm = pygame.font.SysFont('Comic Sans MS',20)
		fonta = pygame.font.SysFont('Comic Sans MS',15)
		
		FPS = self.FPS
		
		SNAKE = self.coords
		HEAD = self.head
		
		catx = 180
		caty = 80
		next = None
		pygame.display.set_caption('SnakeGame')
		movement = 'left'
		sudo = True
		pygame.mixer.music.load(self.d+'batard.mp3')
		pygame.mixer.music.play(-1,12)
		while True:
			lemonImg = pygame.image.load(self.image)
			text = font.render('Level: '+ str(self.level), True, self.black, self.wow)
			textm = fontm.render('Stromae: Batard', True, self.black, self.wow)
			texta = fonta.render('Created by Peter Parada', True, self.black, self.wow)
			textarect =texta.get_rect()
			textarect.center = (530,470)
			textmrect = textm.get_rect()
			textmrect.center = (540,48)
			textrect = text.get_rect()
			textrect.topleft = (5,0)
			self.BOARD.fill(self.wow)
			self.BOARD.blit(text,textrect)
			self.BOARD.blit(textm,textmrect)
			self.BOARD.blit(texta,textarect)
			self.BOARD.blit(lemonImg,(catx,caty+0))
			self.BOARD.blit(self.musicImg,(textarect.center[0],10))
			if {"x":self.random[0],"y":self.random[1]} not in SNAKE:
				pygame.draw.rect(self.BOARD, self.blue, (self.random[0],self.random[1],self.w,self.w))
				food = pygame.draw.ellipse(self.BOARD, self.red, (self.random[0],self.random[1],self.w,self.w))

			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()	

				if event.type == KEYDOWN:
					if event.key == K_RIGHT and movement != "left":
						movement = 'right'
					elif event.key == K_LEFT and movement != "right":
						movement = 'left'
					elif event.key == K_DOWN and movement != "up":
						movement = 'down'
					elif event.key == K_UP and movement != "down":
						movement = 'up'
			if SNAKE[HEAD]['x'] == -1 or SNAKE[HEAD]['x'] == 50 or SNAKE[HEAD]['y'] == -1 or SNAKE[HEAD]['y'] == 40:
				return
				 
			if SNAKE[HEAD] in SNAKE[1:]:
				return
				

			if SNAKE[HEAD]['x']*self.w == self.random[0] and SNAKE[HEAD]['y']*self.w == self.random[1]:
				self.eatfoodreset()	
				if self.score == self.level +2:
					self.level += 1
					self.score = 0
				if self.level == 1:
					self.image = self.d+"lemon.png"
					self.wow = (200, 180, 250)
					self.FPS  += 2	
				if self.level == 2:
					self.image = self.d+"cake.png"
					self.wow = (255, 180, 240)
					self.FPS  += 2	
				
				if self.level == 5:
					self.image = self.d+"cheese.png"
					self.wow = (160, 220, 100)
					self.FPS  += 2	
				if self.level == 3:
					self.image = self.d+"coffee.png"
					self.wow = (200, 130, 80)
					self.FPS  += 2		
				if self.level == 4:
					self.image = self.d+"orange.png"
					self.wow = (250, 180, 200)
					self.FPS  += 2
				elif self.level == 6:
					self.image = self.d+"citrus.png"
					self.wow = (200, 180, 250)
					self.FPS  += 2
					
				elif self.level == 7:
					self.image = self.d+"cherry.png"
					self.wow = (240, 110, 180)
					self.FPS  += 2
				elif self.level == 8:
					self.image = self.d+"banana.png"
					self.wow = (240, 240, 150)
					self.FPS  += 2

				elif self.level ==9:
					self.image = self.d+"leaf.png"
					self.wow = (210, 255, 150)
					self.FPS  += 2		
				elif self.level == 10:
					self.image = self.d+"melon.png"
					self.wow = (210, 255, 255)
					self.FPS  += 2
				elif self.level == 11:
					self.image = self.d+"choco.png"
					self.wow = (170, 130, 80)
					self.FPS  += 2										
								

			else:
				del SNAKE[-1]	
			if movement == 'right':		
				newHead = {'x': SNAKE[HEAD]['x'] + 1, 'y':SNAKE[HEAD]['y']}

			if movement == 'left':
				newHead = {'x': SNAKE[HEAD]['x'] - 1, 'y':SNAKE[HEAD]['y']}

			if movement == 'down':
				newHead = {'x': SNAKE[HEAD]['x'], 'y':SNAKE[HEAD]['y'] + 1}

			if movement == 'up':
				newHead = {'x': SNAKE[HEAD]['x'], 'y':SNAKE[HEAD]['y'] - 1}
				
			
			SNAKE.insert(0, newHead)
			for coord in SNAKE:
				x = coord['x'] * self.w
				y = coord['y'] * self.w
				wormSegmentRect = pygame.Rect(x, y, self.w, self.h)
				if SNAKE.index(coord) == 0:
					pygame.draw.rect(self.BOARD, self.black, wormSegmentRect)
					pygame.draw.rect(self.BOARD, self.blue, (wormSegmentRect[0]-0.5,wormSegmentRect[1],wormSegmentRect[2]-0.5,wormSegmentRect[3]-0.5))
				else:
					pygame.draw.rect(self.BOARD, self.black, wormSegmentRect)
					pygame.draw.rect(self.BOARD, self.green, (wormSegmentRect[0],wormSegmentRect[1],wormSegmentRect[2]-0.5,wormSegmentRect[3]-0.5))
			pygame.display.update()
			pygame.time.Clock().tick(self.FPS)
	def makecoords(self):
		#all possible x,y coords.
		coords = []
		for x in range(0,self.xb,self.w):
			for y in range(0,self.yb,self.h):
				coords.append((x,y))	
		return coords
	
	def eatfoodreset(self):
		self.random = choice(self.makecoords())
		pygame.draw.rect(self.BOARD, self.red, (self.random[0],self.random[1],self.w,self.w))
		pygame.draw.ellipse(self.BOARD, self.red, (self.random[0],self.random[1],self.w,self.w))
		self.score += 1
		

Game().startgame()
