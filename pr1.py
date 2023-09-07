#Assignment no 1
#Name:Jayavant Warkhade
#Roll no:68
#Batch:B4
#Assignment name:Text processing using sentence detection,stop word removal,lemmitization,pos tagging

#sentence detection
import spacy
nlp = spacy.load("en_core_web_sm") 
about_text = (
    """Hello, i am Jayavant Warkhade 
I am a data scientist with a strong background in statistics, machine learning, and data analysis. 
My expertise lies in extracting valuable insights from complex datasets and using them to drive informed decision-making. 
I have experience in a wide range of industries, including healthcare, finance, and e-commerce, 
and have successfully developed and implemented predictive models, recommendation systems, and data-driven strategies. """
)
about_doc = nlp(about_text)
sentences = list(about_doc.sents)
len(sentences)

for sentence in sentences:
    print(f"{sentence[:5]}...")

#output:    
# Hello, i am Jayavant...
# My expertise lies in extracting...
# I have experience in a...


#tokenization
import spacy
nlp = spacy.load("en_core_web_sm")
about_text = (
    "I am a data scientist with a strong background in statistics, machine learning, and data analysis. "
)
about_doc = nlp(about_text)

for token in about_doc:
    print (token, token.idx)
#output:
# I 0
# am 2
# a 5
# data 7
# scientist 12
# with 22
# a 27
# strong 29
# background 36
# in 47
# statistics 50
# , 60
# machine 62
# learning 70
# , 78
# and 80
# data 84
# analysis 89
# . 97


#Lemmatization
#import spacy
import spacy
#load nlp
nlp = spacy.load("en_core_web_sm")
conference_help_text = (
    "Paragraphs are medium-sized units of writing"
    "longer than sentences, but shorter than sections, chapters, or entire works."

)
#lemmatization
conference_help_doc = nlp(conference_help_text)
for token in conference_help_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")

#Output:
# Paragraphs : paragraph
#                  are : be
#                units : unit
#            sentences : sentence
#              shorter : short
#             sections : section
#             chapters : chapter
#                works : work

#PartOfspeech pos tagging
import spacy
nlp = spacy.load("en_core_web_sm")
about_text = (
     "paragraph structure is essential to any writing for organization, flow, and comprehension"
 )
about_doc = nlp(about_text)
for token in about_doc:
     print(
         f"""
 TOKEN: {str(token)}
 
 TAG: {str(token.tag_):10} POS: {token.pos_}
 EXPLANATION: {spacy.explain(token.tag_)}"""
    )
     
#Output:

#  TOKEN: paragraph

#  TAG: NN         POS: NOUN
#  EXPLANATION: noun, singular or mass

#  TOKEN: structure

#  TAG: NN         POS: NOUN
#  EXPLANATION: noun, singular or mass

#  TOKEN: is

#  TAG: VBZ        POS: AUX
#  EXPLANATION: verb, 3rd person singular present

#  TOKEN: essential

#  TAG: JJ         POS: ADJ
#  EXPLANATION: adjective (English), other noun-modifier (Chinese)

#  TOKEN: to

#  TAG: IN         POS: ADP
#  EXPLANATION: conjunction, subordinating or preposition

#  TOKEN: any

#  TAG: DT         POS: DET
#  EXPLANATION: determiner

#  TOKEN: writing

#  TAG: NN         POS: NOUN
#  EXPLANATION: noun, singular or mass

#  TOKEN: for

#  TAG: IN         POS: ADP
#  EXPLANATION: conjunction, subordinating or preposition

#  TOKEN: organization

#  TAG: NN         POS: NOUN
#  EXPLANATION: noun, singular or mass

#  TOKEN: ,

#  TAG: ,          POS: PUNCT
#  EXPLANATION: punctuation mark, comma

#  TOKEN: flow

#  TAG: NN         POS: NOUN
#  EXPLANATION: noun, singular or mass

#  TOKEN: ,

#  TAG: ,          POS: PUNCT
#  EXPLANATION: punctuation mark, comma

#  TOKEN: and

#  TAG: CC         POS: CCONJ
#  EXPLANATION: conjunction, coordinating

#  TOKEN: comprehension

#  TAG: NN         POS: NOUN
#  EXPLANATION: noun, singular or mass