import requests
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import json
import spacy
from spacy import displacy
import en_core_web_sm
from pycorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP('http://127.0.0.1:7000')
Nlp = en_core_web_sm.load()

def get_featured_sents(output1):
    sents = []
    openies=[]
  
    #print("********************* OUTPUT1 **********************")
    #print(output1)
    corenlp_output= json.loads(output1) #.encode('utf-8')
    for sentence in corenlp_output['sentences']:
        #print(sentence)
        sent_start_ind = sentence['index']
        sent = []
        print("\n");
        if(len(sentence['openie'])>0):
           #print(sentence['openie'])
           openies.append(sentence['openie'])
        for token in sentence['tokens']:
            token_start_ind = token['index']
            word = token['originalText']
            lower_word = word.lower()
            if (word[0] == word[0].upper() and word[0] != word[0].lower()):
                case_tag = 'UP'
            else:
                case_tag = 'LOW'
            ner_tag = token['ner']
            pos_tag = token['pos']
            sent.append(({'token': lower_word, 'ner': ner_tag, 'case_tag': case_tag, 'pos_tag': pos_tag,}))
        sents.append(sent)
    #print(sent)
    return openies
def generation(text):
    output= nlp.annotate(text, properties={
        'annotators': 'tokenize,ssplit,pos,ner,openie',
        'outputFormat': 'json'})
    
 
    openies=get_featured_sents(output)
    #print("*******************************Openies******************************")
    #print(openies)
    return openies
