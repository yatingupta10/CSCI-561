import numpy as np

file_input = open('input.txt', 'rb')
file_output = open('output.txt','w')
list_input = file_input.read().splitlines()

grid_size = int(list_input[0])
no_of_cars = int(list_input[1])
no_of_obstacles = int(list_input[2])

temp_obstacles = list_input[3: 3 + int(no_of_obstacles)]
temp_starting_pos_cars = list_input[3 + no_of_obstacles: 3 + no_of_obstacles + no_of_cars]
temp_ending_pos_cars = list_input[3 + no_of_obstacles + no_of_cars: 3 + no_of_obstacles + no_of_cars + no_of_cars]

starting_pos_cars = []
for i in temp_starting_pos_cars:
	x = int(i.split(',')[0])
	y = int(i.split(',')[1])
	starting_pos_cars.append((x,y))

ending_pos_cars = []
for i in temp_ending_pos_cars:
	x = int(i.split(',')[0])
	y = int(i.split(',')[1])
	ending_pos_cars.append((x,y))

obstacles = []
for i in temp_obstacles:
	x = int(i.split(',')[0])
	y = int(i.split(',')[1])
	obstacles.append((x,y))

grid = [[-1 for i in range(grid_size)]for j in range(grid_size)]

for i in range(len(obstacles)):
	grid[obstacles[i][0]][obstacles[i][1]] = -101

