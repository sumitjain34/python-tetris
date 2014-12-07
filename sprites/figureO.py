import tetris
import json

class FigureO:

	cords = {
	'a':[1,5],
	'b':[1,6],
	'c':[2,5],
	'd':[2,6]
	}

	current_cords = {
	'a':[1,5],
	'b':[1,6],
	'c':[2,5],
	'd':[2,6]
	}

	new_cords = {
	'a':[1,5],
	'b':[1,6],
	'c':[2,5],
	'd':[2,6]
	}

	width_boundaries = [1,11]
	height_boundaries = [1,12]

	def calculate_new_cords(self,key):
		if key in [65,97]: #a
			open('errors','a').write('calculating new cords\n')			
			FigureO.new_cords['a'] = [FigureO.current_cords['a'][0]+1,FigureO.current_cords['a'][1]-1]
			FigureO.new_cords['b'] = [FigureO.current_cords['b'][0]+1,FigureO.current_cords['b'][1]-1]
			FigureO.new_cords['c'] = [FigureO.current_cords['c'][0]+1,FigureO.current_cords['c'][1]-1]
			FigureO.new_cords['d'] = [FigureO.current_cords['d'][0]+1,FigureO.current_cords['d'][1]-1]
		
		elif key in [68,100]: #d
			FigureO.new_cords['a'] = [FigureO.current_cords['a'][0]+1,FigureO.current_cords['a'][1]+1]
			FigureO.new_cords['b'] = [FigureO.current_cords['b'][0]+1,FigureO.current_cords['b'][1]+1]
			FigureO.new_cords['c'] = [FigureO.current_cords['c'][0]+1,FigureO.current_cords['c'][1]+1]
			FigureO.new_cords['d'] = [FigureO.current_cords['d'][0]+1,FigureO.current_cords['d'][1]+1]

		elif key in [119,87,115,83]: #w and s
			FigureO.new_cords['a'] = [FigureO.current_cords['a'][0]+1,FigureO.current_cords['a'][1]]
			FigureO.new_cords['b'] = [FigureO.current_cords['b'][0]+1,FigureO.current_cords['b'][1]]
			FigureO.new_cords['c'] = [FigureO.current_cords['c'][0]+1,FigureO.current_cords['c'][1]]
			FigureO.new_cords['d'] = [FigureO.current_cords['d'][0]+1,FigureO.current_cords['d'][1]]

		elif key in [32]:
			FigureO.new_cords['a'] = [FigureO.current_cords['a'][0]+1,FigureO.current_cords['a'][1]]
			FigureO.new_cords['b'] = [FigureO.current_cords['b'][0]+1,FigureO.current_cords['b'][1]]
			FigureO.new_cords['c'] = [FigureO.current_cords['c'][0]+1,FigureO.current_cords['c'][1]]
			FigureO.new_cords['d'] = [FigureO.current_cords['d'][0]+1,FigureO.current_cords['d'][1]]
			
	def mark_cords_used(self):
		open('errors','a').write('marking used cords'+'\n')

		for key in FigureO.new_cords:
			cord = FigureO.new_cords[key]
			if cord not in tetris.USED_CORDS:
				tetris.USED_CORDS.append(cord)
		open('errors','a').write(json.dumps(tetris.USED_CORDS)+'\n')



	def check_new_cords(self):
		open('errors','a').write('checking new cords'+'\n')
		for key in FigureO.new_cords:
			y, x = FigureO.new_cords[key]
			if x in FigureO.width_boundaries:
				open('errors','a').write('reached boundary\n')
				FigureO.new_cords = FigureO.current_cords.copy()
				return None
			if y in FigureO.height_boundaries:
				open('errors','a').write('reached boundary\n')
				FigureO.new_cords = FigureO.current_cords.copy()
				return False

			if [y,x] in tetris.USED_CORDS:
				open('errors','a').write('reached boundary\n')
				FigureO.new_cords = FigureO.current_cords.copy()
				return False

		return True

	def check_termination(self):
		open('errors','a').write('checking termination\n')
		for key in FigureO.new_cords:
			y,x = FigureO.new_cords[key]
			if [y,x] in tetris.USED_CORDS:
				open('errors','a').write('reached termination point\n')
				FigureO.new_cords = FigureO.current_cords.copy()
				return True
		return False

	def draw(self,window,c=0):
		window.addch(FigureO.cords['a'][0],FigureO.cords['a'][1],'*')
		window.addch(FigureO.cords['b'][0],FigureO.cords['b'][1],'*')
		window.addch(FigureO.cords['c'][0],FigureO.cords['c'][1],'*')
		window.addch(FigureO.cords['d'][0],FigureO.cords['d'][1],'*')
		FigureO.current_cords = FigureO.cords.copy()
		FigureO.new_cords = FigureO.cords.copy()
		terminate = self.check_termination()
		return terminate

	def move(self, window, key):
		#first calculate new FigureO.cords
		self.calculate_new_cords(key)
		open('errors','a').write('current cords'+'\n')
		open('errors','a').write(json.dumps(FigureO.current_cords)+'\n')
		open('errors','a').write('new cords'+'\n')
		open('errors','a').write(json.dumps(FigureO.new_cords)+'\n')
		status = self.check_new_cords()
		window.addch(FigureO.current_cords['a'][0],FigureO.current_cords['a'][1],' ')
		window.addch(FigureO.current_cords['b'][0],FigureO.current_cords['b'][1],' ')
		window.addch(FigureO.current_cords['c'][0],FigureO.current_cords['c'][1],' ')
		window.addch(FigureO.current_cords['d'][0],FigureO.current_cords['d'][1],' ')

		if status:
			open('errors','a').write('updating current cords'+'\n')
			FigureO.current_cords = FigureO.new_cords.copy()
			open('errors','a').write(json.dumps(FigureO.current_cords)+'\n')
		if status == False:
			self.mark_cords_used()

		window.addch(FigureO.new_cords['a'][0],FigureO.new_cords['a'][1],'*')
		window.addch(FigureO.new_cords['b'][0],FigureO.new_cords['b'][1],'*')
		window.addch(FigureO.new_cords['c'][0],FigureO.new_cords['c'][1],'*')
		window.addch(FigureO.new_cords['d'][0],FigureO.new_cords['d'][1],'*')
		return status