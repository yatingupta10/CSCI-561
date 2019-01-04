# import time

# start_time = time.clock()

file_input = open('input.txt', 'rb')
file_output = open('output.txt','w')
list_input = file_input.read().splitlines()

#################INPUTS#####################
no_of_beds_LAHSA = int(list_input[0])
no_of_parking_spaces_SPLA = int(list_input[1])

L = int(list_input[2])
LAHSA = list()
for i in range(0, L):
	LAHSA.append(list_input[3 + i])

SPLA = list()
S = int(list_input[2 + L + 1])
for i in range(0, S):
	SPLA.append(list_input[4 + L + i])

total_no_of_applicants = list_input[4 + int(L) + int(S)]
applicants = list()
for i in range(0, int(total_no_of_applicants)):
	applicants.append(list_input[5 + int(L) + int(S) + i])

LAHSA_capacity = [no_of_beds_LAHSA]*7
SPLA_capacity = [no_of_parking_spaces_SPLA]*7

for i in LAHSA:
	for j in applicants:
		if i == j[0:5]:
			try:
				L_list = list()
				L_list = list(str(j[13:]))
				L_list = map(int, L_list)
				for k in range(0, len(L_list)):
					LAHSA_capacity[k] = LAHSA_capacity[k] - L_list[k]
				applicants.remove(j)
			except:
				pass

for i in SPLA:
	for j in applicants:
		if i == j[0:5]:
			try:
				S_list = list()
				S_list = list(str(j[13:]))
				S_list = map(int, S_list)
				for k in range(0, len(S_list)):
					SPLA_capacity[k] = SPLA_capacity[k] - S_list[k]
				applicants.remove(j)
			except:
				pass

print LAHSA_capacity
print SPLA_capacity
no_of_beds_LAHSA = no_of_beds_LAHSA - L
no_of_parking_spaces_SPLA = no_of_parking_spaces_SPLA - S

probable_LAHSA = list()
for i in applicants:
	if (i[5] == "F") and (int(i[6:9]) > 17) and (i[9] == "N"):
		probable_LAHSA.append(i)

probable_SPLA = list()
for i in applicants:
	if (i[11] == "Y") and (i[10] == "N") and (i[12] == "Y"):
		probable_SPLA.append(i)


##########IMPLEMENTING MINIMAX###########################
# sum_val = 0
# max_val = 0
# for i in probable_LAHSA:
# 	if i in probable_SPLA:
# 		# max_ele = i 
# 		sum_val = sum(int(x) for x in i[13:] if x.isdigit())
# 		if sum_val > max_val:
# 			max_val = sum_val
# 			max_ele = i

# tree = dict({1:[(sum(SPLA_capacity), sum(LAHSA_capacity))]})
# print tree

Overlap_list = list(set(probable_SPLA).intersection(probable_LAHSA))
print "SPLA: " + str(probable_SPLA)
print "LAHSA: " + str(probable_LAHSA)
print "Overlap: " + str(Overlap_list)
print applicants
########################################################################################################
# # file_output.write(str(max_ele[0:5]))  
# # print max_ele
# # print max_val



# # probable_SPLA = ['00001M035NNYY1111111', '00004F025NNYY0000010', '00005F020YNYY0011000']
# # Overlap_list = ['00004F025NNYY0000010']
# # 1101110, 1001101

# # [[1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0, 1]]
# #1101110, 1001101
# capacity = SPLA_capacity[:]
# matrix = []

# Overlap_dict = dict()
# probable_SPLA_dict = dict()

# for i in probable_SPLA:
# 	element = i[13:]
# 	element = map(int, element)
# 	probable_SPLA_dict[i[0:5]] = element#.append({'element': i[0:5]})
# 	matrix.append(element)
# for i in Overlap_list:
# 	element = i[13:]
# 	element = map(int, element)
# 	Overlap_dict[i[0:5]] = element 


# Overlap_list = list(set(Overlap_list) - set(probable_SPLA))
# # print "Overlap_list: " + Ove
# # print Overlap_list
# for i in Overlap_list:
# 	element = i[13:]
# 	element = map(int, element)
# 	# Overlap_dict[i[0:5]] = element 
# 	matrix.append(element)

# matrix_desc = sorted(matrix, key=lambda x: sum(x), reverse = True)
# # matrix_asc = [list(t) for t in set(tuple(element) for element in matrix)]
# # matrix_asc = [list(t) for t in set(tuple(element) for element in matrix_asc)]
# matrix_asc = sorted(matrix, key=lambda x: sum(x))
# # print matrix_asc

