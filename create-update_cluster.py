import os
def main():
	print("####_CREATING A DICTIONARY_####")
	cluster_file="wikipedia_stanford_cluster_a1_N200_n200_labelled"
	lines=open(cluster_file).readlines()
	global dictionary 
	dictionary= {(line.split('\t')[0].strip(),int(line.split('\t')[1].strip())):line.split('\t')[2].strip().split(',') for line in lines}
	print("####_DICTIONARY CREATED_####")
	while(True):
		word=input("Enter word : ").strip().lower()
		read(word)
		action=input("\n****press 'A' to 'ADD' or 'CHANGE' the sense cluster****\n****press 'B' to 'GO BACK'****\n****'E' to 'EXIT'****\n").lower()
		if action=='a':
			action=input("****press 'U' to 'UPDATE' existing sense cluster****\n****press 'C' to 'CREATE' new sense cluster****\n").lower()
			if action=='u':
				pos=input("Enter POS tag of the word : "+word+"= ").upper()
				index=int(input("Enter index of the cluster where you want to append : ") )
			elif action=='c':
				pos=input("Enter POS tag of the word : "+word+"= ").upper()
				index=0
				while (word+"#"+pos,index) in dictionary:
					index+=1
			attention_word=input("enter the attention word you want to append: ").strip().lower()
			attention_pos=input("enter pos tag of attention word: ").strip().upper()
			attention_str=attention_word+"#"+attention_pos
			dictionary.setdefault((word+"#"+pos,index),[]).append(attention_str)
			print("***************************************************")
			print("Changes have been incorporated in the dictionary.")
			print("***************************************************")
			read(word,pos)
			print("##"*15)
		elif action=='b':
			print("##"*15)
			continue
		elif acton=='e':
			exit()
		

		

def read(word="",pos=""):
	word=word if word else input("Enter word: ").strip().lower()
	pos=pos if pos else input("Enter pos-tag or press 'd' for 'DEFAULT':").strip().upper()
	pos=['NN','JJ','NP','VB','RB','CD'] if pos=='D' else [pos]
	for p in pos:
		counter=0
		string=word+"#"+p
		while (string,counter) in dictionary:
			print(string+'\t'+str(counter)+'\t'+str(dictionary[(string,counter)])+'\n')
			counter=counter+1







if __name__ == '__main__':
	main()
