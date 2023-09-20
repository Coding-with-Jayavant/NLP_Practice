#Assignment no 2
#Name:Jayavant Warkhade
#Roll no:68
#Batch:B4
#Assignment name:Bag of word in NLP using Gensim Library

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