def main():
    dict1={}
    
    open('n.txt', 'w').close()
    filehandle = open("text.txt", 'r')
    textinput = filehandle.read()
    indexingtext = textinput
    
    targets = ['Dr.', 'i.e.', 'etc.','0.0','0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1.0','1.1','1.2','1.3','1.4','1.5','1.6','1.7','1.8','1.9','2.0','2.1','2.2','2.3','2.4','2.5','2.6','2.7','2.8','2.9','3.0','3.1','3.2','3.3','3.4','3.5','3.6','3.7','3.8','3.9',
               '4.0','4.1','4.2','4.3','4.4','4.5','4.6','4.7','4.8','4.9','5.0','5.1','5.2','5.3','5.4','5.5','5.6','5.7','5.8','5.9','6.0','6.1','6.2','6.3','6.4','6.5','6.6','6.7','6.8','6.9',
               '7.0','7.1','7.2','7.3','7.4','7.5','7.6','7.7','7.8','7.9','8.0','8.1','8.2','8.3','8.4','8.5','8.6','8.7','8.8','8.9','9.0','9.1','9.2','9.3','9.4','9.5','9.6','9.7','9.8','9.9','A.','B.','C.','D.',
               'E.','F.','G.','H.','I.','J.','K.','L.','M.','N.','O.','P.','Q.','R.','S.','T.','U.','V.','W.','X.','Y.','Z.']
    replacements = [t.replace('.', 'XYZ') for t in targets]
    for i in range(len(targets)):
         textinput = textinput.replace(targets[i], replacements[i])
    output = textinput.split('.')
    sentencetokens = output
    output.pop()
    print(output)
    for o in output:
     output = o.replace('XYZ', '.') 
     
     with open('n.txt', 'a') as the_file:
         the_file.write(output)
         the_file.write('.')
         the_file.write('\n')
    the_file.close()
    
    filehandle.close()
    
    file1 = open("n.txt", 'r')
    text = file1.read()
    print(text)
    
    print('-----------INPUT END---------------')
    openies=generation(text)
    doc = Nlp(text)
    print("************************* doc **************************")
    print(doc.ents)
    for x in doc.ents:
        dict1[x.text]=x.label_
    print("\n")
    print("************************** dict *************************")
    print(dict1)


    print("\n")
    print("************Indexing************")
    text1 = indexingtext.replace(","," ")
    text2 = text1.replace("."," ")
    text3 = text2.replace("?"," ")
    text4 = text3.replace("/"," ")
    text5 = text4.replace("!"," ")
    text6 = text5.replace("@"," ")
    text7 = text6.replace("#"," ")
    text8 = text7.replace("$"," ")
    text9 = text8.replace("%"," ")
    text10 = text9.replace("^"," ")
    text11 = text10.replace("&"," ")
    text12 = text11.replace("*"," ")
    text13 = text12.replace("("," ")
    text14 = text13.replace(")"," ")
    text15 = text14.replace("_"," ")
    text16 = text15.replace("{"," ")
    text17 = text16.replace("}"," ")
    text18 = text17.replace("+"," ")
    text19 = text18.replace("\\"," ")
    text20 = text19.replace("|"," ")
    text21 = text20.replace("["," ")
    text22 = text21.replace("]"," ")
    text23 = text22.replace(";"," ")
    text24 = text23.replace(":"," ")
    text25 = text24.replace("<"," ")
    text26 = text25.replace(">"," ")
    text27 = text26.replace("~"," ")
    text28 = text27.lower()
    data = text28.split()
    dictdata = {}
    for term in data :
        dictdata[term] = data.index(term) + 1; 
    print(dictdata)

    similaritysentences = []


    print("\n")
    print("************** Searching *************")
    searchword = "join" #input("Enter your search word : ") 
    for term in data :
        if term == searchword :
            print("search word has found") 
            print("position of searchword = " + str(dictdata[term])) 
    
    print("\n")
    print("************** Ranking *************")
    #print(sentencetokens)
    for sentence1 in sentencetokens :
        sent1 = sentence1.split()
        for word in sent1 :
            if word == searchword :
                similaritysentences += [sentence1]
    print(similaritysentences)

    if len(similaritysentences) >= 2 :
        ss1_list = similaritysentences[0].split() 
        ss2_list = similaritysentences[1].split()
    
        # sw contains the list of stopwords
        sw = ['anything', 'upon', 'whereafter', 'they', 'between', '’s', 'are', 'nothing', 'six', 'first', 'into', 'top', 'hereupon', 'themselves', 'nowhere', 'well', 'but', 'a', 'if', 'the', 'was', 'amongst', 'whether', 'would', 'serious', 'keep', 'neither', 'who', 'back', 'your', 'now', 'n‘t', 'see', 'only', 'get', 'seems', 'take', 'afterwards', 'next', 'nor', 'own', 'very', 'on', 'each', 'still', "'ll", '’ve', 'every', 'move', 'becoming', 'mostly', 'without', 'somewhere', '‘s', 'eleven', 'two', 'alone', 'both', 'anywhere', 'four', 'n’t', 'meanwhile', 'therefore', "'s", 'although', 'to', 'others', 'above', 'make', 'various', 'many', 'one', 'he', '’d', 'anyhow', 'not', 'before', 'another', 'whither', 'three', 'else', 'something', 'latterly', 'already', 'being', 'eight', 'thence', 'here', 'what', 'other', 'fifty', '’m', 'out', 'therein', 'because', '‘re', 'beside', 'whereas', 'around', 'bottom', 'more', 'could', 'whence', 'hereafter', 'since', 'twenty', '‘d', 'per', 'seem', 'seeming', 'all', 'in', 'itself', 'behind', 'thereafter', 'none', 'less', 'again', 'though', 'i', 'rather', 'somehow', 'always', 'my', 'at', 'made', 'besides', 'unless', 'former', 'towards', 'when', 'during', 'perhaps', 'over', 'until', 'everyone', 'using', 'which', 'twelve', '’re', 'herself', 'ever', 'regarding', 'down', 'amount', 'be', 'through', 'whereby', 'show', 'from', 'whoever', 'under', 'formerly', 'where', 'his', 'can', 'himself', 'last', 'how', 'or', 'ten', 'is', 'have', 'its', "'re", 'some', 'no', 'same', 'sometimes', 'their', 'too', 'nobody', 'than', 'thru', 'were', 'give', 'indeed', 'thereby', 'fifteen', 'for', 'has', 'with', 'except', 'us', '‘m', 'onto', 'whole', 'whatever', 'toward', 'latter', 'used', 'enough', 'elsewhere', 'almost', 'whereupon', 'yet', 'moreover', 'via', 'namely', 'these', 'myself', 'why', 'everything', 'it', 'may', 'five', "'m", 'cannot', 'do', 'so', 'me', 'them', 'whom', 'further', 'our', 'those', 'ourselves', 'nevertheless', 'become', '‘ll', 'everywhere', 'empty', 'say', "'ve", 'hers', 'ca', 'wherever', 're', 'we', 'once', 'sixty', '’ll', 'really', 'yours', 'whenever', 'hence', 'should', 'even', 'third', 'call', 'such', 'across', 'of', 'quite', 'as', 'least', "'d", 'also', 'and', 'thereupon', 'ours', 'much', 'yourself', 'few', 'beforehand', 'hundred', 'among', 'done', 'up', 'does', 'you', 'anyway', 'often', 'name', 'there', 'together', 'forty', 'off', 'might', 'seemed', 'became', 'never', 'below', 'wherein', 'noone', 'beyond', 'mine', 'part', 'must', 'by', 'several', 'throughout', 'then', 'been', 'am', 'him', 'however', 'this', 'due', 'any', 'becomes', 'just', 'whose', 'please', 'full', 'side', 'will', 'most', 'an', 'along', 'doing', 'front', 'while', 'after', 'that', 'anyone', 'put', "n't", 'sometime', 'about', 'her', 'within', 'nine', 'go', 'she', 'hereby', 'did', 'against', 'herein', 'either', 'someone', '‘ve', 'yourselves', 'had', 'otherwise', 'thus']
        l1 =[];l2 =[]
        
        # remove stop words from the string
        ss1_set = {w for w in ss1_list if not w in sw} 
        ss2_set = {w for w in ss2_list if not w in sw}
        
        # form a set containing keywords of both strings 
        rvector = ss1_set.union(ss2_set) 
        for w in rvector:
            if w in ss1_set: l1.append(1) # create a vector
            else: l1.append(0)
            if w in ss2_set: l2.append(1)
            else: l2.append(0)
        c = 0
        
        # cosine formula 
        for i in range(len(rvector)):
                c+= l1[i]*l2[i]
        cosine = c / float((sum(l1)*sum(l2))**0.5)
        print("similarity: ", cosine)
        print("\n")
    simsenfreq={} #Similarity sentence frquency
    for sentence1 in sentencetokens :
        sent1 = sentence1.split()
        for word in sent1 :
            if word == searchword :
                if sentence1 not in simsenfreq.keys() :
                    simsenfreq[sentence1] = 1
                else :
                    simsenfreq[sentence1] += 1 
    print("********* Raw frequencies of search word in sentences*****************")
    print(simsenfreq)

    
    print("\n")
    print("************** Evaluation Part *************")  

    def check(sentence, words):
        res = []
        for substring in sentence:
            k = [ w for w in words if w in substring ]
            if (len(k) == len(words) ):
                res.append(substring)
              
        return res
    sentence = sentencetokens
    words = ['join', 'the Federal Republic']
    print(check(sentence, words))
    
    print("\n")
    print("*********** Questions *********** \n")
    for i in openies:
        j=0 
        for key in dict1:
          #print("------------------------------------------------------------")
          #print(key)
          if i[j]['subject']==key:
              if dict1[key]== 'PERSON':
                  print('who' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )
              elif dict1[key]=='NORP':
                  print('who' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )
              elif dict1[key]=='ORG':
                   print('which' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                   print(i[j]['subject'] )
              elif dict1[key]=='DATE':
                  print('when' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i['subject'] )
              elif dict1[key]=='MONEY':
                  print('how much' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )
              elif dict1[key]=='FAC':
                  print('which' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )
              elif dict1[key]=='GPE':
                  print('where' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )

              elif dict1[key]=='GPE':
                  print('where' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )
              elif dict1[key]=='LOC':
                  print('where' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )

              elif dict1[key]=='PRODUCT':
                  print('where' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )
              elif dict1[key]=='EVENT':
                  print('what' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )
              
              elif dict1[key]=='WORK_OF_ART':
                  print('which' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )
              elif dict1[key]=='LANGUAGE':
                  print('which language' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )
                
              elif dict1[key]=='TIME':
                  print('at what time' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )
              elif dict1[key]=='PERCENT':
                  print('How much percent' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )
              elif dict1[key]=='QUANTITY':
                  print('How much ' + ' '+i[j]['relation']+ ' '+i[j]['object']+'?')
                  print(i[j]['subject'] )
        j=j+1;  

if __name__ == "__main__":
    main()