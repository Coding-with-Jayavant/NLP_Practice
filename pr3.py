#Assignment no 3
#Name:Jayavant Warkhade
#Roll no:68
#Batch:B4
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