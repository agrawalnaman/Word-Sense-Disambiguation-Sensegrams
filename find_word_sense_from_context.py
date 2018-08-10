import re
import os

def find_cluster(words_list,word,pos="default"):
	POS_DICT={'n':'NN','v':'VB','a':'JJ','r':'RB'}
	max_common,max_common_index,max_common_key=[[],0,""]
	if pos!="default" and pos in POS_DICT:
		output=os.popen("grep ^"+word+"#"+POS_DICT[pos]+"~/wikipedia_stanford_cluster_a1_N200_n200_labelled").read()
	else:
		output=os.popen("grep ^"+word+"#"+" ~/wikipedia_stanford_cluster_a1_N200_n200_labelled").read()
	output=output.split("\n")
	output=[o for o in output if len(o)!=0]
	for string in output:
		key,index,similar,hypernym=string.split('\t')
		similar=[i.split('#')[0].lower() for i in similar.split(', ')]
		if len(list(set(similar).intersection(words_list)))>=len(max_common):
			max_common=list(set(similar).intersection(words_list))
			max_common_index=index
			max_common_key=key
	print(word,max_common_key,max_common_index,max_common)
	return


def main():
#	s=re.compile("TRANSLATION\n(.*)\n((PURPORT)|(TRANSLATION))")
#	file_content=open('gita_eng.txt').readlines()
	word=input("enter any word").strip()
	line1=input("enter a line").strip()
	line=line1.lower()
	word_regex=re.compile("([a-zA-z]+)")
	words_list=re.findall(word_regex,line)
#	matches=re.findall(s,file_content)
#	print(len(matches))
#	print(matches)
	words_list.remove(word)
	find_cluster(words_list,word)




if __name__ == '__main__':
	main()
