#Assignment no 2
#Name:Jayavant Warkhade
#Roll no:68
#Batch:B4
#Assignment name:Bag of word and TF-IDF in NLP using Gensim Library
from gensim.utils import simple_preprocess
from gensim import corpora

#text2 = open('sample_text.txt', encoding ='utf-8')
text2 = """Hii I am Jayavant Warkhade i'm future data scientist.
if you have any query please feel free to reach me."""
tokens2 =[]
for line in text2.split('.'):
  tokens2.append(simple_preprocess(line, deacc = True))
g_dict2 = corpora.Dictionary(tokens2)

print("The dictionary has: " +str(len(g_dict2)) + " tokens\n")
print(g_dict2.token2id)

g_dict2.add_documents(tokens2)

print("The dictionary has: " +str(len(g_dict2)) + " tokens\n")
print(g_dict2.token2id)
g_dict2.add_documents(tokens2)

print("The dictionary has: " +str(len(g_dict2)) + " tokens\n")
print(g_dict2.token2id)

g_bow =[g_dict2.doc2bow(token, allow_update = True) for token in tokens2]
print("Bag of Words : ", g_bow)
"""
#output->
The dictionary has: 18 tokens
{'am': 0, 'data': 1, 'future': 2, 'hii': 3, 'jayavant': 4, 'scientist': 5, 'warkhade': 6, 'any': 7, 'feel': 8, 'free': 9, 'have': 10, 'if': 11, 'me': 12, 'please': 13, 'query': 14, 'reach': 15, 'to': 16, 'you': 17}        
The dictionary has: 18 tokens
{'am': 0, 'data': 1, 'future': 2, 'hii': 3, 'jayavant': 4, 'scientist': 5, 'warkhade': 6, 'any': 7, 'feel': 8, 'free': 9, 'have': 10, 'if': 11, 'me': 12, 'please': 13, 'query': 14, 'reach': 15, 'to': 16, 'you': 17}        
The dictionary has: 18 tokens
{'am': 0, 'data': 1, 'future': 2, 'hii': 3, 'jayavant': 4, 'scientist': 5, 'warkhade': 6, 'any': 7, 'feel': 8, 'free': 9, 'have': 10, 'if': 11, 'me': 12, 'please': 13, 'query': 14, 'reach': 15, 'to': 16, 'you': 17}        

Bag of Words :  [[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1)], [(7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1), (14, 1), (15, 1), (16, 1), (17, 1)], []]
"""

#-------------------------------------------------------
#Assignment name: TF-IDF in NLP using Gensim Library
from gensim import corpora, models
from gensim.utils import simple_preprocess
import numpy as np

doc_list = [
   "Hii I am Jayavant Warkhade", "How do you do?", 
   "if you have any query please feel free to reach me."
]
doc_tokenized = [simple_preprocess(doc) for doc in doc_list]
dictionary = corpora.Dictionary(doc_tokenized)
BoW_corpus = [dictionary.doc2bow(doc, allow_update=True) for doc in doc_tokenized]

for doc in BoW_corpus:
   print([[dictionary[id], freq] for id, freq in doc])
tfidf = models.TfidfModel(BoW_corpus, smartirs='ntc')

print("\nTF-IDF VECTOR ->")
for doc in tfidf[BoW_corpus]:
   print([[dictionary[id], np.around(freq, decimals=2)] for id, freq in doc])
"""
#output->
[['am', 1], ['hii', 1], ['jayavant', 1], ['warkhade', 1]]
[['do', 2], ['how', 1], ['you', 1]]
[['you', 1], ['any', 1], ['feel', 1], ['free', 1], ['have', 1], ['if', 1], ['me', 1], ['please', 1], ['query', 1], ['reach', 1], ['to', 1]]
[['am', 0.5], ['hii', 0.5], ['jayavant', 0.5], ['warkhade', 0.5]]
[['do', 0.87], ['how', 0.44], ['you', 0.22]]
[['you', 0.16], ['any', 0.31], ['feel', 0.31], ['free', 0.31], 
['have', 0.31], ['if', 0.31], ['me', 0.31], ['please', 0.31], ['query', 0.31], ['reach', 0.31], ['to', 0.31]]
"""