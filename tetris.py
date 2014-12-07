from board import Board
import curses
import random

USED_CORDS = []

class Tetris:

	def __init__(self):
		self.figures = ['line','l','j','s','o']
		self.active_figure = None
		self.draw_new_figure = True


	def initialize_game(self):
		curses.initscr()
		curses.curs_set(0)
		curses.cbreak()
		self.board = Board()

	def main(self,stdscr):
		# c = 0
		# board_steps = 0
		# total_steps = 11
		# pad = curses.newpad(100, 100)
		# #  These loops fill the pad with letters; this is
		# # explained in the next section
		# try:
		# 	pad.addstr(2,10,'Enter Input')
		# except curses.error:
		# 	pass
		# #  Displays a section of the pad in the middle of the screen
		# pad.refresh(0,0, 20,5, 40,75)

		while 1:
			self.window= self.board.draw()
			key = self.window.getch()

			if key == -1:
				status = None
				pass
			if key == 27:
				status = None
				break
			elif key in [65,97,68,100,32]:
				status = self.board.move_figure(self.active_figure,key)
			if status == False:
				self.draw_new_figure = True
			figure = random.choice(self.figures)
			if self.draw_new_figure:
				terminate = self.board.draw_figure(figure)
				open('errors','a').write('terminating'+str(terminate)+'\n')
				self.draw_new_figure = False
				self.active_figure = figure
				if terminate:
					open('errors','a').write('terminating\n')
					break
		curses.endwin()

	def start(self):
		curses.wrapper(self.main)

if __name__ == '__main__':
	game = Tetris()
	game.initialize_game()
	game.start()
	
