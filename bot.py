import numpy as np 
import random


def Bernoulli(p):
	if (random.random()<p):
		return 1
	return 0

def generateAns(probaArray, nbLine):
	out = np.zeros((nbLine, len(probaArray)), dtype=int)
	for l in range(nbLine):
		out[l] = [Bernoulli(p) if p is not None else -1 for p in probaArray]
	return out

def generateAnsBonobo(nbLine, nbCol):
	'''
	-1 : ne pas répondre
	 0 : répondre F
	+1 : répondre V 
	'''
	return np.random.randint(3, size=(nbLine, nbCol)) - 1

def generateAnsBinomial(nbLine, nbCol, p):
	return np.random.binomial(1, p, size=(nbLine, nbCol))

def getAnsScore(ans, cor):
	assert ans.shape == cor.shape
	nrows, ncols = ans.shape
	score = 0
	for l in range(nrows):

		tmp = 0
		for c in range(ncols):
			if ans[l][c] != -1:
				tmp += 1 if ans[l][c]==cor[l][c] else -1
		
		if tmp<0: # A question score cannot < 0
			tmp = 0
		elif tmp>=4: # bonus
			tmp += 1 

		score += tmp
	return score

def getNote(score, total):
	return 20*score/total

result = [
[0, 0, 1, 1, 0],
[0, 1, 0, 1, 1],
[1, 0, 0, 1, 1],
[1, 1, 0, 1, 1],
[1, 0, 1, 1, 0],
[0, 0, 0, 0, 1],
[1, 0, 0, 0, 0],
[0, 0, 1, 1, 0],
[0, 1, 0, 1, 1],
[1, 1, 1, 0, 1],
[1, 1, 1, 1, 0],
[1, 1, 1, 0, 1],
[1, 1, 1, 1, 0],
[0, 1, 0, 1, 0],
[1, 1, 0, 1, 1],
[0, 1, 1, 1, 1],
[1, 0, 1, 0, 1]
]

cor = np.array(result)
nrows, ncols = cor.shape
size = cor.size

probaArray = [column.sum()/cor.shape[0] for column in cor.T]
print(probaArray, '\n')

N = 10000

# -----------------------------------------------------------
print("Strategie : répondre aux questions avec les p précalculés") 

total = 0
for _ in range(N):
	ans = generateAns(probaArray, nrows)
	total += getAnsScore(ans, cor)
mean =  total/N
print("note : {:.2f} / 20".format(getNote(mean, size)), '\n')

# -----------------------------------------------------------
print("Strategie : répondre aux questions avec (p> 0.55)") 

probaArray2 = [p if p > 0.55 else -1 for p in probaArray]
total = 0
for _ in range(N):
	ans = generateAns(probaArray2, cor.shape[0])
	total += getAnsScore(ans, cor)
mean =  total/N
print("note : {:.2f} / 20".format(getNote(mean, size)), '\n')

'''--------- Strategie 2 : bonobo '''
print("Strategie : toujours répondre au hasard avec abstention")

total = 0
for _ in range(N):
	ans = generateAnsBonobo(nrows, ncols)
	total += getAnsScore(ans, cor)
mean =  total/N
print("note : {:.2f} / 20".format(getNote(mean, size)), '\n')

# -----------------------------------------------------------
print("Strategie : répondre avec p=0.5")

total = 0
for _ in range(N):
	ans = generateAnsBinomial(nrows, ncols, 0.5)
	total += getAnsScore(ans, cor)
mean =  total/N
print("note : {:.2f} / 20".format(getNote(mean, size)), '\n')


# -----------------------------------------------------------
print("Strategie : répondre avec p=0.6")

total = 0
for _ in range(N):
	ans = generateAnsBinomial(nrows, ncols, 0.6)
	total += getAnsScore(ans, cor)
mean =  total/N
print("note : {:.2f} / 20".format(getNote(mean, size)), '\n')

# -----------------------------------------------------------
print("Strategie : répondre toujours V (p=1)")

ans = np.ones(shape=(nrows, ncols))
mean = getAnsScore(ans, cor)
print("note : {:.2f} / 20".format(getNote(mean, size)), '\n')

# -----------------------------------------------------------
print("Strategie : répondre toujours F (p=0)")

ans = np.zeros(shape=(nrows, ncols))
mean = getAnsScore(ans, cor)
print("note : {:.2f} / 20".format(getNote(mean, size)), '\n')
