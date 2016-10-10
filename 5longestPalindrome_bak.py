def longestPalindrome(s):
		def isPalindrome(s):
			s = s.lower()
			l = 0
			r = len(s) - 1
			while l < r:
				if s[l].isalnum() is not True:
					l += 1
				elif s[r].isalnum() is not True:
					r -= 1
				elif s[l] != s[r]:
					return False
				else:
					l += 1
					r -= 1
			return True
		s = s.lower()
		array = list()
		r = len(s)
		for l in xrange(0,r):
			r = len(s)
			while r > l:
				if isPalindrome(s[l:r]):
					array.append([l,r])
					break
				else:
					r -= 1
		re = 0
		ree = [0,0]
		for x in array:
			if x[1] - x[0] > re:
				re = x[1] - x[0]
				ree.pop(0)
				ree.pop(0)
				ree.append(x[0])
				ree.append(x[1])	
		return s[ree[0]:ree[1]]

print longestPalindrome("ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy")