import os
import re
import numpy as np
from gensim.models import KeyedVectors
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize, pos_tag
from collections import defaultdict
from nltk.corpus import wordnet as wn
def main():
	wv=KeyedVectors.load_word2vec_format('glove.6B.50d.txt',binary=False)
	sense_vector_file="test_sense_vectors_show.txt"
	tag_map = defaultdict(lambda : wn.NOUN)
	tag_map['J'] = wn.ADJ
	tag_map['V'] = wn.VERB
	tag_map['R'] = wn.ADV
	lmtzr = WordNetLemmatizer()
	word=input("enter any word").strip()
	line1=input("enter a line").strip()
	tokens = word_tokenize(line1)
	line1=line1.lower()
	for token, tag in pos_tag(tokens):
		lemma = lmtzr.lemmatize(token, tag_map[tag[0]])
		print(token, "=>", lemma, tag)
		lemma=lemma.lower()
		POS_DICT={'N':'NN','V':'VB','J':'JJ','R':'RB'}
		if lemma==word:
			pos=POS_DICT[tag[0]]
			print("POS")
			print(pos)
			word_regex=re.compile("([a-zA-z]+)")
			words_list=re.findall(word_regex,line1)
			words_list.remove(token)
			print(words_list)
	output_vector=os.popen("grep ^"+word+"#"+pos+" \"/home/nmn/jobim_naman/my programs/test_sense_vectors_show.txt\"").read()
	output_vector=output_vector.split("\n")
	output_vector=[o for o in output_vector if len(o)!=0]
	sense_vector_list=[]
	for line in output_vector:
		word1,counter,vector=line.split('\t')
		print (word,counter,vector)
		sense_vector_list.append(vector)
	print(sense_vector_list)
	context_words_vectors=[]
	print("#"*10)
	for i in words_list:
		if i in wv:
			a = wv.get_vector(i)
			print(a)
			print("printing a")
			context_words_vectors.append(a)
	print("context_words_vectors")
	print(context_words_vectors)
	context_words_vectors=np.array(context_words_vectors)
	print(context_words_vectors)
	numerator=0
	for i in context_words_vectors:
		numerator=np.add(i,numerator)
	print("numerator")
	print(numerator)

	denominator=len(context_words_vectors)
	print("denominator")
	print(denominator)

	if denominator != 0:
		aggregate_context_vector=np.divide(numerator,denominator)
		print("aggregate_context_vector=")
		print(aggregate_context_vector)
	cosine_similarity_list=[]
	for i in sense_vector_list:
		i=eval(i)
		cosine_similarity = np.dot(i,aggregate_context_vector) / (np.sqrt(np.dot(i,i)) * np.sqrt(np.dot(aggregate_context_vector,aggregate_context_vector)))
		cosine_similarity_list.append(cosine_similarity)
	print(cosine_similarity_list)
	sense_index=cosine_similarity_list.index(max(cosine_similarity_list))
	print("sense index=")
	print(word,pos,sense_index)
	print("#"*10)





	
if __name__ == '__main__':
	main()

