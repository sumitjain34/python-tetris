import tetris
import json

class FigureL:

	cords = {
	'a':[1,5],
	'b':[2,5],
	'c':[3,5],
	'd':[3,6]
	}

	current_cords = {
	'a':[1,5],
	'b':[2,5],
	'c':[3,5],
	'd':[3,6]
	}

	new_cords = {
	'a':[1,5],
	'b':[2,5],
	'c':[3,5],
	'd':[3,6]
	}

	width_boundaries = [1,11]
	height_boundaries = [1,12]

	def calculate_new_cords(self,key):
		if key in [65,97]: #a
			open('errors','a').write('calculating new cords\n')			
			FigureL.new_cords['a'] = [FigureL.current_cords['a'][0]+1,FigureL.current_cords['a'][1]-1]
			FigureL.new_cords['b'] = [FigureL.current_cords['b'][0]+1,FigureL.current_cords['b'][1]-1]
			FigureL.new_cords['c'] = [FigureL.current_cords['c'][0]+1,FigureL.current_cords['c'][1]-1]
			FigureL.new_cords['d'] = [FigureL.current_cords['d'][0]+1,FigureL.current_cords['d'][1]-1]
		
		elif key in [68,100]: #d
			FigureL.new_cords['a'] = [FigureL.current_cords['a'][0]+1,FigureL.current_cords['a'][1]+1]
			FigureL.new_cords['b'] = [FigureL.current_cords['b'][0]+1,FigureL.current_cords['b'][1]+1]
			FigureL.new_cords['c'] = [FigureL.current_cords['c'][0]+1,FigureL.current_cords['c'][1]+1]
			FigureL.new_cords['d'] = [FigureL.current_cords['d'][0]+1,FigureL.current_cords['d'][1]+1]

		elif key in [119,87]: #w
			FigureL.new_cords['a'] = [FigureL.current_cords['a'][0]+1+1,FigureL.current_cords['a'][1]-1]
			FigureL.new_cords['b'] = [FigureL.current_cords['b'][0]+1,FigureL.current_cords['b'][1]]
			FigureL.new_cords['c'] = [FigureL.current_cords['c'][0]-1+1,FigureL.current_cords['c'][1]+1]
			FigureL.new_cords['d'] = [FigureL.current_cords['d'][0]+1,FigureL.current_cords['d'][1]+2]

		elif key in [83,115]:  #s
			pass

		elif key in [32]:
			FigureL.new_cords['a'] = [FigureL.current_cords['a'][0]+1,FigureL.current_cords['a'][1]]
			FigureL.new_cords['b'] = [FigureL.current_cords['b'][0]+1,FigureL.current_cords['b'][1]]
			FigureL.new_cords['c'] = [FigureL.current_cords['c'][0]+1,FigureL.current_cords['c'][1]]
			FigureL.new_cords['d'] = [FigureL.current_cords['d'][0]+1,FigureL.current_cords['d'][1]]

	def mark_cords_used(self):
		open('errors','a').write('marking used cords'+'\n')

		for key in FigureL.new_cords:
			cord = FigureL.new_cords[key]
			if cord not in tetris.USED_CORDS:
				tetris.USED_CORDS.append(cord)
		open('errors','a').write(json.dumps(tetris.USED_CORDS)+'\n')



	def check_new_cords(self):
		open('errors','a').write('checking new cords'+'\n')
		for key in FigureL.new_cords:
			y, x = FigureL.new_cords[key]
			if x in FigureL.width_boundaries:
				open('errors','a').write('reached boundary\n')
				FigureL.new_cords = FigureL.current_cords.copy()
				return None
			if y in FigureL.height_boundaries:
				open('errors','a').write('reached boundary\n')
				FigureL.new_cords = FigureL.current_cords.copy()
				return False

			if [y,x] in tetris.USED_CORDS:
				open('errors','a').write('reached boundary\n')
				FigureL.new_cords = FigureL.current_cords.copy()
				return False
		return True

	def check_termination(self):
		open('errors','a').write('checking termination\n')
		for key in FigureL.new_cords:
			y,x = FigureL.new_cords[key]
			if [y,x] in tetris.USED_CORDS:
				open('errors','a').write('reached termination point\n')
				FigureL.new_cords = FigureL.current_cords.copy()
				return True
		return False

	def draw(self, window):
		window.addch(FigureL.cords['a'][0],FigureL.cords['a'][1],'*')
		window.addch(FigureL.cords['b'][0],FigureL.cords['b'][1],'*')
		window.addch(FigureL.cords['c'][0],FigureL.cords['c'][1],'*')
		window.addch(FigureL.cords['d'][0],FigureL.cords['d'][1],'*')
		FigureL.current_cords = FigureL.cords.copy()
		FigureL.new_cords = FigureL.cords.copy()
		terminate = self.check_termination()
		return terminate
		
	
	def move(self, window, key):
		#first calculate new FigureL.cords
		self.calculate_new_cords(key)
		open('errors','a').write('current cords'+'\n')
		open('errors','a').write(json.dumps(FigureL.current_cords)+'\n')
		open('errors','a').write('new cords'+'\n')
		open('errors','a').write(json.dumps(FigureL.new_cords)+'\n')
		status = self.check_new_cords()
		window.addch(FigureL.current_cords['a'][0],FigureL.current_cords['a'][1],' ')
		window.addch(FigureL.current_cords['b'][0],FigureL.current_cords['b'][1],' ')
		window.addch(FigureL.current_cords['c'][0],FigureL.current_cords['c'][1],' ')
		window.addch(FigureL.current_cords['d'][0],FigureL.current_cords['d'][1],' ')

		if status:
			open('errors','a').write('updating current cords'+'\n')
			FigureL.current_cords = FigureL.new_cords.copy()
			open('errors','a').write(json.dumps(FigureL.current_cords)+'\n')
		if status == False:
			self.mark_cords_used()

		window.addch(FigureL.new_cords['a'][0],FigureL.new_cords['a'][1],'*')
		window.addch(FigureL.new_cords['b'][0],FigureL.new_cords['b'][1],'*')
		window.addch(FigureL.new_cords['c'][0],FigureL.new_cords['c'][1],'*')
		window.addch(FigureL.new_cords['d'][0],FigureL.new_cords['d'][1],'*')
		return status


		



