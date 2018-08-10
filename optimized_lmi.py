from functools import reduce
def main():
	#print("####_CREATING A DICTIONARY_####")
	LMI_file="wikipedia_stanford_LMI_s0.0_w2_f2_wf0_wpfmax1000_wpfmin2_p1000_filtered_g1"
	BIM_LMI_file="wikipedia_stanford_BIM_LMI_s0.0_w2_f2_wf0_wpfmax1000_wpfmin2_p1000_filtered_g1"
	lines=open(LMI_file).readlines()
	lines_BIM=open(BIM_LMI_file).readlines()
	dictionary_lmi={}


	for line in lines:
		jo,bim_rel,value,no=line.split('\t')
		bim="#".join(bim_rel.split("#")[:-1])
		rel=bim_rel.split("#")[-1]
		#print(bim+"\t"+rel)
		if (jo,bim) in dictionary_lmi:
			if (rel,value) in dictionary_lmi[(jo,bim)]:
				continue
			else:
				dictionary_lmi[(jo,bim)].append((rel,value))
		else:
			dictionary_lmi[(jo,bim)]=[(rel,value)]
			
	for line in lines_BIM:
		bim_rel,jo,value,no=line.split('\t')
		bim="#".join(bim_rel.split("#")[:-1])
		rel=bim_rel.split("#")[-1]
		#print(bim+"\t"+rel)
		if (jo,bim) in dictionary_lmi:
			if (rel,value) in dictionary_lmi[(jo,bim)]:
				continue
			else:
				dictionary_lmi[(jo,bim)].append((rel,value))
		else:
			dictionary_lmi[(jo,bim)]=[(rel,value)]

	#print(dictionary_lmi)
	# new_dict={key:reduce(lambda x,y : x+y,[float(i[1]) for i in value]) for key,value in dictionary_lmi.items()}
	for key,value in dictionary_lmi.items():
		total_value=reduce(lambda x,y : x+y,[float(i[1]) for i in value])
		print(key,value,total_value)

	#print(new_dict)
	file=open("lmi_score_added.txt", 'w')
	for (jo,bim) in new_dict:
		file.write(str(jo)+'\t'+str(bim)+'\t'+str(new_dict[jo,bim])+'\n')
	file.close()




if __name__ == '__main__':
	main()
	
	


