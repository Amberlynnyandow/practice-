
#def palindrome(text): 
	text = text.lower().replace(' ', '')
	x = text[::-1]
	if x == text:
		print('True') 
	else:
		print('False') 

#text = 'A nut for a jar of tuna'
#palindrome(text)

import time 
import random 
letters = 'ab'
text = ''.join([random.choice(letters) for x in range(1000000)])
text 