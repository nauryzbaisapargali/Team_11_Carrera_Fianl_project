import gensim
from gensim.summarization import summarize
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
import RAKE,operator
from rake_nltk import Rake

text = '''The philosophy of enlightenment
There is no doubt that philosophy according to period of time, problems that bother society has several stages of development.
Starting from ancient Greek and pre-Socratic philosophy, throw Renaissance until modern philosophy. In this topic I am going 
to talk about most influential from the point of science period of philosophy - philosophy of enlightenment. 18th century was 
period of time when great scientific discoveries took place. And that’s exact period of time when people start to think about 
things that happening around from rational point of view. Enlightenment was the time when people took ideas and methods of 
scientific discoveries to figure out how things actually work without basic presumptions through  new lens of reason. 
So the main question enlightenment is aimed to answer was why are things way they are? So that’s why a lot of philosophers 
of this period also called thinkers. And by answering this question they tried to find solution of mankind problems relying 
on rationalism. Such as to try minimize human suffering, and make world as good as possibly could. There are many main issues 
that enlightenment addresses: political representation, human rights, ideals of how to find a ruler and what limits on those 
rulers should be, and more and more ethical and religious issues. 
'''
stop_words = stopwords.words('english')
stopwrds = []
for element in stop_words:
	stopwrds.append(element.lower())
word_token = word_tokenize(text)
array = []
clean_text = {}
for word in word_token:
	if word.lower() not in stopwrds:
		clean_text[word.lower()]=20
		array.append(word.lower())
new_text = " ".join(array)
a=new_text.replace(',','').replace('.','').replace("'",'')
res = a.split()

r = Rake()

r.extract_keywords_from_text(a)

key_phrases = r.get_ranked_phrases()[0:10]



#print(clean_text)


short_summary = summarize(text1)
print("Short summary of text are: \n",short_summary)
#print("\n")
#print("Key phrases from text are: ",key_phrases)