import os
import numpy as np
from gensim.models import KeyedVectors

def main():
	file = open("sensegrams","w")
	wv=KeyedVectors.load_word2vec_format('glove.6B.300d.txt',binary=False)
	cluster_file="wikipedia_stanford_cluster_a1_N200_n200_labelled"
	lines=open(cluster_file).readlines()
	for line in lines:
		a=line.split("\t")
		if len(a)==4:	
			string,counter,cluster_list,info=line.split("\t")
		if len(a)==3:
			string,counter,cluster_list=line.split("\t")
		string=string.strip()
		counter=int(counter.strip())
		l=cluster_list.split(",")
		word,pos=string.split("#")
		word=word.strip().lower()
		pos=pos.strip().upper()
		lmi_vec_tuple=[]
		print(l)
		print("printing l")
		for i in range(len(l)):
			bim=l[i].strip()
			lmi=extract_lmi(string,bim)
			vec_word=extract_vectors(wv,l[i])
			lmi_vec_tuple.append((vec_word,lmi))
		
		final_list=list(filter(lambda x: x[0] is not None and x[1] is not None , lmi_vec_tuple))
		k=[]
		lmi_list=[]
		for i in final_list:
			k.append(i[0])
			lmi_list.append(i[1])
		print(k)
		print(lmi_list)
		weighted_vector=weighted_sum(k,lmi_list)
		if type(weighted_vector)!=np.ndarray:
			weighted_vector=np.zeros((300))
		file.write(string+"\t"+str(counter)+"\t"+str(list(weighted_vector))+"\n")
		
	file.close() 

def extract_vectors(wv,vec_word):
	vec_word=vec_word[0:-3].strip().lower()
	if vec_word in wv:
		a = wv.get_vector(vec_word)
	else:
		a = None
	return a

			

def weighted_sum(k,lmi):
	print(k,lmi)
	if k!=None and lmi!=None:
		vec=np.array(k)
		lmi=np.array(lmi)
		print(vec.shape)
		print(lmi.shape)
		numerator=np.dot(np.matrix.transpose(lmi),vec)
		denominator=np.sum(lmi)
		if denominator != 0.0:
			weighted_sum_vector=np.divide(numerator,denominator)
			print (weighted_sum_vector)	
			return	weighted_sum_vector
	else:
		return np.zeros((300))

def extract_lmi(jo,bim):
	bim=bim.lower()
	jo=jo.lower()

	
	output_bim_lmi=os.popen("grep -i ^"+bim+".*"+jo+" \"/home/nmn/jobim_naman/my programs/wikipedia_stanford_BIM_LMI_s0.0_w2_f2_wf0_wpfmax1000_wpfmin2_p1000_filtered_g1\"").read()
	output_bim_lmi=output_bim_lmi.split("\n")
	output_bim_lmi=[o.lower() for o in output_bim_lmi if len(o)!=0]
	

	output_lmi=os.popen("grep -i ^"+jo+"."+bim+" \"/home/nmn/jobim_naman/my programs/wikipedia_stanford_LMI_s0.0_w2_f2_wf0_wpfmax1000_wpfmin2_p1000_filtered_g1\"").read()
	output_lmi=output_lmi.split("\n")
	output_lmi=[o.lower() for o in output_lmi if len(o)!=0]
	nset=set()
	for string in output_lmi:
		jo1,bim1_rel,lmi1,no1=[i.strip() for i in string.split("\t")]
		bim1="#".join(bim1_rel.split("#")[:-1])
		print(jo1,bim1,lmi1)
		print(jo,bim)
		if jo1==jo and bim1==bim:
			nset.add((jo1,bim1_rel,lmi1))

	for string in output_bim_lmi:
		bim1_rel,jo1,lmi1,no1=[i.strip() for i in string.split("\t")]
		bim1="#".join(bim1_rel.split("#")[:-1])
		print(jo1,bim1,lmi1)
		print(jo,bim)
		if jo1==jo and bim1==bim:
			nset.add((jo1,bim1_rel,lmi1))
	print("set is printed")
	print(nset)
	lmi = 0.0
	for i in nset:
		lmi=float(i[2])+lmi
		print("added_lmi="+str(lmi))
	if lmi==0.0: return None
	return lmi

	
if __name__ == '__main__':
	main()