# # matrix_asc = [list(set(matrix_asc))
# # print matrix_desc
# # print len(matrix_desc)

# def column(matrix, i):
#     return [row[i] for row in matrix]

# # final_desc_dict = dict()
# sum_x = 0
# sum_y = 0
# for i in range(len(matrix_desc)):
# 	x = []
# 	y = matrix_desc[:]
# 	if (matrix_desc[i][0] + sum(column(x, 0)))<= capacity[0] and (matrix_desc[i][1] + sum(column(x, 1)))<= capacity[1] and (matrix_desc[i][2] + sum(column(x, 2)))<= capacity[2] and (matrix_desc[i][3] + sum(column(x, 3)))<= capacity[3] and (matrix_desc[i][4] + sum(column(x, 4)))<= capacity[4] and (matrix_desc[i][5] + sum(column(x, 5)))<= capacity[5] and (matrix_desc[i][6] + sum(column(x, 6)))<= capacity[6]:
# 		x.append(matrix_desc[i])
# 		y.remove(matrix_desc[i])
# 		y = sorted(y, key=lambda z: sum(z), reverse=True )
# 	# print x
# 	for j in range(len(y)):
# 		# print matrix_desc[j][0]
# 		# print x[:][0]
# 		# print matrix_desc[j, 0]
# 		if (y[j][0] + sum(column(x, 0)))<= capacity[0] and (y[j][1] + sum(column(x, 1)))<= capacity[1] and (y[j][2] + sum(column(x, 2)))<= capacity[2] and (y[j][3] + sum(column(x, 3)))<= capacity[3] and (y[j][4] + sum(column(x, 4)))<= capacity[4] and (y[j][5] + sum(column(x, 5)))<= capacity[5] and (y[j][6] + sum(column(x, 6)))<= capacity[6]:
# 			x.append(y[j])
# 		# print "y: " + str(y[j]) 
# 	# sum_y = sum_x
# 	sum_x = sum(map(sum, x)) #sum 2d matrix
# 	if sum_x > sum_y:
# 		sum_y = sum_x
# 		final_desc_matrix = x

# sum_e = 0
# sum_f = 0
# for i in range(len(matrix_desc)):
# 	x = []
# 	# y = matrix_desc[:]
# 	if (matrix_desc[i][0] + sum(column(x, 0)))<= capacity[0] and (matrix_desc[i][1] + sum(column(x, 1)))<= capacity[1] and (matrix_desc[i][2] + sum(column(x, 2)))<= capacity[2] and (matrix_desc[i][3] + sum(column(x, 3)))<= capacity[3] and (matrix_desc[i][4] + sum(column(x, 4)))<= capacity[4] and (matrix_desc[i][5] + sum(column(x, 5)))<= capacity[5] and (matrix_desc[i][6] + sum(column(x, 6)))<= capacity[6]:
# 		x.append(matrix_desc[i])
# 	# y.remove(matrix_desc[i])
# 	# y = sorted(y, key=lambda z: sum(z), reverse=True )
# 	# print x
# 	for j in range((i+1), len(matrix_desc)):
# 		if (matrix_desc[j][0] + sum(column(x, 0)))<= capacity[0] and (matrix_desc[j][1] + sum(column(x, 1)))<= capacity[1] and (matrix_desc[j][2] + sum(column(x, 2)))<= capacity[2] and (matrix_desc[j][3] + sum(column(x, 3)))<= capacity[3] and (matrix_desc[j][4] + sum(column(x, 4)))<= capacity[4] and (matrix_desc[j][5] + sum(column(x, 5)))<= capacity[5] and (matrix_desc[j][6] + sum(column(x, 6)))<= capacity[6]:
# 			x.append(matrix_desc[j])
# 		# print "y: " + str(y[j]) 
# 	# sum_y = sum_x
# 	sum_e = sum(map(sum, x)) #sum 2d matrix
# 	if sum_e > sum_f:
# 		sum_f = sum_e
# 		final_desc_matrix1 = x

