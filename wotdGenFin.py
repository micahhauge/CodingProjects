from mechanize import ParseResponse, urlopen, urljoin
import requests
from lxml import html
import re
import random

###################################################################################################

class word():
	def __init__(self):
		self.name = ''

###################################################################################################

def randWord(wordType, wordComplexity):

	randURL = 'http://watchout4snakes.com'

	response = urlopen(urljoin(randURL, '/wo4snakes/Random/RandomWordPlus'))

	forms = ParseResponse(response, backwards_compat=False)
	form = forms[0]

	form['Pos'] = [wordType]
	form['Level'] = [wordComplexity]

	return urlopen(form.click()).read()

###################################################################################################

print 'Choices for Complexity: Very Common, Common, Average, Somewhat Uncommon, Uncommon, Very Uncommon, Obscure.'

looping = True
while looping == True:
	complexity = raw_input('Complexity: ')
	looping = False;
	if complexity == 'Very Common':
		wordComplexity = '10'
	elif complexity == 'Common':
		wordComplexity = '20'
	elif complexity == 'Average':
		wordComplexity = '35'
	elif complexity == 'Somewhat Uncommon':
		wordComplexity = '50'
	elif complexity == 'Uncommon':
		wordComplexity = '60'
	elif complexity == 'Very Uncommon':
		wordComplexity = '70'
	elif complexity == 'Obscure':
		wordComplexity = '95'
	else:
		looping = True

###################################################################################################

noun = word()
adj = word()
verb = word()
adverb = word()
prep = word()

wordNoun = 'n'
wordAdj = 'a'
wordVerb = 'i'
wordAdverb = 'e'
wordPrep = 's'

###################################################################################################

def sentence():

	noun.name = randWord(wordType = wordNoun, wordComplexity = wordComplexity)
	adj.name = randWord(wordType = wordAdj, wordComplexity = wordComplexity)
	verb.name = randWord(wordType = wordVerb, wordComplexity = wordComplexity)
	adverb.name = randWord(wordType = wordAdverb, wordComplexity = wordComplexity)
	prep.name = randWord(wordType = wordPrep, wordComplexity = wordComplexity)

	sentenceNoun = noun.name
	sentenceAdjective = adj.name
	sentenceVerb = verb.name
	sentenceAdverb = adverb.name
	sentencePreposition = prep.name

	vowels = ('a', 'e', 'i', 'o', 'u')

	sentenceStructure = random.randint(1, 3)
	round(sentenceStructure)

#################################################

	if sentenceStructure == 1:


		#Noun Grammar Rules
		if sentenceNoun.endswith('ct'):
			sentenceNoun += 's'
		elif sentenceNoun.endswith('t'):
			Grammar = True
		elif sentenceNoun.endswith('z'):
			sentenceNoun += 'es'
		elif sentenceNoun.endswith('x'):
			sentenceNoun += 'en'
		elif sentenceNoun.endswith('y'):
			sentenceNoun = sentenceNoun.replace('y', 'ies')
		elif sentenceNoun.endswith('rt'):
			sentenceNoun += 's'
		elif sentenceNoun.endswith ('et'):
			sentenceNoun += 's'
		
		elif sentenceNoun.endswith('ch'):
			sentenceNoun += 'es'
		else:
			sentenceNoun += 's'
		if 'oo' in sentenceNoun:
			sentenceNoun.replace('oo','ee')
			
#################################################
		
		#Adverb Grammar Rules
		if sentenceAdverb.endswith('o'):
			Grammar = True
		elif sentenceAdverb.endswith('ly'):
			Grammar = True
		elif sentenceAdverb.endswith('s'):
			Grammar = True
		elif sentenceAdverb.endswith('l'):
			sentenceAdverb += 'ishly'
		elif sentenceAdverb.endswith('e'):
			sentenceAdverb += 'dly'
		elif sentenceAdverb.endswith('est'):
			sentenceAdverb = sentenceAdverb.replace('est', 'ly')
		else:
			sentenceAdverb += 'ly'
			
#################################################
		
		#Adjective Grammar Rules
		if sentenceAdjective.endswith('e'):
			sentenceAdjective += 'd'
		elif sentenceAdjective.endswith('ism'):
			sentenceAdjective = sentenceAdjective.replace('ism', 'ist')
	
		if sentenceAdverb.startswith(vowels):
			aOrAn = 'an'
		else:
			aOrAn = 'a'
	
		print 'The', sentenceNoun, sentenceAdverb, 'complained about other more', sentenceAdjective, sentenceNoun	

#################################################

	elif sentenceStructure == 2:

		#Noun Grammar Rules
		if sentenceNoun.endswith('ism'):
			sentenceNoun = sentenceNoun.replace('ism', 'ist')

#################################################

		#Adverb Grammar Rules
		if sentenceAdverb.endswith('o'):
			Grammar = True
		elif sentenceAdverb.endswith('ly'):
			Grammar = True
		elif sentenceAdverb.endswith('s'):
			Grammar = True
		elif sentenceAdverb.endswith('l'):
			sentenceAdverb += 'ishly'
		elif sentenceAdverb.endswith('e'):
			sentenceAdverb += 'dly'
		elif sentenceAdverb.endswith('est'):
			sentenceAdverb = sentenceAdverb.replace('est', 'ly')
		else:
			sentenceAdverb += 'ly'
		
#################################################
		
		#Adjective Grammar Rules
		if sentenceAdjective.endswith('e'):
			sentenceAdjective += 'd'
		elif sentenceAdjective.endswith('ism'):
			sentenceAdjective = sentenceAdjective.replace('ism', 'ist')
	
		if sentenceAdverb.startswith(vowels):
			aOrAn = 'an'
		else:
			aOrAn = 'a'
	
		print '"Sorry!" said the', sentenceAdjective, sentenceNoun, ',', '"Im just', aOrAn, sentenceNoun, 'with', aOrAn, sentenceAdverb, sentenceAdjective, sentenceVerb, 'problem."'
	
#################################################

	elif sentenceStructure == 3:

		#Adverb Grammar Rules
		if sentenceAdverb.endswith('o'):
			Grammar = True
		elif sentenceAdverb.endswith('ly'):
			Grammar = True
		elif sentenceAdverb.endswith('s'):
			Grammar = True
		elif sentenceAdverb.endswith('l'):
			sentenceAdverb += 'ishly'
		elif sentenceAdverb.endswith('e'):
			sentenceAdverb += 'dly'
		elif sentenceAdverb.endswith('est'):
			sentenceAdverb = sentenceAdverb.replace('est', 'ly')
		else:
			sentenceAdverb += 'ly'
		
#################################################

		#Adjective Grammar Rules
		if sentenceAdjective.endswith('e'):
			sentenceAdjective += 'd'
		elif sentenceAdjective.endswith('ism'):
			sentenceAdjective = sentenceAdjective.replace('ism', 'ist')

#################################################
		
		#Verb Rules
		if sentenceVerb.endswith(''):
			sentenceVerb += 'ing'

		#Determines if a or an.
		if sentenceAdverb.startswith(vowels):
			aOrAn = 'an'
		else:
			aOrAn = 'a'

		print 'Who do you think you are?', aOrAn, sentenceAdverb, sentenceVerb, sentenceAdjective, sentenceNoun, '?', 'Well!?'

##################################################################################################

fuckMe = False

while fuckMe == True:
	sentence()

sentence()
	
	


