def getting_direction(h, z, grid_size, utility):
	north1 = 0.0
	west1 = 0.0
	south1 = 0.0
	east1 = 0.0
	if h == 0  and z == 0:
		# print "0,0"
		north1 = 0.7*utility[h][z] + 0.1*utility[h][z+1] + 0.1*utility[h+1][z] + 0.1*utility[h][z]
 		west1 = 0.7*utility[h][z] + 0.1*utility[h][z+1] + 0.1*utility[h+1][z] + 0.1*utility[h][z]
		east1 = 0.7*utility[h][z+1]+ 0.1*utility[h+1][z] + 0.1*utility[h][z] + 0.1*utility[h][z]
		south1 = 0.7*utility[h+1][z]+ 0.1*utility[h][z+1] + 0.1*utility[h][z] + 0.1*utility[h][z]

	elif h == (grid_size - 1) and z == 0:
		# print "2,0"
		north1 = 0.7*utility[h-1][z]+ 0.1*utility[h][z+1] + 0.1*utility[h][z] + 0.1*utility[h][z]
		west1 = 0.7*utility[h][z]+ 0.1*utility[h-1][z] + 0.1*utility[h][z+1] + 0.1*utility[h][z]
		east1 = 0.7*utility[h][z+1]+ 0.1*utility[h-1][z] + 0.1*utility[h][z] + 0.1*utility[h][z]
		south1 = 0.7*utility[h][z]+ 0.1*utility[h-1][z] + 0.1*utility[h][z+1] + 0.1*utility[h][z]

	elif h == 0 and z == (grid_size - 1):
		# print "0,2"
		north1 = 0.7*utility[h][z]+ 0.1*utility[h][z-1] + 0.1*utility[h+1][z] + 0.1*utility[h][z]
		west1 = 0.7*utility[h][z-1]+ 0.1*utility[h+1][z] + 0.1*utility[h][z] + 0.1*utility[h][z]
		east1 = 0.7*utility[h][z]+ 0.1*utility[h][z-1] + 0.1*utility[h+1][z] + 0.1*utility[h][z]
		south1 = 0.7*utility[h+1][z]+ 0.1*utility[h][z-1] + 0.1*utility[h][z] + 0.1*utility[h][z]

	elif h == (grid_size - 1) and z == (grid_size - 1):
		# print "2,2"
		north1 = 0.7*utility[h-1][z]+ 0.1*utility[h][z-1] + 0.1*utility[h][z] + 0.1*utility[h][z]
		west1 = 0.7*utility[h][z-1]+ 0.1*utility[h-1][z] + 0.1*utility[h][z] + 0.1*utility[h][z]
		east1 = 0.7*utility[h][z]+ 0.1*utility[h-1][z] + 0.1*utility[h][z-1] + 0.1*utility[h][z]
		south1 = 0.7*utility[h][z]+ 0.1*utility[h-1][z] + 0.1*utility[h][z-1] + 0.1*utility[h][z]

	elif z == 0 and h > 0 and h < (grid_size-1):
		# print "1,0"
		north1 = 0.7*utility[h-1][z]+ 0.1*utility[h][z+1] + 0.1*utility[h+1][z] + 0.1*utility[h][z]
		east1 = 0.7*utility[h][z+1]+ 0.1*utility[h-1][z] + 0.1*utility[h+1][z] + 0.1*utility[h][z]
		west1 = 0.7*utility[h][z]+ 0.1*utility[h-1][z] + 0.1*utility[h+1][z] + 0.1*utility[h][z+1]
		south1 = 0.7*utility[h+1][z]+ 0.1*utility[h-1][z] + 0.1*utility[h][z+1] + 0.1*utility[h][z]

	elif h == (grid_size - 1) and z > 0 and z < (grid_size-1):
		# print "2,1"
		north1 = 0.7*utility[h-1][z]+ 0.1*utility[h][z+1] + 0.1*utility[h][z-1] + 0.1*utility[h][z]
		east1 = 0.7*utility[h][z+1]+ 0.1*utility[h-1][z] + 0.1*utility[h][z-1] + 0.1*utility[h][z]
		south1 = 0.7*utility[h][z]+ 0.1*utility[h-1][z] + 0.1*utility[h][z-1] + 0.1*utility[h][z+1]
		west1 = 0.7*utility[h][z-1]+ 0.1*utility[h-1][z] + 0.1*utility[h][z+1] + 0.1*utility[h][z]

	elif z == (grid_size-1) and h > 0 and h < (grid_size-1):
		# print "1,2"
		north1 = 0.7*utility[h-1][z]+ 0.1*utility[h][z-1] + 0.1*utility[h+1][z] + 0.1*utility[h][z]
		south1 = 0.7*utility[h+1][z]+ 0.1*utility[h-1][z] + 0.1*utility[h][z-1] + 0.1*utility[h][z]
		east1 = 0.7*utility[h][z]+ 0.1*utility[h][z-1] + 0.1*utility[h-1][z] + 0.1*utility[h+1][z]
		west1 = 0.7*utility[h][z-1]+ 0.1*utility[h-1][z] + 0.1*utility[h+1][z] + 0.1*utility[h][z]


	elif h == 0 and z > 0 and z < (grid_size-1):
		# print "0,1"
		east1 = 0.7*utility[h][z+1]+ 0.1*utility[h+1][z] + 0.1*utility[h][z-1] + 0.1*utility[h][z]
		south1 = 0.7*utility[h+1][z]+ 0.1*utility[h][z-1] + 0.1*utility[h][z+1] + 0.1*utility[h][z]
		north1 = 0.7*utility[h][z]+ 0.1*utility[h+1][z] + 0.1*utility[h][z-1] + 0.1*utility[h][z+1]
		west1 = 0.7*utility[h][z-1]+ 0.1*utility[h+1][z] + 0.1*utility[h][z+1] + 0.1*utility[h][z]

	else:# (h+1) < grid_size and (h-1) >= 0 and (z+1) < grid_size and (z-1) >=0:
		# print "1,1"
		north1 = 0.7*utility[h-1][z]+ 0.1*utility[h+1][z] + 0.1*utility[h][z-1] + 0.1*utility[h][z+1]
		south1 = 0.7*utility[h+1][z]+ 0.1*utility[h-1][z] + 0.1*utility[h][z-1] + 0.1*utility[h][z+1]
		east1 = 0.7*utility[h][z+1]+ 0.1*utility[h+1][z] + 0.1*utility[h][z-1] + 0.1*utility[h-1][z]
		west1 = 0.7*utility[h][z-1]+ 0.1*utility[h+1][z] + 0.1*utility[h-1][z] + 0.1*utility[h][z+1]
	max_var = max(north1, south1, east1, west1)
	return north1, south1, east1, west1, max_var

def opt_value(h, z, grid_size, utility):
	north1, south1, east1, west1, returning_var = getting_direction(h, z, grid_size, utility)
	# returning_var = max(north1, south1, east1, west1)
	return returning_var