# sum_a = 0
# sum_z = 0
# for i in range(0, len(matrix_asc)):
# 	x = []
# 	y = matrix_asc[:]
# 	# print matrix_asc[i]
# 	if (matrix_asc[i][0] + sum(column(x, 0)))<= capacity[0] and (matrix_asc[i][1] + sum(column(x, 1)))<= capacity[1] and (matrix_asc[i][2] + sum(column(x, 2)))<= capacity[2] and (matrix_asc[i][3] + sum(column(x, 3)))<= capacity[3] and (matrix_asc[i][4] + sum(column(x, 4)))<= capacity[4] and (matrix_asc[i][5] + sum(column(x, 5)))<= capacity[5] and (matrix_asc[i][6] + sum(column(x, 6)))<= capacity[6]:	
# 		x.append(matrix_asc[i])
# 		y.remove(matrix_asc[i])
# 		y = sorted(y, key=lambda z: sum(z))
# 	for j in range(len(y)):
# 		# print matrix_asc[j]
# 		if (y[j][0] + sum(column(x, 0)))<= capacity[0] and (y[j][1] + sum(column(x, 1)))<= capacity[1] and (y[j][2] + sum(column(x, 2)))<= capacity[2] and (y[j][3] + sum(column(x, 3)))<= capacity[3] and (y[j][4] + sum(column(x, 4)))<= capacity[4] and (y[j][5] + sum(column(x, 5)))<= capacity[5] and (y[j][6] + sum(column(x, 6)))<= capacity[6]:
# 			x.append(y[j])
# 	# sum_z = sum_a
# 	sum_a = sum(map(sum, x)) #sum 2d matrix
# 	if sum_a > sum_z:
# 		# print sum_a
# 		sum_z = sum_a
# 		final_asc_matrix = x

# sum_g = 0
# sum_h = 0
# for i in range(len(matrix_asc)):
# 	x = []
# 	# y = matrix_desc[:]
# 	if (matrix_asc[i][0] + sum(column(x, 0)))<= capacity[0] and (matrix_asc[i][1] + sum(column(x, 1)))<= capacity[1] and (matrix_asc[i][2] + sum(column(x, 2)))<= capacity[2] and (matrix_asc[i][3] + sum(column(x, 3)))<= capacity[3] and (matrix_asc[i][4] + sum(column(x, 4)))<= capacity[4] and (matrix_asc[i][5] + sum(column(x, 5)))<= capacity[5] and (matrix_asc[i][6] + sum(column(x, 6)))<= capacity[6]:
# 		x.append(matrix_asc[i])
# 	# y.remove(matrix_desc[i])
# 	# y = sorted(y, key=lambda z: sum(z), reverse=True )
# 	# print x
# 	for j in range((i+1), len(matrix_asc)):
# 		if (matrix_asc[j][0] + sum(column(x, 0)))<= capacity[0] and (matrix_asc[j][1] + sum(column(x, 1)))<= capacity[1] and (matrix_asc[j][2] + sum(column(x, 2)))<= capacity[2] and (matrix_asc[j][3] + sum(column(x, 3)))<= capacity[3] and (matrix_asc[j][4] + sum(column(x, 4)))<= capacity[4] and (matrix_asc[j][5] + sum(column(x, 5)))<= capacity[5] and (matrix_asc[j][6] + sum(column(x, 6)))<= capacity[6]:
# 			x.append(matrix_asc[j])
# 		# print "y: " + str(y[j]) 
# 	# sum_y = sum_x
# 	sum_g = sum(map(sum, x)) #sum 2d matrix
# 	if sum_g > sum_h:
# 		sum_h = sum_g
# 		final_asc_matrix1 = x

# # print "final_desc_matrix: " + str(final_desc_matrix) #value taken by considering all desc matrix at every step
# # print "final_desc_matrix1: " + str(final_desc_matrix1) #value taken by moving forward
# # print "final_asc_matrix: " + str(final_asc_matrix) #value taken by considering all
# # print "final_asc_matrix1: " + str(final_asc_matrix1) #value taken by moving forward
# # print matrix_asc

# final_desc_matrix_value = sum(map(sum, final_desc_matrix))
# final_desc_matrix_value1 = sum(map(sum, final_desc_matrix1))
# final_asc_matrix_value = sum(map(sum, final_asc_matrix))
# final_asc_matrix_value1 = sum(map(sum, final_asc_matrix1))
# # print sum(map(sum, final_desc_matrix))
# # print sum(map(sum, final_desc_matrix1))
# # print sum(map(sum, final_asc_matrix))
# # print sum(map(sum, final_asc_matrix1))

