# Word-Sense-Disambiguation-Sensegrams

This project is a Word Sense Disambiguation system for the Machine Translation system ‘Anusaaraka’, which is being worked upon at the Anusaaraka Lab, LTRC, International institute of information Technology Hyderabad. The concept has been derived from the research paper ‘Making Sense of Word Embeddings’ by Alexander Panchenko et al.
There is a plethora of polysemous words which we use in our everyday life. These words when translated into other languages often generate ambiguity regarding the correct sense of the word used in the sentence. To improve the disambiguation of word senses a novel approach has been used in this project, which incorporates the context in which the words have been used and predicts the correct sense. We trained the Sense Embeddings (Sensegrams) from Wikipedia clusters for our system. The system takes the weighted average of the context words and then calculates the cosine similarity between the Sense Embeddings and the context-based Embeddings and then predicts the correct sense with highest cosine similarity. Further work is being done to improve the ability of the system to predict correct sense and to incorporate this with “Anusaaraka” Machine translation system at International institute of information Technology Hyderabad.

----------------------------------------------------------------------------------
### DATA REQUIRED
```
1]wikipedia_stanford_BIM_LMI_s0.0_w2_f2_wf0_wpfmax1000_wpfmin2_p1000_filtered_g1
2]wikipedia_stanford_LMI_s0.0_w2_f2_wf0_wpfmax1000_wpfmin2_p1000_filtered_g1
3]wikipedia_stanford_cluster_a1_N200_n200_labelled
4]glove.6B.300d.txt
```
----------------------------------------------------------------------------------

### REFERENCES:
```
1]making sense of word embeddings
2]Unsupervised, Knowledge-Free, and Interpretable
  Word Sense Disambiguation
3]API :http://ltbev.informatik.uni-hamburg.de/wsd/single-word
5]www.jobimtext.org
```
----------------------------------------------------------------------------------

## CONTEXT_BASED_FEATURES
#### PROGRAM (sensegram_generator.py)
* "sensegram_generator.py" is a python module for generating the sense vectors for all the senses given in the cluster file (wikipedia_stanford_cluster_a1_N200_n200_labelled).
* Refer paper [making sense of word embeddings ~panchenko@lt.informatik.tu-darmstadt.de] for the theory of "weighted average" of the vectors.

----------------------------------------------------------------------------------
#### PROGRAM (cosine_similarity.py)
* "cosine_similarity.py" is a python module for calculating cosine similarity of all the context words in the sentence input by the user and predicting the most appropriate sense according to the context .
----------------------------------------------------------------------------------
#### PROGRAM (optimized_lmi.py)
* "optimized_lmi.py" is a python module for generating a dictionary of unique JO ,BIM ,RELATION and LMI scores from files: 
* 1]wikipedia_stanford_BIM_LMI_s0.0_w2_f2_wf0_wpfmax1000_wpfmin2_p1000_filtered_g1
* 2]wikipedia_stanford_LMI_s0.0_w2_f2_wf0_wpfmax1000_wpfmin2_p1000_filtered_g1
----------------------------------------------------------------------------------

## CLUSTER_BASED_FEATURES
#### PROGRAM(find_word_sense_from_context.py)
* "find_word_sense_from_context.py" is a python module for finding word sense from the context of the sentence input by the user by the clustering method.
-----------------------------------------------------------------------------------
#### PROGRAM (create-update-cluster.py)
* "create-update_cluster.py" is a python module for updating a cluster or creating a new entry of sense in the existing cluster file.
------------------------------------------------------------------------------------
### OTHER PROGRAMS FOLDER
* The folder contains some experimental programs which might be usefull for other tasks such as creating a CRUD script for cluster file editing and feedback.
------------------------------------------------------------------------------------- 
## NOTE:
* 1]Please check the research papers enclosed in this folder [important concepts have been highlighted].
----------------------------------------------------------------------------------------
## Authors:

* NAMAN AGRAWAL:namanagrawal54@gmail.com
* PRIYANKA CORNELIUS:priyankajohn1997@gmail.com
-----------------------------------------------------------------------------------------
## Downloads:
* Sensegrams Trained from 300 dimension vectors (glove).
Email the authors to request the file link.

