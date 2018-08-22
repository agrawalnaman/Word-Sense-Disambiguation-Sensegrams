# Word-Sense-Disambiguation-Sensegrams
***JOBIM TEXT***

---------------------------------------------------------------------------------
@CONTACT:<br>
NAMAN AGRAWAL:namanagrawal54@gmail.com
		:8390702789<br>
PRIYANKA CORNELIUS:priyankajohn1997@gmail.com
		:8953945345<br>
----------------------------------------------------------------------------------
<br>
DATA REQUIRED:<br>
1]wikipedia_stanford_BIM_LMI_s0.0_w2_f2_wf0_wpfmax1000_wpfmin2_p1000_filtered_g1<br>
2]wikipedia_stanford_LMI_s0.0_w2_f2_wf0_wpfmax1000_wpfmin2_p1000_filtered_g1<br>
3]wikipedia_stanford_cluster_a1_N200_n200_labelled<br>
4]glove.6B.300d.txt<br>

----------------------------------------------------------------------------------

REFERENCES:<br>
1]making sense of word embeddings<br>
2]Unsupervised, Knowledge-Free, and Interpretable
Word Sense Disambiguation<br>
3]API :http://ltbev.informatik.uni-hamburg.de/wsd/single-word<br>
5]www.jobimtext.org<br>
----------------------------------------------------------------------------------

<br>CONTEXT_BASED_FEATURES<br>
PROGRAM (sensegram_generator.py)<br>
--> "sensegram_generator.py" is a python module for generating the sense vectors for all the senses given in the cluster file (wikipedia_stanford_cluster_a1_N200_n200_labelled).<br>
-->Refer paper [making sense of word embeddings ~panchenko@lt.informatik.tu-darmstadt.de] for the theory of "weighted average" of the vectors.<br><br>
----------------------------------------------------------------------------------
PROGRAM (cosine_similarity.py)<br>
--> "cosine_similarity.py" is a python module for calculating cosine similarity of all the context words in the sentence input by the user and predicting the most appropriate sense according to the context .<br><br>
----------------------------------------------------------------------------------
PROGRAM (optimized_lmi.py)<br>
--> "optimized_lmi.py" is a python module for generating a dictionary of unique JO ,BIM ,RELATION and LMI scores from files: 1]wikipedia_stanford_BIM_LMI_s0.0_w2_f2_wf0_wpfmax1000_wpfmin2_p1000_filtered_g1<br>
2]wikipedia_stanford_LMI_s0.0_w2_f2_wf0_wpfmax1000_wpfmin2_p1000_filtered_g1<br><br>
----------------------------------------------------------------------------------

<br>CLUSTER_BASED_FEATURES<br>
PROGRAM(find_word_sense_from_context.py)<br>
-->"find_word_sense_from_context.py" is a python module for finding word sense from the context of the sentence input by the user by the clustering method.<br><br>
-----------------------------------------------------------------------------------
PROGRAM (create-update-cluster.py)<br>
-->"create-update_cluster.py" is a python module for updating a cluster or creating a new entry of sense in the existing cluster file.<br><br>
------------------------------------------------------------------------------------
<br>OTHER PROGRAMS FOLDER<br>
The folder contains some experimental programs which might be usefull for other tasks such as creating a CRUD script for cluster file editing and feedback.<br><br>
------------------------------------------------------------------------------------- 
<br>NOTE:<br>
1]Please check the research papers enclosed in this folder [important concepts have been highlighted].