# # if sum(map(sum, final_desc_matrix)) > sum(map(sum, final_asc_matrix)):
# # 	final_matrix = final_desc_matrix
# # 	result = final_desc_matrix[0]
# # elif sum(map(sum, final_asc_matrix)) > sum(map(sum, final_desc_matrix)):
# # 	final_matrix = final_asc_matrix
# # 	result = final_asc_matrix[-1]
# # print result
# # print probable_SPLA_dict
# # print [app_id for app_id, arr in probable_SPLA_dict.items() if arr == result]
# # # print probable_SPLA_dict.keys()[probable_SPLA_dict.values().index(result)]
# # print Overlap_dict.keys()[Overlap_dict.values().index(result)]

# # print "SPLA dict: " + str(probable_SPLA_dict)
# # print "Overlap_dict: " + str(Overlap_dict)
# # print "final_desc_matrix: " + str(final_desc_matrix) + " value: " + str(final_desc_matrix_value)
# # print "final_desc_matrix1: " + str(final_desc_matrix1) + " value: " + str(final_desc_matrix_value1)
# # print "final_asc_matrix: " + str(final_asc_matrix) + " value: " + str(final_asc_matrix_value)
# # print "final_asc_matrix1: " + str(final_asc_matrix1) + " value: " + str(final_asc_matrix_value1)

# if final_desc_matrix_value > final_desc_matrix_value1:
# 	FINAL_DESC_MATRIX = final_desc_matrix
# elif final_desc_matrix_value1 > final_desc_matrix_value:
# 	FINAL_DESC_MATRIX = final_desc_matrix1
# elif final_desc_matrix_value1 == final_desc_matrix_value: ##returning least overlap one
# 	l1 = []
# 	for i in final_desc_matrix:
# 		x = [app_id for app_id, arr in Overlap_dict.items() if arr == i]
# 		for x1 in x:
# 			l1.append(x1)
# 	l2 = []
# 	for j in final_desc_matrix1:
# 		x = [app_id for app_id, arr in Overlap_dict.items() if arr == j]
# 		for x1 in x:
# 			l2.append(x1)
# 	if len(l1) < len(l2):
# 		# print "yesss"
# 		FINAL_DESC_MATRIX = final_desc_matrix
# 	elif len(l2) < len(l1):
# 		FINAL_DESC_MATRIX = final_desc_matrix1
# 	elif len(l2) == len(l1):
# 		# print str(l1)
# 		# print str(l2)
# 		# print str(set(final_desc_matrix))
# 		final_desc_matrix2 = sorted(final_desc_matrix, key=lambda x: sum(x), reverse = True)
# 		final_desc_matrix3 = sorted(final_asc_matrix1, key=lambda x: sum(x), reverse = True)
# 		# if final_desc_matrix2 == final_desc_matrix3:
# 		FINAL_DESC_MATRIX = final_desc_matrix
# 		# else:
# 			#FINAL_DESC_MATRIX####think about it

# if final_asc_matrix_value > final_asc_matrix_value1:
# 	FINAL_ASC_MATRIX = final_asc_matrix
# elif final_asc_matrix_value1 > final_asc_matrix_value:
# 	FINAL_ASC_MATRIX = final_asc_matrix1
# elif final_asc_matrix_value1 == final_asc_matrix_value:
# 	l1 = []
# 	for i in final_desc_matrix:
# 		x = [app_id for app_id, arr in Overlap_dict.items() if arr == i]
# 		for x1 in x:
# 			l1.append(x1)
# 	l2 = []
# 	for j in final_asc_matrix1:
# 		x = [app_id for app_id, arr in Overlap_dict.items() if arr == j]
# 		for x1 in x:
# 			l2.append(x1)
# 	if len(l1) < len(l2):
# 		FINAL_ASC_MATRIX = final_asc_matrix
# 	elif len(l2) < len(l1):
# 		FINAL_ASC_MATRIX = final_asc_matrix1
# 	elif len(l2) == len(l1):
# 		final_asc_matrix2 = sorted(final_asc_matrix, key=lambda x: sum(x), reverse = True)
# 		final_asc_matrix3 = sorted(final_asc_matrix1, key=lambda x: sum(x), reverse = True)
# 		# if final_asc_matrix2 == final_asc_matrix3:
# 		FINAL_ASC_MATRIX = final_asc_matrix
# 		# else:
# 			#FINAL_ASC_MATRIX####think about it

# # print FINAL_DESC_MATRIX
# # print FINAL_ASC_MATRIX

# FINAL_DESC_MATRIX_VALUE = sum(map(sum, FINAL_DESC_MATRIX))
# FINAL_ASC_MATRIX_VALUE = sum(map(sum, FINAL_ASC_MATRIX))

