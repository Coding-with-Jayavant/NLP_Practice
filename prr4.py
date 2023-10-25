#Assignment no 4
#Name:Jayavant Warkhade
#Roll no:68
#Batch:B4
#Assignment name:1-Gram,2-Gram and 3-Gram using NLTK.

from nltk import ngrams
#for one gram
sentence = """I am Jayavant Warkhade. I possesses a strong skill set as a data scientist, including expertise in statistical analysis, 
machine learning, and data preprocessing. He is proficient in programming languages such as Python and R, with a talent for leveraging 
data visualization tools to convey insights effectively. Jayavant's ability to collaborate in 
cross-functional teams and communicate findings make him a valuable 
contributor with a track record of delivering data-driven solutions."""
arr = ngrams(sentence.split(" "), 1)
print("\n1-grams for given sentence are : ")
for j in arr:
    print(j, end = " ")

#for two gram
d=ngrams(sentence.split(" "),2)
print("\n\n2-grams for given sentence are : ")
for k in d:
    print(k,end=' ')

#for three gram
d=ngrams(sentence.split(" "),3)
print("\n\n3-grams for given sentence are : ")
for k in d:
    print(k,end=' ')

""" OUTPUT->
1-grams for given sentence are : 
('I',) ('am',) ('Jayavant',) ('Warkhade.',) ('I',) ('possesses',) ('a',) ('strong',) ('skill',) ('set',) 
('as',) ('a',) ('data',) ('scientist,',) ('including',) ('expertise',) ('in',) ('statistical',) 
('analysis,',) ('machine',) ('learning,',) ('and',) ('data',) ('preprocessing.',) ('\nHe',) ('is',) 
('proficient',) ('in',) ('programming',) ('languages',) ('such',) ('as',) ('Python',) ('and',) ('R,',) 
('with',) ('a',) ('talent',) ('for',) ('leveraging',) ('data',) ('visualization',) ('tools',) ('to',) 
('convey',) ('insights',) ('effectively.',) ("\nJayavant's",) ('ability',) ('to',) ('collaborate',) 
('in',) ('cross-functional',) ('teams',) ('and',) ('communicate',) ('findings',) ('make',) ('him',) ('a',) ('valuable',) ('contributor',) ('with',) 
('a',) ('track',) ('record',) ('of',) ('delivering',) ('data-driven',) ('solutions.',)

2-grams for given sentence are :
('I', 'am') ('am', 'Jayavant') ('Jayavant', 'Warkhade.') ('Warkhade.', 'I') ('I', 'possesses') 
('possesses', 'a') ('a', 'strong') ('strong', 'skill') ('skill', 'set') ('set', 'as') ('as', 'a') ('a', 'data') ('data', 'scientist,') 
('scientist,', 'including') ('including', 'expertise') ('expertise', 'in') ('in', 'statistical') ('statistical', 'analysis,') 
('analysis,', 'machine') ('machine', 'learning,') ('learning,', 'and') ('and', 'data') ('data', 'preprocessing.') ('preprocessing.', '\nHe') ('\nHe', 'is') 
('is', 'proficient') ('proficient', 'in') ('in', 'programming') ('programming', 'languages') ('languages', 'such') ('such', 'as') ('as', 'Python') ('Python', 'and') 
('and', 'R,') ('R,', 'with') ('with', 'a') ('a', 'talent') ('talent', 'for') ('for', 'leveraging') ('leveraging', 'data') ('data', 'visualization') ('visualization', 'tools') 
('tools', 'to') ('to', 'convey') ('convey', 'insights') ('insights', 'effectively.') ('effectively.', "\nJayavant's") ("\nJayavant's", 'ability') ('ability', 'to') 
('to', 'collaborate') ('collaborate', 'in') ('in', 'cross-functional') ('cross-functional', 'teams') ('teams', 'and') ('and', 'communicate') ('communicate', 'findings') 
('findings', 'make') ('make', 'him') ('him', 'a') ('a', 'valuable') ('valuable', 'contributor') ('contributor', 'with') ('with', 'a') ('a', 'track') ('track', 'record') ('record', 'of') 
('of', 'delivering') ('delivering', 'data-driven') ('data-driven', 'solutions.')

3-grams for given sentence are :
('I', 'am', 'Jayavant') ('am', 'Jayavant', 'Warkhade.') ('Jayavant', 'Warkhade.', 'I') ('Warkhade.', 'I', 'possesses') 
('I', 'possesses', 'a') ('possesses', 'a', 'strong') ('a', 'strong', 'skill') ('strong', 'skill', 'set') ('skill', 'set', 'as') ('set', 'as', 'a') 
('as', 'a', 'data') ('a', 'data', 'scientist,') ('data', 'scientist,', 'including') ('scientist,', 'including', 'expertise') ('including', 'expertise', 'in') 
('expertise', 'in', 'statistical') ('in', 'statistical', 'analysis,') ('statistical', 'analysis,', 'machine') ('analysis,', 'machine', 'learning,') 
('machine', 'learning,', 'and') ('learning,', 'and', 'data') ('and', 'data', 'preprocessing.') ('data', 'preprocessing.', '\nHe') ('preprocessing.', '\nHe', 'is') 
('\nHe', 'is', 'proficient') ('is', 'proficient', 'in') ('proficient', 'in', 'programming') ('in', 'programming', 'languages') ('programming', 'languages', 'such') 
('languages', 'such', 'as') ('such', 'as', 'Python') ('as', 'Python', 'and') ('Python', 'and', 'R,') ('and', 'R,', 'with') ('R,', 'with', 'a') ('with', 'a', 'talent') 
('a', 'talent', 'for') ('talent', 'for', 'leveraging') ('for', 'leveraging', 'data') ('leveraging', 'data', 'visualization') ('data', 'visualization', 'tools') 
('visualization', 'tools', 'to') ('tools', 'to', 'convey') ('to', 'convey', 'insights') ('convey', 'insights', 'effectively.') ('insights', 'effectively.', "\nJayavant's") 
('effectively.', "\nJayavant's", 'ability') ("\nJayavant's", 'ability', 'to') ('ability', 'to', 'collaborate') ('to', 'collaborate', 'in') ('collaborate', 'in', 'cross-functional') 
('in', 'cross-functional', 'teams') ('cross-functional', 'teams', 'and') ('teams', 'and', 'communicate') ('and', 'communicate', 'findings') ('communicate', 'findings', 'make') 
('findings', 'make', 'him') ('make', 'him', 'a') ('him', 'a', 'valuable') ('a', 'valuable', 'contributor') ('valuable', 'contributor', 'with') ('contributor', 'with', 'a') 
('with', 'a', 'track') ('a', 'track', 'record') ('track', 'record', 'of') ('record', 'of', 'delivering') ('of', 'delivering', 'data-driven') ('delivering', 'data-driven', 'solutions.')
"""

