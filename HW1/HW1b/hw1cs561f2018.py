file_input = open('input.txt', 'rb')
file_output = open('output.txt','w')
list_input = file_input.read().splitlines()

grid_size = int(list_input[0])
no_of_police_officers = int(list_input[1])
no_of_scooters =  int(list_input[2])
coordinate_list = list()

for i in range(3, len(list_input)):
	coordinate_list.append((list_input[i]))

actual_grid = [[0 for i in range(grid_size)] for j in range(grid_size)]

for i in range(0, len(coordinate_list)):
	actual_grid[int(coordinate_list[i][:1])][int(coordinate_list[i][2:])] += 1
print actual_grid

nodes_dict = {(x,y):actual_grid[x][y] for x in range(grid_size) for y in range(grid_size)}

nodes_dict = {x: y for x, y in nodes_dict.iteritems()} #if y != 0
print nodes_dict

sorted_nodes_set = sorted(nodes_dict.items(), key=lambda x: x[1], reverse=True)
print sorted_nodes_set

# left_diagonal_dict = {(x,y):x - y for x in range(grid_size) for y in range(grid_size)}
# right_diagonal_dict = {(x,y):x + y for x in range(grid_size) for y in range(grid_size)}
activation_value = 0
delete_elements = list()
t = len(sorted_nodes_set)
# for i in range(no_of_police_officers):
for j in range(t):
	for k in range(j + 1, len(sorted_nodes_set)):
		try:
			if sorted_nodes_set[j][0][0] == sorted_nodes_set[k][0][0]:
				delete_elements.append(sorted_nodes_set[k])
				# print sorted_nodes_set[k]
				# del(sorted_nodes_set[k])

			elif sorted_nodes_set[j][0][1] == sorted_nodes_set[k][0][1]:
				delete_elements.append(sorted_nodes_set[k])
				# print sorted_nodes_set[k]
				# del(sorted_nodes_set[k])

			elif sorted_nodes_set[j][0][0] - sorted_nodes_set[j][0][1] == sorted_nodes_set[k][0][0] - sorted_nodes_set[k][0][1]:
				delete_elements.append(sorted_nodes_set[k])
				# print sorted_nodes_set[k]
				# del(sorted_nodes_set[k])

			elif sorted_nodes_set[j][0][0] + sorted_nodes_set[j][0][1] == sorted_nodes_set[k][0][0] + sorted_nodes_set[k][0][1]:
				delete_elements.append(sorted_nodes_set[k])
				# print sorted_nodes_set[k]
				# del(sorted_nodes_set[k])
		
		except:
			pass
	# break
	sorted_nodes_set = [item for item in sorted_nodes_set if item not in delete_elements]
	p = t
	t = len(sorted_nodes_set)
	if j == (no_of_police_officers - 1):
		print t
		print j
		break
	elif t == p:
		break
	print t
	print j
# print sorted_nodes_set
# print "!!!!!!!!"
# print delete_elements
if j == 0:
	activation_value = sorted_nodes_set[0][1]
else:
	for i in sorted_nodes_set:
		j = 1
		activation_value = activation_value + i[1]
		j += 1
		if j == no_of_police_officers:
			break
# sorted_nodes_set = [item for item in sorted_nodes_set if item not in delete_elements]
print sorted_nodes_set
print activation_value

# if len(sorted_nodes_set) < no_of_police_officers:
	#do nqueens problem

# for i in range(len(sorted_nodes_set)):
# 	for j in range(i + 1, len(sorted_nodes_set)):
# 		if sorted_nodes_set[i][0][0] == sorted_nodes_set[j][0][0]:
# 			sorted_nodes_set.remove(sorted_nodes_set[j])


# types1 = set(type(k) for k in nodes_dict.keys())
# print types1
# print type(nodes_dict[(0,0)])
#can use argmax from numpy with axis = 1 fpr etraction of max but it will return first of the two duplicates, need to find out a method to sort 2D array then traverse only first ???? integers from it
#what if max are duplicates then we will have to consider both cases

#depth of tree would be number of cops
#always select max from actual_grid as it represents max path