# if FINAL_DESC_MATRIX_VALUE >= FINAL_ASC_MATRIX_VALUE:
# 	l1 = []
# 	for i in FINAL_DESC_MATRIX:
# 		x = [app_id for app_id, arr in Overlap_dict.items() if arr == i]
# 		for x1 in x:
# 			l1.append(x1)
# 	if len(l1) != 0:
# 		z = 0
# 		for j in l1:
# 			y = sum(Overlap_dict[j])
# 			if y > z:
# 				z = y
# 				result = j
# 	else:
# 		l2 = []
# 		for k in FINAL_DESC_MATRIX:
# 			x = [app_id for app_id, arr in probable_SPLA_dict.items() if arr == k]
# 			for x1 in x:
# 				l2.append(x1)
# 		z = 0
# 		for j in l2:
# 			y = sum(probable_SPLA_dict[j])
# 			if y > z:
# 				z = y
# 				result = j
# elif FINAL_DESC_MATRIX_VALUE < FINAL_ASC_MATRIX_VALUE:
# 	# print "yessssssssssssssss"
# 	l1 = []
# 	for i in FINAL_ASC_MATRIX:
# 		x = [app_id for app_id, arr in Overlap_dict.items() if arr == i]
# 		for x1 in x:
# 			l1.append(x1)
# 	# print l1
# 	if len(l1) != 0:
# 		z = 0
# 		for j in l1:
# 			y = sum(Overlap_dict[j])
# 			if y > z:
# 				z = y
# 				result = j
# 	else:
# 		# print "hi"
# 		l2 = []
# 		for k in FINAL_ASC_MATRIX:
# 			x = [app_id for app_id, arr in probable_SPLA_dict.items() if arr == k]
# 			for x1 in x:
# 				l2.append(x1)
# 		z = 0
# 		for j in l2:
# 			y = sum(probable_SPLA_dict[j])
# 			if y > z:
# 				z = y
# 				result = j

# # print result

# file_output.write(str(result)) 

##code tie breaker


matrix = []

Overlap_dict = dict()
probable_SPLA_dict = dict()

for i in probable_SPLA:
	element = i[13:]
	element = map(int, element)
	probable_SPLA_dict[i[0:5]] = element#.append({'element': i[0:5]})
	matrix.append(element)
for i in Overlap_list:
	element = i[13:]
	element = map(int, element)
	Overlap_dict[i[0:5]] = element 


Overlap_list = list(set(Overlap_list) - set(probable_SPLA))
# print "Overlap_list: " + Ove
print Overlap_list
for i in Overlap_list:
	element = i[13:]
	element = map(int, element)
	# Overlap_dict[i[0:5]] = element 
	matrix.append(element)

matrix_desc = sorted(matrix, key=lambda x: sum(x), reverse = True)
# matrix_asc = [list(t) for t in set(tuple(element) for element in matrix)]
# matrix_asc = [list(t) for t in set(tuple(element) for element in matrix_asc)]
matrix_asc = sorted(matrix, key=lambda x: sum(x))
print matrix_asc

# matrix_asc = [list(set(matrix_asc))
# print matrix_desc
# print len(matrix_desc)

def column(matrix, i):
    return [row[i] for row in matrix]

# final_desc_dict = dict()
sum_x = 0
sum_y = 0
for i in range(len(matrix_desc)):
	x = []
	y = matrix_desc[:]
	if (matrix_desc[i][0] + sum(column(x, 0)))<= capacity[0] and (matrix_desc[i][1] + sum(column(x, 1)))<= capacity[1] and (matrix_desc[i][2] + sum(column(x, 2)))<= capacity[2] and (matrix_desc[i][3] + sum(column(x, 3)))<= capacity[3] and (matrix_desc[i][4] + sum(column(x, 4)))<= capacity[4] and (matrix_desc[i][5] + sum(column(x, 5)))<= capacity[5] and (matrix_desc[i][6] + sum(column(x, 6)))<= capacity[6]:
		x.append(matrix_desc[i])
		y.remove(matrix_desc[i])
		y = sorted(y, key=lambda z: sum(z), reverse=True )
	# print x
	for j in range(len(y)):
		# print matrix_desc[j][0]
		# print x[:][0]
		# print matrix_desc[j, 0]
		if (y[j][0] + sum(column(x, 0)))<= capacity[0] and (y[j][1] + sum(column(x, 1)))<= capacity[1] and (y[j][2] + sum(column(x, 2)))<= capacity[2] and (y[j][3] + sum(column(x, 3)))<= capacity[3] and (y[j][4] + sum(column(x, 4)))<= capacity[4] and (y[j][5] + sum(column(x, 5)))<= capacity[5] and (y[j][6] + sum(column(x, 6)))<= capacity[6]:
			x.append(y[j])
		# print "y: " + str(y[j]) 
	# sum_y = sum_x
	sum_x = sum(map(sum, x)) #sum 2d matrix
	if sum_x > sum_y:
		sum_y = sum_x
		final_desc_matrix = x

