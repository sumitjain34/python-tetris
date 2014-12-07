import tetris
import json

class FigureS:

	cords = {
	'a':[1,6],
	'b':[2,6],
	'c':[2,5],
	'd':[3,5]
	}

	current_cords = {
	'a':[1,6],
	'b':[2,6],
	'c':[3,5],
	'd':[4,5]
	}

	new_cords = {
	'a':[1,6],
	'b':[2,6],
	'c':[3,5],
	'd':[4,5]
	}

	width_boundaries = [1,11]
	height_boundaries = [1,12]

	def calculate_new_cords(self,key):
		if key in [65,97]: #a
			open('errors','a').write('calculating new cords\n')			
			FigureS.new_cords['a'] = [FigureS.current_cords['a'][0]+1,FigureS.current_cords['a'][1]-1]
			FigureS.new_cords['b'] = [FigureS.current_cords['b'][0]+1,FigureS.current_cords['b'][1]-1]
			FigureS.new_cords['c'] = [FigureS.current_cords['c'][0]+1,FigureS.current_cords['c'][1]-1]
			FigureS.new_cords['d'] = [FigureS.current_cords['d'][0]+1,FigureS.current_cords['d'][1]-1]
		
		elif key in [68,100]: #d
			FigureS.new_cords['a'] = [FigureS.current_cords['a'][0]+1,FigureS.current_cords['a'][1]+1]
			FigureS.new_cords['b'] = [FigureS.current_cords['b'][0]+1,FigureS.current_cords['b'][1]+1]
			FigureS.new_cords['c'] = [FigureS.current_cords['c'][0]+1,FigureS.current_cords['c'][1]+1]
			FigureS.new_cords['d'] = [FigureS.current_cords['d'][0]+1,FigureS.current_cords['d'][1]+1]

		elif key in [119,87]: #w
			FigureS.new_cords['a'] = [FigureS.current_cords['a'][0]+1+1,FigureS.current_cords['a'][1]-1]
			FigureS.new_cords['b'] = [FigureS.current_cords['b'][0]+1,FigureS.current_cords['b'][1]]
			FigureS.new_cords['c'] = [FigureS.current_cords['c'][0]-1+1,FigureS.current_cords['c'][1]+1]
			FigureS.new_cords['d'] = [FigureS.current_cords['d'][0]+1,FigureS.current_cords['d'][1]+2]

		elif key in [83,115]:  #s
			pass

		elif key in [32]:
			FigureS.new_cords['a'] = [FigureS.current_cords['a'][0]+1,FigureS.current_cords['a'][1]]
			FigureS.new_cords['b'] = [FigureS.current_cords['b'][0]+1,FigureS.current_cords['b'][1]]
			FigureS.new_cords['c'] = [FigureS.current_cords['c'][0]+1,FigureS.current_cords['c'][1]]
			FigureS.new_cords['d'] = [FigureS.current_cords['d'][0]+1,FigureS.current_cords['d'][1]]
			
	def mark_cords_used(self):
		open('errors','a').write('marking used cords'+'\n')

		for key in FigureS.new_cords:
			cord = FigureS.new_cords[key]
			if cord not in tetris.USED_CORDS:
				tetris.USED_CORDS.append(cord)
		open('errors','a').write(json.dumps(tetris.USED_CORDS)+'\n')



	def check_new_cords(self):
		open('errors','a').write('checking new cords'+'\n')
		for key in FigureS.new_cords:
			y, x = FigureS.new_cords[key]
			if x in FigureS.width_boundaries:
				open('errors','a').write('reached boundary\n')
				FigureS.new_cords = FigureS.current_cords.copy()
				return None
			if y in FigureS.height_boundaries:
				open('errors','a').write('reached boundary\n')
				FigureS.new_cords = FigureS.current_cords.copy()
				return False

			if [y,x] in tetris.USED_CORDS:
				open('errors','a').write('reached boundary\n')
				FigureS.new_cords = FigureS.current_cords.copy()
				return False
		return True

	def check_termination(self):
		open('errors','a').write('checking termination\n')
		for key in FigureS.new_cords:
			y,x = FigureS.new_cords[key]
			if [y,x] in tetris.USED_CORDS:
				open('errors','a').write('reached termination point\n')
				FigureS.new_cords = FigureS.current_cords.copy()
				return True
		return False

	def draw(self,window,c=0):
		window.addch(FigureS.cords['a'][0],FigureS.cords['a'][1],'*')
		window.addch(FigureS.cords['b'][0],FigureS.cords['b'][1],'*')
		window.addch(FigureS.cords['c'][0],FigureS.cords['c'][1],'*')
		window.addch(FigureS.cords['d'][0],FigureS.cords['d'][1],'*')
		FigureS.current_cords = FigureS.cords.copy()
		FigureS.new_cords = FigureS.cords.copy()
		terminate = self.check_termination()
		return terminate

	def move(self, window, key):
		#first calculate new FigureS.cords
		self.calculate_new_cords(key)
		open('errors','a').write('current cords'+'\n')
		open('errors','a').write(json.dumps(FigureS.current_cords)+'\n')
		open('errors','a').write('new cords'+'\n')
		open('errors','a').write(json.dumps(FigureS.new_cords)+'\n')
		status = self.check_new_cords()
		window.addch(FigureS.current_cords['a'][0],FigureS.current_cords['a'][1],' ')
		window.addch(FigureS.current_cords['b'][0],FigureS.current_cords['b'][1],' ')
		window.addch(FigureS.current_cords['c'][0],FigureS.current_cords['c'][1],' ')
		window.addch(FigureS.current_cords['d'][0],FigureS.current_cords['d'][1],' ')

		if status:
			open('errors','a').write('updating current cords'+'\n')
			FigureS.current_cords = FigureS.new_cords.copy()
			open('errors','a').write(json.dumps(FigureS.current_cords)+'\n')
		if status == False:
			self.mark_cords_used()

		window.addch(FigureS.new_cords['a'][0],FigureS.new_cords['a'][1],'*')
		window.addch(FigureS.new_cords['b'][0],FigureS.new_cords['b'][1],'*')
		window.addch(FigureS.new_cords['c'][0],FigureS.new_cords['c'][1],'*')
		window.addch(FigureS.new_cords['d'][0],FigureS.new_cords['d'][1],'*')
		return status
