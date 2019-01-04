import random
import math
import time

start_time = time.clock()

def getRandomQueens(n,p):
    # array = [i for i in range(n)]
    # queens = [0 for i in range(n)]
    # random.shuffle(array)
    # index = set()
    # for i in range(0,n):
    #     if i<p:
    #         queens[i] = array[i]
    #     else:
    #         queens[i] = -1
    # random.shuffle(queens)
    # while len(index)<p:
    #     index.add(random.randint(0, n - 1))
    # while len(index)>0:
    #     i = index.pop()
    #     queens[i] = random.randint(0, n - 1)
    # rand_list = random.randint(0, n+1)
    # print rand_list
    queens = [0 for i in range(n)]
    for i in range(0, n):
        queens[i] = random.randint(0, n-1)
    return queens

def calculateHeuristic(solution,n):
    score = 0
    global scooter
    for i in range(0, n):
        threat = 0
        for j in range(0, n):
            if (solution[i] == solution[j] or ((i - solution[i]) == (j - solution[j])) or ((i + solution[i]) == (j + solution[j]))) and i!=j:
                threat += 1
                break
        if threat == 0:
            score += scooter[i][solution[i]]

    return score

def simulatedAnnealing(solution,n,p):
    temperature = 400
    decay = 0.999999999999999999999999999999
    maxScore = 0
    for k in range(1000000):
        if temperature < 0.005:
            print "temp break"
            break
        temperature = temperature*decay
        new_solution = getRandomQueens(n,p)
        a = calculateHeuristic(new_solution,n)
        b = calculateHeuristic(solution,n)
        if a>maxScore:
            maxScore = a
        if b>maxScore:
            maxScore = b
        deltaE = a-b 
        if deltaE > 0:
            solution = new_solution
        prob = min(1,math.exp(deltaE/temperature))
        if random.uniform(0, 1) < prob:
            solution = new_solution
    return maxScore

# startTime = datetime.now()
file = open("input3.txt", "r")
lineCount = 0
for line in file:
  line = line.strip()
  if lineCount == 0:
    n = int(line)
    scooter = [[ 0 for x in range(n)] for y in range(n)]
  elif lineCount == 1:
    p = int(line)
  elif lineCount == 2:
    s = int(line)
    #scooter = [[[0,0] for x in range(12)] for y in range(s)]
  else:
    line = line.split(",")
    x = int(line[0])
    y = int(line[1])
    scooter[x][y] += 1
  lineCount += 1

solution = getRandomQueens(n,p)
print simulatedAnnealing(solution,n,p)
print time.clock() - start_time, "seconds"