sum_e = 0
sum_f = 0
for i in range(len(matrix_desc)):
	x = []
	# y = matrix_desc[:]
	if (matrix_desc[i][0] + sum(column(x, 0)))<= capacity[0] and (matrix_desc[i][1] + sum(column(x, 1)))<= capacity[1] and (matrix_desc[i][2] + sum(column(x, 2)))<= capacity[2] and (matrix_desc[i][3] + sum(column(x, 3)))<= capacity[3] and (matrix_desc[i][4] + sum(column(x, 4)))<= capacity[4] and (matrix_desc[i][5] + sum(column(x, 5)))<= capacity[5] and (matrix_desc[i][6] + sum(column(x, 6)))<= capacity[6]:
		x.append(matrix_desc[i])
	# y.remove(matrix_desc[i])
	# y = sorted(y, key=lambda z: sum(z), reverse=True )
	# print x
	for j in range((i+1), len(matrix_desc)):
		if (matrix_desc[j][0] + sum(column(x, 0)))<= capacity[0] and (matrix_desc[j][1] + sum(column(x, 1)))<= capacity[1] and (matrix_desc[j][2] + sum(column(x, 2)))<= capacity[2] and (matrix_desc[j][3] + sum(column(x, 3)))<= capacity[3] and (matrix_desc[j][4] + sum(column(x, 4)))<= capacity[4] and (matrix_desc[j][5] + sum(column(x, 5)))<= capacity[5] and (matrix_desc[j][6] + sum(column(x, 6)))<= capacity[6]:
			x.append(matrix_desc[j])
		# print "y: " + str(y[j]) 
	# sum_y = sum_x
	sum_e = sum(map(sum, x)) #sum 2d matrix
	if sum_e > sum_f:
		sum_f = sum_e
		final_desc_matrix1 = x

sum_a = 0
sum_z = 0
for i in range(0, len(matrix_asc)):
	x = []
	y = matrix_asc[:]
	# print matrix_asc[i]
	if (matrix_asc[i][0] + sum(column(x, 0)))<= capacity[0] and (matrix_asc[i][1] + sum(column(x, 1)))<= capacity[1] and (matrix_asc[i][2] + sum(column(x, 2)))<= capacity[2] and (matrix_asc[i][3] + sum(column(x, 3)))<= capacity[3] and (matrix_asc[i][4] + sum(column(x, 4)))<= capacity[4] and (matrix_asc[i][5] + sum(column(x, 5)))<= capacity[5] and (matrix_asc[i][6] + sum(column(x, 6)))<= capacity[6]:	
		x.append(matrix_asc[i])
		y.remove(matrix_asc[i])
		y = sorted(y, key=lambda z: sum(z))
	for j in range(len(y)):
		# print matrix_asc[j]
		if (y[j][0] + sum(column(x, 0)))<= capacity[0] and (y[j][1] + sum(column(x, 1)))<= capacity[1] and (y[j][2] + sum(column(x, 2)))<= capacity[2] and (y[j][3] + sum(column(x, 3)))<= capacity[3] and (y[j][4] + sum(column(x, 4)))<= capacity[4] and (y[j][5] + sum(column(x, 5)))<= capacity[5] and (y[j][6] + sum(column(x, 6)))<= capacity[6]:
			x.append(y[j])
	# sum_z = sum_a
	sum_a = sum(map(sum, x)) #sum 2d matrix
	if sum_a > sum_z:
		# print sum_a
		sum_z = sum_a
		final_asc_matrix = x