def turn_left(move):
	if move == 'u':
		return 'l'
	if move == 'd':
		return 'r'
	if move == 'l':
		return 'd'
	if move == 'r':
		return 'u'

def turn_right(move):
	if move == 'u':
		return 'r'
	if move == 'd':
		return 'l'
	if move == 'l':
		return 'u'
	if move == 'r':
		return 'd'

def if_move_valid(move, c, d, grid_size):
	if move == 'u':
		if (c - 1) >= 0:
			return c-1, d
		else:
			# print i, j
			return c, d
	elif move == 'd':
		if (c + 1) < grid_size:
			return c+1, d
		else:
			return c, d
	elif move == 'l':
		if (d - 1) >= 0:
			return c, d-1
		else:
			# print i, j
			return c, d
	elif move == 'r':
		if (d + 1) < grid_size:
			return c, d+1
		else:
			return c, d

final_score = []
for i in range(no_of_cars): ##running for one car
	sx = []
	reward = [row[:] for row in grid]
	# print grid_copy
	reward[ending_pos_cars[i][0]][ending_pos_cars[i][1]] = 99 #starting position and ending positions keep on changing wrt cars
	utility = [[0 for q in range(grid_size)]for w in range(grid_size)]
	dir_matrix = [['' for f in range(grid_size)]for g in range(grid_size)]
	# print dir_matrix
	delta = float("inf")
	xyz = [row[:] for row in utility]
	while delta > (0.1*0.1/0.9):
		delta = 0
		for h in range(len(utility)):
			for z in range(len(utility[h])):
				if utility[h][z] != 99: #and (h != ending_pos_cars[i][0] and z != ending_pos_cars[i][1]):
					t = utility[h][z]
					# if opt_value(h, z, grid_size, utility) != 99:
					utility[h][z] = reward[h][z] + 0.9*opt_value(h, z, grid_size, xyz)
					if abs(utility[h][z] - t) > delta:
						delta =  abs(utility[h][z] - t)
				else:
					utility[h][z] = 99
		xyz = [row[:] for row in utility]

	for h in range(len(utility)):
		for z in range(len(utility[h])):
			n1, s1, e1, w1, max_var = getting_direction(h, z, grid_size, xyz)
			directions = [n1, s1, e1, w1]

			if max_var == w1:
				dir_matrix[h][z] = "l"
			elif max_var == e1:
				dir_matrix[h][z] = "r"
			elif max_var == s1:
				dir_matrix[h][z] = "d"
			else:
				dir_matrix[h][z] = "u"

	for j in range(10):
		pos = starting_pos_cars[i]
		np.random.seed(j)
		swerve = np.random.random_sample(1000000)	
		k=0	
		x = starting_pos_cars[i][0]
		y = starting_pos_cars[i][1]
		score = 0
		count = 0
		while pos != ending_pos_cars[i]:	
			move = dir_matrix[x][y]
			if	swerve[k] > 0.7:	
				if	swerve[k] > 0.8:	
					if	swerve[k] > 0.9:	
						move = turn_left(turn_left(move))
						temp = (x, y)
						x, y = if_move_valid(move, x, y, grid_size)
						pos = (x, y)
						score = score + reward[temp[0]][temp[1]]	
					else:	
						move = turn_left(move)
						temp = (x, y)
						x, y = if_move_valid(move, x, y, grid_size)
						pos = (x, y)
						score = score + reward[temp[0]][temp[1]]	
				else:	
					move = turn_right(move)
					count += 1
					temp = (x, y)
					x, y = if_move_valid(move, x, y, grid_size)
					pos = (x, y)
					score = score + reward[temp[0]][temp[1]]
			else:
				temp = (x, y)
				count += 1
				move = dir_matrix[x][y]
				x, y = if_move_valid(move, x, y, grid_size)
				pos = (x, y)
				score = score + reward[temp[0]][temp[1]]
				
			k+=1

		score = score + 100
		sx.append(score)
	avg_sx = np.floor(sum(sx) / float(len(sx)))
	final_score.append(avg_sx)

for i in range(len(final_score)):
    if i == (len(final_score)-1):
        file_output.write(str(int(final_score[i])))
    else:
    	file_output.write(str(int(final_score[i])) + '\n') 