############3-------------------------------using text file input
file = open(r"D:\NLP\NLP_Labb\sample_pr4.txt")
sentence=file.readline()
d=ngrams(sentence.split(" "),1)
print("\n\n 1-grams for given sentence are(txt) : ")
for k in d:
    print(k,end=' ')

#for two gram
d=ngrams(sentence.split(" "),2)
print("\n\n2-grams for given sentence are(txt) : ")
for k in d:
    print(k,end=' ')

#for three gram
d=ngrams(sentence.split(" "),3)
print("\n\n3-grams for given sentence are(txt) : ")
for k in d:
    print(k,end=' ')

""" OUPUT->
1-grams for given sentence are(txt) :
('Jayavant',) ('Warkhade',) ('is',) ('an',) ('experienced',) ('data',) ('scientist',) ('with',) ('a',) 
('strong',) ('background',) ('in',) ('statistical',) ('analysis',) ('and',) ('machine',) ('learning.',) 
('\n',)

2-grams for given sentence are(txt) :
('Jayavant', 'Warkhade') ('Warkhade', 'is') ('is', 'an') ('an', 'experienced') ('experienced', 'data') 
('data', 'scientist') ('scientist', 'with') ('with', 'a') ('a', 'strong') ('strong', 'background') 
('background', 'in') ('in', 'statistical') ('statistical', 'analysis') ('analysis', 'and') 
('and', 'machine') ('machine', 'learning.') ('learning.', '\n')

3-grams for given sentence are(txt) :
('Jayavant', 'Warkhade', 'is') ('Warkhade', 'is', 'an') ('is', 'an', 'experienced') ('an', 'experienced', 'data')
 ('experienced', 'data', 'scientist') ('data', 'scientist', 'with') ('scientist', 'with', 'a') 
 ('with', 'a', 'strong') ('a', 'strong', 'background') ('strong', 'background', 'in') ('background', 'in', 'statistical')
   ('in', 'statistical', 'analysis') ('statistical', 'analysis', 'and') ('analysis', 'and', 'machine') 
   ('and', 'machine', 'learning.') ('machine', 'learning.', '\n')
"""