sum_g = 0
sum_h = 0
for i in range(len(matrix_asc)):
	x = []
	# y = matrix_desc[:]
	if (matrix_asc[i][0] + sum(column(x, 0)))<= capacity[0] and (matrix_asc[i][1] + sum(column(x, 1)))<= capacity[1] and (matrix_asc[i][2] + sum(column(x, 2)))<= capacity[2] and (matrix_asc[i][3] + sum(column(x, 3)))<= capacity[3] and (matrix_asc[i][4] + sum(column(x, 4)))<= capacity[4] and (matrix_asc[i][5] + sum(column(x, 5)))<= capacity[5] and (matrix_asc[i][6] + sum(column(x, 6)))<= capacity[6]:
		x.append(matrix_asc[i])
	# y.remove(matrix_desc[i])
	# y = sorted(y, key=lambda z: sum(z), reverse=True )
	# print x
	for j in range((i+1), len(matrix_asc)):
		if (matrix_asc[j][0] + sum(column(x, 0)))<= capacity[0] and (matrix_asc[j][1] + sum(column(x, 1)))<= capacity[1] and (matrix_asc[j][2] + sum(column(x, 2)))<= capacity[2] and (matrix_asc[j][3] + sum(column(x, 3)))<= capacity[3] and (matrix_asc[j][4] + sum(column(x, 4)))<= capacity[4] and (matrix_asc[j][5] + sum(column(x, 5)))<= capacity[5] and (matrix_asc[j][6] + sum(column(x, 6)))<= capacity[6]:
			x.append(matrix_asc[j])
		# print "y: " + str(y[j]) 
	# sum_y = sum_x
	sum_g = sum(map(sum, x)) #sum 2d matrix
	if sum_g > sum_h:
		sum_h = sum_g
		final_asc_matrix1 = x

print "final_desc_matrix: " + str(final_desc_matrix) #value taken by considering all desc matrix at every step
print "final_desc_matrix1: " + str(final_desc_matrix1) #value taken by moving forward
print "final_asc_matrix: " + str(final_asc_matrix) #value taken by considering all
print "final_asc_matrix1: " + str(final_asc_matrix1) #value taken by moving forward
# print matrix_asc

final_desc_matrix_value = sum(map(sum, final_desc_matrix))
final_desc_matrix_value1 = sum(map(sum, final_desc_matrix1))
final_asc_matrix_value = sum(map(sum, final_asc_matrix))
final_asc_matrix_value1 = sum(map(sum, final_asc_matrix1))
# print sum(map(sum, final_desc_matrix))
# print sum(map(sum, final_desc_matrix1))
# print sum(map(sum, final_asc_matrix))
# print sum(map(sum, final_asc_matrix1))

# if sum(map(sum, final_desc_matrix)) > sum(map(sum, final_asc_matrix)):
# 	final_matrix = final_desc_matrix
# 	result = final_desc_matrix[0]
# elif sum(map(sum, final_asc_matrix)) > sum(map(sum, final_desc_matrix)):
# 	final_matrix = final_asc_matrix
# 	result = final_asc_matrix[-1]
# print result
# print probable_SPLA_dict
# print [app_id for app_id, arr in probable_SPLA_dict.items() if arr == result]
# # print probable_SPLA_dict.keys()[probable_SPLA_dict.values().index(result)]
# print Overlap_dict.keys()[Overlap_dict.values().index(result)]

print "SPLA dict: " + str(probable_SPLA_dict)
print "Overlap_dict: " + str(Overlap_dict)
print "final_desc_matrix: " + str(final_desc_matrix) + " value: " + str(final_desc_matrix_value)
print "final_desc_matrix1: " + str(final_desc_matrix1) + " value: " + str(final_desc_matrix_value1)
print "final_asc_matrix: " + str(final_asc_matrix) + " value: " + str(final_asc_matrix_value)
print "final_asc_matrix1: " + str(final_asc_matrix1) + " value: " + str(final_asc_matrix_value1)

if final_desc_matrix_value > final_desc_matrix_value1:
	FINAL_DESC_MATRIX = final_desc_matrix
elif final_desc_matrix_value1 > final_desc_matrix_value:
	FINAL_DESC_MATRIX = final_desc_matrix1
