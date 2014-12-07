import tetris
import json
class FigureJ:

	cords = {
	'a':[1,5],
	'b':[2,5],
	'c':[3,5],
	'd':[3,4]
	}

	current_cords = {
	'a':[1,5],
	'b':[2,5],
	'c':[3,5],
	'd':[3,4]
	}

	new_cords = {
	'a':[1,5],
	'b':[2,5],
	'c':[3,5],
	'd':[3,4]
	}

	width_boundaries = [1,11]
	height_boundaries = [1,12]

	def calculate_new_cords(self,key):
		if key in [65,97]: #a
			open('errors','a').write('calculating new cords\n')			
			FigureJ.new_cords['a'] = [FigureJ.current_cords['a'][0]+1,FigureJ.current_cords['a'][1]-1]
			FigureJ.new_cords['b'] = [FigureJ.current_cords['b'][0]+1,FigureJ.current_cords['b'][1]-1]
			FigureJ.new_cords['c'] = [FigureJ.current_cords['c'][0]+1,FigureJ.current_cords['c'][1]-1]
			FigureJ.new_cords['d'] = [FigureJ.current_cords['d'][0]+1,FigureJ.current_cords['d'][1]-1]
		
		elif key in [68,100]: #d
			FigureJ.new_cords['a'] = [FigureJ.current_cords['a'][0]+1,FigureJ.current_cords['a'][1]+1]
			FigureJ.new_cords['b'] = [FigureJ.current_cords['b'][0]+1,FigureJ.current_cords['b'][1]+1]
			FigureJ.new_cords['c'] = [FigureJ.current_cords['c'][0]+1,FigureJ.current_cords['c'][1]+1]
			FigureJ.new_cords['d'] = [FigureJ.current_cords['d'][0]+1,FigureJ.current_cords['d'][1]+1]

		elif key in [119,87]: #w
			FigureJ.new_cords['a'] = [FigureJ.current_cords['a'][0]+1+1,FigureJ.current_cords['a'][1]-1]
			FigureJ.new_cords['b'] = [FigureJ.current_cords['b'][0]+1,FigureJ.current_cords['b'][1]]
			FigureJ.new_cords['c'] = [FigureJ.current_cords['c'][0]-1+1,FigureJ.current_cords['c'][1]+1]
			FigureJ.new_cords['d'] = [FigureJ.current_cords['d'][0]+1,FigureJ.current_cords['d'][1]+2]

		elif key in [83,115]:  #s
			pass

		elif key in [32]:
			FigureJ.new_cords['a'] = [FigureJ.current_cords['a'][0]+1,FigureJ.current_cords['a'][1]]
			FigureJ.new_cords['b'] = [FigureJ.current_cords['b'][0]+1,FigureJ.current_cords['b'][1]]
			FigureJ.new_cords['c'] = [FigureJ.current_cords['c'][0]+1,FigureJ.current_cords['c'][1]]
			FigureJ.new_cords['d'] = [FigureJ.current_cords['d'][0]+1,FigureJ.current_cords['d'][1]]

	def mark_cords_used(self):
		open('errors','a').write('marking used cords'+'\n')

		for key in FigureJ.new_cords:
			cord = FigureJ.new_cords[key]
			if cord not in tetris.USED_CORDS:
				tetris.USED_CORDS.append(cord)
		open('errors','a').write(json.dumps(tetris.USED_CORDS)+'\n')



	def check_new_cords(self):
		open('errors','a').write('checking new cords'+'\n')
		for key in FigureJ.new_cords:
			y, x = FigureJ.new_cords[key]
			if x in FigureJ.width_boundaries:
				open('errors','a').write('reached width boundary\n')
				FigureJ.new_cords = FigureJ.current_cords.copy()
				return None
			if y in FigureJ.height_boundaries:
				open('errors','a').write('reached height boundary\n')
				FigureJ.new_cords = FigureJ.current_cords.copy()
				return False

			if [y,x] in tetris.USED_CORDS:
				open('errors','a').write('reached used coordinates\n')
				FigureJ.new_cords = FigureJ.current_cords.copy()
				return False

		return True

	def check_termination(self):
		open('errors','a').write('checking termination\n')
		for key in FigureJ.new_cords:
			y,x = FigureJ.new_cords[key]
			if [y,x] in tetris.USED_CORDS:
				open('errors','a').write('reached termination point\n')
				FigureJ.new_cords = FigureJ.current_cords.copy()
				return True
		return False

	def draw(self, window):
		window.addch(FigureJ.cords['a'][0],FigureJ.cords['a'][1],'*')
		window.addch(FigureJ.cords['b'][0],FigureJ.cords['b'][1],'*')
		window.addch(FigureJ.cords['c'][0],FigureJ.cords['c'][1],'*')
		window.addch(FigureJ.cords['d'][0],FigureJ.cords['d'][1],'*')
		FigureJ.current_cords = FigureJ.cords.copy()
		FigureJ.new_cords = FigureJ.cords.copy()
		terminate = self.check_termination()
		return terminate
		
	
	def move(self, window, key):
		#first calculate new FigureJ.cords
		self.calculate_new_cords(key)
		open('errors','a').write('current cords'+'\n')
		open('errors','a').write(json.dumps(FigureJ.current_cords)+'\n')
		open('errors','a').write('new cords'+'\n')
		open('errors','a').write(json.dumps(FigureJ.new_cords)+'\n')
		status = self.check_new_cords()
		window.addch(FigureJ.current_cords['a'][0],FigureJ.current_cords['a'][1],' ')
		window.addch(FigureJ.current_cords['b'][0],FigureJ.current_cords['b'][1],' ')
		window.addch(FigureJ.current_cords['c'][0],FigureJ.current_cords['c'][1],' ')
		window.addch(FigureJ.current_cords['d'][0],FigureJ.current_cords['d'][1],' ')

		if status:
			open('errors','a').write('updating current cords'+'\n')
			FigureJ.current_cords = FigureJ.new_cords.copy()
			open('errors','a').write(json.dumps(FigureJ.current_cords)+'\n')
		if status == False:
			self.mark_cords_used()

		window.addch(FigureJ.new_cords['a'][0],FigureJ.new_cords['a'][1],'*')
		window.addch(FigureJ.new_cords['b'][0],FigureJ.new_cords['b'][1],'*')
		window.addch(FigureJ.new_cords['c'][0],FigureJ.new_cords['c'][1],'*')
		window.addch(FigureJ.new_cords['d'][0],FigureJ.new_cords['d'][1],'*')
		return status


		

