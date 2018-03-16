#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pydeepl
import nltk

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

f = open('pdfcontents.txt', 'r')
chunks = f.readlines()
f.close()

#Splits the text into paragraphs
chunks = [chunk.strip() for chunk in chunks]
chunks = [chunk for chunk in chunks if chunk]

f = open('traduction.txt', 'w')
for chunk in chunks:

	#Are we dealing with a "real" paragraph or with a paragraph title, like "1.7.3. Extraction"?
	if chunk[0].isdigit(): 
		sentences = [chunk]
	else:
		#Joins sentences that had been split by line breaks in the PDF
		sentences = tokenizer.tokenize(chunk, realign_boundaries=True)
	
	#Translation is done sentence by sentence. If you chose to do it with whole paragraphs, in some cases only the beginning would be translated.
	for sentence in sentences:
	
		#remove this line if working with Python3
		sentence = sentence.decode('UTF-8')
		
		print(sentence+'\n\n')
		translation = pydeepl.translate(sentence, 'FR', from_lang='EN')
		print(translation+'\n---------------------------------')
		
		#Again, if working with Python3, no need to encode. f.write(translation+' ') should be fine
		f.write(translation.encode('utf-8')+' ')
	f.write('\n\n')
f.close()