elif final_desc_matrix_value1 == final_desc_matrix_value: ##returning least overlap one
	l1 = []
	for i in final_desc_matrix:
		x = [app_id for app_id, arr in Overlap_dict.items() if arr == i]
		for x1 in x:
			l1.append(x1)
	l2 = []
	for j in final_desc_matrix1:
		x = [app_id for app_id, arr in Overlap_dict.items() if arr == j]
		for x1 in x:
			l2.append(x1)
	if len(l1) < len(l2):
		# print "yesss"
		FINAL_DESC_MATRIX = final_desc_matrix
	elif len(l2) < len(l1):
		FINAL_DESC_MATRIX = final_desc_matrix1
	elif len(l2) == len(l1):
		# print str(l1)
		# print str(l2)
		# print str(set(final_desc_matrix))
		final_desc_matrix2 = sorted(final_desc_matrix, key=lambda x: sum(x), reverse = True)
		final_desc_matrix3 = sorted(final_asc_matrix1, key=lambda x: sum(x), reverse = True)
		# if final_desc_matrix2 == final_desc_matrix3:
		FINAL_DESC_MATRIX = final_desc_matrix
		# else:
			#FINAL_DESC_MATRIX####think about it

if final_asc_matrix_value > final_asc_matrix_value1:
	FINAL_ASC_MATRIX = final_asc_matrix
elif final_asc_matrix_value1 > final_asc_matrix_value:
	FINAL_ASC_MATRIX = final_asc_matrix1
elif final_asc_matrix_value1 == final_asc_matrix_value:
	l1 = []
	for i in final_desc_matrix:
		x = [app_id for app_id, arr in Overlap_dict.items() if arr == i]
		for x1 in x:
			l1.append(x1)
	l2 = []
	for j in final_asc_matrix1:
		x = [app_id for app_id, arr in Overlap_dict.items() if arr == j]
		for x1 in x:
			l2.append(x1)
	if len(l1) < len(l2):
		FINAL_ASC_MATRIX = final_asc_matrix
	elif len(l2) < len(l1):
		FINAL_ASC_MATRIX = final_asc_matrix1
	elif len(l2) == len(l1):
		final_asc_matrix2 = sorted(final_asc_matrix, key=lambda x: sum(x), reverse = True)
		final_asc_matrix3 = sorted(final_asc_matrix1, key=lambda x: sum(x), reverse = True)
		# if final_asc_matrix2 == final_asc_matrix3:
		FINAL_ASC_MATRIX = final_asc_matrix
		# else:
			#FINAL_ASC_MATRIX####think about it

print FINAL_DESC_MATRIX
print FINAL_ASC_MATRIX

FINAL_DESC_MATRIX_VALUE = sum(map(sum, FINAL_DESC_MATRIX))
FINAL_ASC_MATRIX_VALUE = sum(map(sum, FINAL_ASC_MATRIX))

if FINAL_DESC_MATRIX_VALUE >= FINAL_ASC_MATRIX_VALUE:
	l1 = []
	for i in FINAL_DESC_MATRIX:
		x = [app_id for app_id, arr in Overlap_dict.items() if arr == i]
		for x1 in x:
			l1.append(x1)
	if len(l1) != 0:
		z = 0
		z_id = 0
		for j in l1:
			y = sum(Overlap_dict[j])
			if y > z:
				z = y
				z_id = j
				result = j
			elif y == z:
				if int(j) < int(z_id):
					result = j
	else:
		l2 = []
		for k in FINAL_DESC_MATRIX:
			x = [app_id for app_id, arr in probable_SPLA_dict.items() if arr == k]
			for x1 in x:
				l2.append(x1)
		z = 0
		z_id = 0
		for j in l2:
			y = sum(probable_SPLA_dict[j])
			if y > z:
				z = y
				z_id = j
				result = j
			elif y == z:
				if int(j) < int(z_id):
					result = j
elif FINAL_DESC_MATRIX_VALUE < FINAL_ASC_MATRIX_VALUE:
	# print "yessssssssssssssss"
	l1 = []
	for i in FINAL_ASC_MATRIX:
		x = [app_id for app_id, arr in Overlap_dict.items() if arr == i]
		for x1 in x:
			l1.append(x1)
	print l1
	if len(l1) != 0:
		z = 0
		z_id = 0
		for j in l1:
			y = sum(Overlap_dict[j])
			if y > z:
				z = y
				z_id = j
				result = j
			elif y == z:
				if int(j) < int(z_id):
					result = j
	else:
		# print "hi"
		l2 = []
		for k in FINAL_ASC_MATRIX:
			x = [app_id for app_id, arr in probable_SPLA_dict.items() if arr == k]
			for x1 in x:
				l2.append(x1)
		z = 0
		z_id = 0
		for j in l2:
			y = sum(probable_SPLA_dict[j])
			if y > z:
				z = y
				z_id = j
				result = j
			elif y == z:
				if int(j) < int(z_id):
					result = j

print result
