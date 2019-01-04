import time

start_time = time.clock()

x = ['*', '00001F020NNYY1001000', '00003M040NNYY1000110', '00004M033NNYY1000000']
probable_SPLA = ['00001F020NNYY1001000', '00003M040NNYY1000110', '00004M033NNYY1000000'] #, '00005M040NNYY1000111', '00006M040NNYY1000110'
probable_LAHSA = ['00001F020NNYY1001000', '00005M040NNYY1000111'] #'00007M040NNYY1000001'
LAHSA_capacity = [10]*7
SPLA_capacity = [10]*7

class Node(object):
    def __init__(self, value, children = [], parent=None):
        self.value     = value
        self.children  = children
        self.parent = parent

    def other_name(self, level=0):
    	print '\t' * level + repr(self.value)
    	for child in self.children:
        	child.other_name(level+1)

    def addChildren(self, child):
    	self.children.append(child)

probable_SPLA_1 = probable_SPLA
probable_LAHSA_1 = probable_LAHSA

# SPLA_capacity1 = [10]*7
# def tree_to_list(atree): 
#     return [atree.value]+[tree_to_list(c) for c in atree.children]
def func(rootNode, player):
	
	if player == "spla":
		# probable_SPLA = probable_SPLA_1
		for i in range(len(probable_SPLA)):
			# if rootNode.value == "*,*":
			# 	rootNode_Value = [0, 0, 0, 0, 0, 0, 0]
			flag = 0
			# flag1 = 0
			# probable_SPLA  = probable_SPLA_1
			try:
				candidate = probable_SPLA[i]
				childNode = Node(candidate, [], rootNode)
			# 	try:
			# 		# rootNode_Value = list(rootNode.value[13:])
			# 		# rootNode_Value = map(int, rootNode_Value)
			# 	# rootNode_Value = rootNode.value.split(',')[1]
			# 		childNode_Value = list(candidate[13:])
			# 		childNode_Value = map(int, childNode_Value)

			# 		Sum_Value = [sum(x) for x in zip(rootNode_Value, childNode_Value)]

			# 		for x,y in zip(Sum_Value, SPLA_capacity):
			# 			if x > y:
			# 				flag1 =1
			# 				break

			# 		# print Sum_Value
			# 	except:
			# 		pass
				# print childNode_Value
				# probable_SPLA.remove(candidate)
				# try:
				# 	# print "1"
				# 	# if candidate in probable_LAHSA:
				# 	# print "removed : "+ candidate
				# 	probable_LAHSA_index = probable_LAHSA.index(candidate)
				# 	probable_LAHSA.remove(candidate)
				# 	flag = 1
				# except:
				# 	pass
				rootNode.addChildren(childNode)
				# if flag1 == 1:
				# 	break
				# else:
					# rootNode_Value = [sum(x) for x in zip(rootNode_Value, childNode_Value)]
				# childNode_Value = list(candidate[13:])
				# childNode_Value = map(int, childNode_Value)
				# SPLA_capacity1 = [r - m for r, m in zip(SPLA_capacity1, childNode_Value)]

				probable_SPLA.remove(candidate)
				try:
					probable_LAHSA_index = probable_LAHSA.index(candidate)
					probable_LAHSA.remove(candidate)
					flag = 1
				except:
					pass
				# rootNode.addChildren(childNode)
				func(childNode,"lahsa")
				probable_SPLA.insert(i, candidate)
				if flag == 1:
					# print "2"
					# print "inserted : "+candidate
					probable_LAHSA.insert(probable_LAHSA_index, candidate)
				# print "spla: " + str(rootNode_Value)
				print "$$$$$$"
				childNode_Value = list(candidate[13:])
				print "1"
				childNode_Value = map(int, childNode_Value)
				print "2"
				SPLA_capacity1 = [sum(x) for x in zip(SPLA_capacity, childNode_Value)]
				# SPLA_capacity = SPLA_capacity1
				print "3"
				print "within loop:" + str(candidate) + str(SPLA_capacity1)
			except:
				pass
			# probable_SPLA.remove(candidate) #remove candidate
		# func(childNode)
		# probable_SPLA.append(candidate)# add candidate
	if player == "lahsa":
		for j in range(len(probable_LAHSA)):
			flag = 0
			# flag1 = 0
			# if candidate1 != candidate:
			try:
				candidate1 = probable_LAHSA[j]
				childNode1 = Node(candidate1, [], rootNode)
				# try:
				# 	# rootNode_Value = list(rootNode.value[13:])
				# 	# rootNode_Value = map(int, rootNode_Value)
				# # rootNode_Value = rootNode.value.split(',')[1]
				# 	childNode1_Value = list(candidate1[13:])
				# 	childNode1_Value = map(int, childNode1_Value)

				# 	Sum1_Value = [sum(x) for x in zip(rootNode_Value, childNode1_Value)]

				# 	for x,y in zip(Sum1_Value, LAHSA_capacity):
				# 		if x > y:
				# 			flag1 = 1
				# 			break

				# 	# print Sum_Value
				# except:
				# 	pass
				# probable_LAHSA.remove(candidate1)
				# try:
				# 	probable_SPLA_index = probable_SPLA.index(candidate1)
				# 	probable_SPLA.remove(candidate1)
				# 	flag = 1
				# except:
				# 	pass
				rootNode.addChildren(childNode1)
				# if flag1 == 1:
				# 	break
				# else:
					# rootNode_Value = [sum(x) for x in zip(rootNode_Value, childNode1_Value)]
				# childNode1_Value = list(candidate1[13:])
				# childNode1_Value = map(int, childNode1_Value)
				# LAHSA_capacity = [r - m for r, m in zip(LAHSA_capacity, childNode1_Value)]
				probable_LAHSA.remove(candidate1)
				try:
					probable_SPLA_index = probable_SPLA.index(candidate1)
					probable_SPLA.remove(candidate1)
					flag = 1
				except:
					pass
				# rootNode.addChildren(childNode1)
				func(childNode1, "spla")
				probable_LAHSA.insert(j, candidate1)
				# childNode1_Value = list(candidate1[13:])
				# childNode1_Value = map(int, childNode1_Value)
				# LAHSA_capacity = [r + m for r, m in zip(LAHSA_capacity, childNode1_Value)]
				if flag == 1:
					probable_SPLA.insert(probable_SPLA_index, candidate1)
				# print "lahsa: " + str(rootNode_Value)
			except:
				pass

t = Node("*,*", [])
func(t, "spla")
print probable_SPLA
print probable_LAHSA
t.other_name()
print time.clock() - start_time, "seconds"
print SPLA_capacity