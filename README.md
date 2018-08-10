# Word-Sense-Disambiguation-Sensegrams-
***JOBIM TEXT***

---------------------------------------------------------------------------------
@CONTACT-
NAMAN AGRAWAL	:namanagrawal54@gmail.com
		:8390702789
PRIYANKA CORNELIUS:priyankajohn1997@gmail.com
		:8953945345
----------------------------------------------------------------------------------

DATA REQUIRED:
1]wikipedia_stanford_BIM_LMI_s0.0_w2_f2_wf0_wpfmax1000_wpfmin2_p1000_filtered_g1
2]wikipedia_stanford_LMI_s0.0_w2_f2_wf0_wpfmax1000_wpfmin2_p1000_filtered_g1
3]wikipedia_stanford_cluster_a1_N200_n200_labelled
4]glove.6B.300d.txt

----------------------------------------------------------------------------------

REFERENCES:
1]making sense of word embeddings
2]Unsupervised, Knowledge-Free, and Interpretable
Word Sense Disambiguation
3]API :http://ltbev.informatik.uni-hamburg.de/wsd/single-word
5]www.jobimtext.org
----------------------------------------------------------------------------------


##################################################################################
#				CONTEXT_BASED_FEATURES				 #
##################################################################################
PROGRAM (sensegram_generator.py)
--> "sensegram_generator.py" is a python module for generating the sense vectors for all the senses given in the cluster file (wikipedia_stanford_cluster_a1_N200_n200_labelled).
-->Refer paper [making sense of word embeddings ~panchenko@lt.informatik.tu-darmstadt.de] for the theory of "weighted average" of the vectors.
----------------------------------------------------------------------------------
PROGRAM (cosine_similarity.py)
--> "cosine_similarity.py" is a python module for calculating cosine similarity of all the context words in the sentence input by the user and predicting the most appropriate sense according to the context .
----------------------------------------------------------------------------------
PROGRAM (optimized_lmi.py)
--> "optimized_lmi.py" is a python module for generating a dictionary of unique JO ,BIM ,RELATION and LMI scores from files: 1]wikipedia_stanford_BIM_LMI_s0.0_w2_f2_wf0_wpfmax1000_wpfmin2_p1000_filtered_g1
2]wikipedia_stanford_LMI_s0.0_w2_f2_wf0_wpfmax1000_wpfmin2_p1000_filtered_g1
----------------------------------------------------------------------------------


##################################################################################
#				CLUSTER_BASED_FEATURES				 #
##################################################################################
PROGRAM(find_word_sense_from_context.py)
-->"find_word_sense_from_context.py" is a python module for finding word sense from the context of the sentence input by the user by the clustering method.
-----------------------------------------------------------------------------------
PROGRAM (create-update_cluster.py)
-->"create-update_cluster.py" is a python module for updating a cluster or creating a new entry of sense in the existing cluster file.
------------------------------------------------------------------------------------
	[OTHER PROGRAMS FOLDER]
The folder contains some experimental programs which might be usefull for other tasks such as creating a CRUD script for cluster file editing and feedback.
------------------------------------------------------------------------------------- 



-------------------------------------------------------------------------------------
NOTE:
1]Please check the research papers enclosed in this folder [important concepts have been highlighted].
--------------------------------------------------------------------------------------


