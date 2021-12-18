How to run this Automatic Question Generator project :
#Firstly download stanford nlp server using below link
https://stanfordnlp.github.io/CoreNLP/index.html  


After installing unzip the above folder and go to the stanford-corenlp-4.3.2 folder using cd(change the directory) and run the following command :
java -Xmx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 7000


Libraries to Install :
pip install spacy 
pip install en_core_web_sm
pip install pycorenlp==0.3.0
pip install nltk


Project Explanation :
For Indexing - 
Since our project has only one text, we have incremented the index values of the tokenized list to get the indexing. The tokens and indexes are stored in a dictionary.


For Searching - 
We have a searchword which we have to find from the text in the text.txt file. We will parse the indexing list we have done and print the index of the word if it is there.


For Similarity-
We find the sentences that are having the searchword and find cosine similarity between them.


For Ranking -
We find the frequency of the searchword in the sentences it appears and print it. The sentence with higher frequency has a higher rank.


For Evaluation -  
We pass the words and sentences to the check function where we check if all the words passed as parameters are present in the sentence we are checking, if it is present - we append the sentence to the result list.




How core nlp server helps in generating the questions :
we need to start standard core nlp server which is simple web api server, this server has different default properties like output format is json and then the default enabled annotators
Here are the basic Natural Language Processing capabilities (or annotators) that are usually necessary to extract language units from textual data for the sake of search and other applications. 
Sentence breaker - to split text (usually, text paragraphs to sentences)
Tokenize - split the sentences to words
Split - split text into sentences
Pos - parts of speech tagging 
Lemma - lemmatization conversion of word forms into root 
Ner - named entity recognition tagging 
Depparse - dependency parser means finding the relation between the words. 
Coref - Coreference resolution is the task of finding all expressions that refer to the same entity in a text.
Natlog - natural logic annotator, it places an operator annotation and polarity annotation on tokens.
Openie - open information extraction refers to extraction of relation tuples(sub,rel,obj). 
We use spacy which is used to build information extraction or natural language understanding systems, or to pre-process text for deep learning.




For Generation of Questions :
At first we split the text into proper sentences for that we have done some text cleaning. we will generate openie for each sentence. we load spacy and then apply it to the text. we will create a dictionary in which key is token and value is ner. If subjects in openie and keys in dictionary are equal. We create a question by replacing the subject with the question tag and combining it with relation and object and the respective subject will be the answer. Basically the questions will start with When, Who, Where etc ..