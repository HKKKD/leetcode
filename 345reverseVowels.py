def reverseVowels(s):
		vowels = 'aeiouAEIOU'
		array = list()
		s = list(s)
		for x in s:
			if x in vowels:
				array.append(x)
		array.reverse()
		for i in range(0,len(s)):
			if s[i] in vowels: 
				s[i] = array.pop(0)
		return ''.join(s)

print reverseVowels('leetcode')