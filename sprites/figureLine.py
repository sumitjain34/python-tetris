import tetris
import json

class FigureLine:
	cords = {
	'a':[1,4],
	'b':[1,5],
	'c':[1,6],
	'd':[1,7]
	}

	current_cords = {
	'a':[1,4],
	'b':[1,5],
	'c':[1,6],
	'd':[1,7]
	}

	new_cords = {
	'a':[1,4],
	'b':[1,5],
	'c':[1,6],
	'd':[1,7]
	}

	width_boundaries = [1,11]
	height_boundaries = [1,12]

	def calculate_new_cords(self,key):
		if key in [65,97]: #a
			open('errors','a').write('calculating new cords\n')			
			FigureLine.new_cords['a'] = [FigureLine.current_cords['a'][0]+1,FigureLine.current_cords['a'][1]-1]
			FigureLine.new_cords['b'] = [FigureLine.current_cords['b'][0]+1,FigureLine.current_cords['b'][1]-1]
			FigureLine.new_cords['c'] = [FigureLine.current_cords['c'][0]+1,FigureLine.current_cords['c'][1]-1]
			FigureLine.new_cords['d'] = [FigureLine.current_cords['d'][0]+1,FigureLine.current_cords['d'][1]-1]
		
		elif key in [68,100]: #d
			FigureLine.new_cords['a'] = [FigureLine.current_cords['a'][0]+1,FigureLine.current_cords['a'][1]+1]
			FigureLine.new_cords['b'] = [FigureLine.current_cords['b'][0]+1,FigureLine.current_cords['b'][1]+1]
			FigureLine.new_cords['c'] = [FigureLine.current_cords['c'][0]+1,FigureLine.current_cords['c'][1]+1]
			FigureLine.new_cords['d'] = [FigureLine.current_cords['d'][0]+1,FigureLine.current_cords['d'][1]+1]

		elif key in [119,87]: #w
			FigureLine.new_cords['a'] = [FigureLine.current_cords['a'][0]-1+1,FigureLine.current_cords['a'][1]+1]
			FigureLine.new_cords['b'] = [FigureLine.current_cords['b'][0]+1,FigureLine.current_cords['b'][1]]
			FigureLine.new_cords['c'] = [FigureLine.current_cords['c'][0]+1+1,FigureLine.current_cords['c'][1]-1]
			FigureLine.new_cords['d'] = [FigureLine.current_cords['d'][0]+1+2,FigureLine.current_cords['d'][1]-2]

		elif key in [83,115]:  #s
			pass

		elif key in [32]:
			FigureLine.new_cords['a'] = [FigureLine.current_cords['a'][0]+1,FigureLine.current_cords['a'][1]]
			FigureLine.new_cords['b'] = [FigureLine.current_cords['b'][0]+1,FigureLine.current_cords['b'][1]]
			FigureLine.new_cords['c'] = [FigureLine.current_cords['c'][0]+1,FigureLine.current_cords['c'][1]]
			FigureLine.new_cords['d'] = [FigureLine.current_cords['d'][0]+1,FigureLine.current_cords['d'][1]]

	def mark_cords_used(self):
		open('errors','a').write('marking used cords'+'\n')

		for key in FigureLine.new_cords:
			cord = FigureLine.new_cords[key]
			if cord not in tetris.USED_CORDS:
				tetris.USED_CORDS.append(cord)
		open('errors','a').write(json.dumps(tetris.USED_CORDS)+'\n')

	def check_new_cords(self):
		open('errors','a').write('checking new cords'+'\n')
		for key in FigureLine.new_cords:
			y, x = FigureLine.new_cords[key]
			if x in FigureLine.width_boundaries:
				open('errors','a').write('reached width boundary\n')
				FigureLine.new_cords = FigureLine.current_cords.copy()
				return None
			if y in FigureLine.height_boundaries:
				open('errors','a').write('reached height boundary\n')
				FigureLine.new_cords = FigureLine.current_cords.copy()
				return False

			if [y,x] in tetris.USED_CORDS:
				open('errors','a').write('reached used coordinates\n')
				FigureLine.new_cords = FigureLine.current_cords.copy()
				return False

		return True

	def check_termination(self):
		open('errors','a').write('checking termination\n')
		for key in FigureLine.new_cords:
			y,x = FigureLine.new_cords[key]
			if [y,x] in tetris.USED_CORDS:
				open('errors','a').write('reached termination point\n')
				FigureLine.new_cords = FigureLine.current_cords.copy()
				return True
		return False

	def draw(self,window,c=0):
		window.addch(FigureLine.cords['a'][0],FigureLine.cords['a'][1],'*')
		window.addch(FigureLine.cords['b'][0],FigureLine.cords['b'][1],'*')
		window.addch(FigureLine.cords['c'][0],FigureLine.cords['c'][1],'*')
		window.addch(FigureLine.cords['d'][0],FigureLine.cords['d'][1],'*')
		FigureLine.current_cords = FigureLine.cords.copy()
		FigureLine.new_cords = FigureLine.cords.copy()
		terminate = self.check_termination()
		return terminate

	def move(self, window, key):
		#first calculate new FigureLine.cords
		self.calculate_new_cords(key)
		open('errors','a').write('current cords'+'\n')
		open('errors','a').write(json.dumps(FigureLine.current_cords)+'\n')
		open('errors','a').write('new cords'+'\n')
		open('errors','a').write(json.dumps(FigureLine.new_cords)+'\n')
		status = self.check_new_cords()
		window.addch(FigureLine.current_cords['a'][0],FigureLine.current_cords['a'][1],' ')
		window.addch(FigureLine.current_cords['b'][0],FigureLine.current_cords['b'][1],' ')
		window.addch(FigureLine.current_cords['c'][0],FigureLine.current_cords['c'][1],' ')
		window.addch(FigureLine.current_cords['d'][0],FigureLine.current_cords['d'][1],' ')

		if status:
			open('errors','a').write('updating current cords'+'\n')
			FigureLine.current_cords = FigureLine.new_cords.copy()
			open('errors','a').write(json.dumps(FigureLine.current_cords)+'\n')
		if status == False:
			self.mark_cords_used()

		window.addch(FigureLine.new_cords['a'][0],FigureLine.new_cords['a'][1],'*')
		window.addch(FigureLine.new_cords['b'][0],FigureLine.new_cords['b'][1],'*')
		window.addch(FigureLine.new_cords['c'][0],FigureLine.new_cords['c'][1],'*')
		window.addch(FigureLine.new_cords['d'][0],FigureLine.new_cords['d'][1],'*')
		return status