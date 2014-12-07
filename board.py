import curses
from random import randrange
import time
import os
from sprites.figureLine import FigureLine
from sprites.figureL import FigureL
from sprites.figureO import FigureO
from sprites.figureS import FigureS
from sprites.figureJ import FigureJ

class Board:

	def __init__(self):
		self.height = 13
		self.width = 13
		self.begin_y = 1
		self.begin_x = 1
		self.window = curses.newwin(self.height,self.width,self.begin_y,self.begin_x)
		# self.prompt_window = curses.newwin(5,10,20,2)
		self.window.keypad(1)
		self.window.nodelay(1)
		self.window.timeout(600)
		
		# self.prompt_window.keypad(1)
		# self.prompt_window.nodelay(1)
		# self.prompt_window.timeout(100)

		self.figures={
						'line' : FigureLine,
						'l' : FigureL,
						'o' : FigureO,
						's' : FigureS,
						'j' : FigureJ
		}

		self.active_figure = None

	def draw(self):
		self.window.border('*','*',' ','*',' ',' ','*','*')
		return self.window

	def draw_figure(self,fig=None,c=0):
		Figure = self.figures[fig]
		figure = Figure()
		terminate = figure.draw(self.window)
		return terminate

	def move_figure(self,active_figure=None,key=None):
		if active_figure:
			Figure = self.figures[active_figure]
			figure = Figure()
			status = figure.move(self.window,key)
		return status

	def check_figure(self,figure=None):
		pass

	def check_board(self):
		pass
		