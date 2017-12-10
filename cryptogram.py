#programme is used to decrpyt "cryptogram puzzles"

import os

os.system('cls')

#list of most frequent letters in the English language: etaoinshrdlcumwfgypbvkjxqz
wordFrequency={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
letterNumber={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
most_frequent_letter=["e","t","a","o","i","n","s","h","r","d","l","c","u","m","w","f","g","y","p","b","v","k","j","x","q","z"]
encrptKey={}

string=raw_input("Please enter the crytogram ")
#string="This is a test"

def evol(strng):
	#strng is the cryptogram
	#programme status: GO
	#this function should return the encrypt key and decoded phrase
	 #this creates an list of the letters in the sentence
	evolutions=[]
	replylist=["yes","y","ye"]
	sentinal=True
	
	cryptKey={} #This is the key where the encryptVale=key and decryptVal=Value
	wordFrequency=wordFreq(strng)
	#print wordFrequency
	#sortLst=sortList(wordFrequency)
	#print sortLst
	newSentence=""
	cryptList=sortList(wordFrequency)
	
	while(sentinal):
	
		os.system('cls')
		print strng
		letterNsentence=letterlist(strng)
		print "Here is the letter frequency of the sentence"
		print wordFrequency
		print "Here is a list of the most frequent letters in the sentence"
		print cryptList
		print "Here are the most common letters"
		print "e,t,a,o,i,n,s,h,r,d,l,c,u,m,w,f,g,y,p,b,v,k,j,x"
		if(len(evolutions)):
			print "Here is the cryptograph key"
			print cryptKey
			#gets letter to replace and validates
		while True:
			letterReplace=raw_input("Please input the letter to replace: ")
			letterReplace=letterReplace.lower()
			if(letterReplace not in wordFrequency):
				continue
			break
			#get letter to substitute and validates
		while True:
			letterSubstitute=raw_input("Please input the letter to be sustituted in: ")
			letterSubstitute=letterSubstitute.lower()
			if(letterReplace not in wordFrequency):
				continue
			break
		
		
		for i,letter in enumerate(letterNsentence):
			if((letter==letterReplace) and (letter.islower()) and (letter not in cryptKey.keys())):
				letterNsentence[i]=letterSubstitute.upper()
			
		print newSentence.join(letterNsentence)
		reply=raw_input("Would you like to keep this iteration? ")
		
		if(reply in replylist):
			strng=newSentence.join(letterNsentence)
			evolutions.append(strng)
			cryptKey[letterReplace]=letterSubstitute
			cryptList.pop(cryptList.index(letterReplace))
			
		elif(reply=="quit"):
			sentinal=False
			
		else:
			continue
				
			
def wordFreq(string):
	#this function creates a dictionary of letter frequency
	for char in string:
	
		if (char.isalpha()):
			keyVal=wordFrequency[char.lower()]
			keyVal=keyVal+1
			wordFrequency[char.lower()]=keyVal
		else:
			continue
		
	return wordFrequency
	
def resetFreq():
	#this resets the frequency dictionary
	global wordFrequency
	keyList=list(wordFrequency.keys())
	for i in keyList:
		wordFrequency[i]=0
	print "Dictionary has now been reset"
	
def sortList(x):
	#x is most frequent letters
	#this creates a sorted list of letter from the dictionary, with the most frequent letters being up front
	freqList=[]
	wkey=x.values()
	wkey.sort(reverse=True)
	while(len(wkey)>0):
		i=0
		it2add=wkey.pop(i)
		for y in x.keys():
			if(x[y]==it2add and x[y]!=0 and y not in freqList):
				freqList+=y
				i+=1
	return freqList
	
def letterlist(x):
	#this function creates a list of letters from the string
        letters=[]
        for i in x:
                letters.append(i)
        return letters



def rplcLttr(lst,l2Ra,Repla):
	#this function replaces letters from the string with the substitued letter
	newStrList=[]
	for i in lst:
		if(i.lower()==l2Ra[0].lower()):
			newStrList.append(Repla[0])
		else:
			newStrList.append(i)
	return newStrList
	



resetFreq()

evol(string)