from numpy import *
import time
start_time = time.clock()

with open("input3.txt", 'r') as f:
    ar = f.readline()
    area = int(ar)

    print area

    of = f.readline()
    officer = int(of)

    print officer

    total_off = officer

    sc = f.readline()
    scooter = int(sc)

    scooter_count_arr = [[0 for i in xrange(area)] for j in xrange(area)]


with open("input3.txt", 'r') as f:
    f.readline()
    f.readline()
    f.readline()
    for line in f:
        a = line.split(',')[0]
        i = int(a)
        b = line.split(',')[1]
        j = int(b)

        scooter_count_arr[i][j] += 1

def is_safe_position(cop_matrix, row, col, area):
    # same row
    for a in range(area):
        if cop_matrix[row][a] == 1:
            return False
    # same column
    for a in range(area):
        if cop_matrix[a][col] == 1:
            return False

    # upper left diagonal
    a = row
    b = col
    while a >= 0 and b >= 0:
        if cop_matrix[a][b] == 1:
            return False
        a -= 1
        b -= 1

    # lower left diagonal
    p, q = row, col
    while p < area and q >= 0:
        if cop_matrix[p][q] == 1:
            return False
        p += 1
        q -= 1

    # upper right diagonal
    p, q = row, col
    while p >= 0 and q < area:
        if cop_matrix[p][q] == 1:
            return False
        p -= 1
        q += 1

    # lower right diagonal
    a = row
    b = col
    while a < area and b < area:
        if cop_matrix[a][b] == 1:
            return False
        a += 1
        b += 1

    return True


cop_matrix = [[0 for i in xrange(area)] for j in xrange(area)]

l = []
for i in xrange(area):
    for j in xrange(area):
        l.append((scooter_count_arr[i][j], i, j))

l.sort(reverse=True)


def check_officer(officer):
    total = officer
    max_points = 0
    for x in xrange(len(l)):
        cop_matrix = [[0 for n in xrange(area)] for m in xrange(area)]
        officer = total
        points = 0

        cop_matrix[l[x][1]][l[x][2]] = 1
        points += l[x][0]
        officer -= 1

        for j in range(len(l)):
            if officer == 0:

                break
            if is_safe_position(cop_matrix, l[j][1], l[j][2], area):

                cop_matrix[l[j][1]][l[j][2]] = 1
                points += l[j][0]
                officer -= 1

        if officer == 0:
            if max_points < points:
                max_points = points
    return max_points

def same_officer(cop_matrix, row, col, l, index,  officer):
    new_len = len(l)
    new_list = l[:]
    actual_len = len(l)
    for k in range(len(l)):
        cop_matrix = [[0 for i in xrange(area)] for j in xrange(area)]
        row = l[k][1]
        col = l[k][2]
        cop_matrix[row][col] = 1
        delete_ele = list()
        j = k 
        for j in range(actual_len - 1):
            for i in range(j + 1, new_len):
                if new_list[j][1] == new_list[i][1]:
                    delete_ele.append(new_list[i])
                if new_list[j][2] == new_list[i][2]:
                    delete_ele.append(new_list[i])
                if new_list[j][1] - new_list[j][2] == new_list[i][1] - new_list[i][2]:
                    delete_ele.append(new_list[i])
                if new_list[j][1] + new_list[j][2] == new_list[i][1] + new_list[i][2]:
                    delete_ele.append(new_list[i])
            
            new_list = [item for item in new_list if item not in delete_ele]
            
            new_len = len(new_list) - 1
            
            if new_len < officer:
                break
            print new_list
            actual_len -= 1
        new_list = [item for item in new_list if item not in [l[k]]]

def solution():
    index = 0
    row = l[index][1]
    col = l[index][2]
    if officer < area:
        val1 = check_officer(officer)
        print val1

    elif officer == area:
        if same_officer(cop_matrix, row, col, l, index, officer) == False:
            print "Solution does not exist"
            return False

solution()

print time.clock() - start_time, "seconds"

