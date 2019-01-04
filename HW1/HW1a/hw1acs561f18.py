file_input = open('input.txt', 'rb')
file_output = open('output.txt','w')
list_input = file_input.read().splitlines()
i = 0

for element in list_input:
	if element[2:] == "Dirty":
		file_output.write("Suck" )#return SUCK 
	elif element[2:] == "Clean":
		if element[0] == "A":
			file_output.write("Right")#return right
		if element[0] == "B":
			file_output.write("Left")#return left
	
	i = i + 1
	
	if i != len(list_input): 
		file_output.write("\n")