def getHint(secret,guess):
		secretL = list(secret); guessL = list(guess)
		bull = 0; cow = 0
		print secretL,'\n',guessL
		for x in range(0,len(guessL)):
			if guessL[x] == secretL[x]: 
				bull += 1
		for x in range(0,len(guessL)):
			if guessL[x] in secretL:
				print guessL[x]
				cow += 1
				secretL[secretL.index(guessL[x])] = 'used'
		return "%dA%dB"%(bull,cow)

print getHint('011','110')