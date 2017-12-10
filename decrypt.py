#print this is a test programme for a roll over text encryptio
print "This programme decrypts a cryptogram using a shift key"
import os

letterNumber={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

def decrypt(string,letter_shift):
	newString=""
	newList=[]
	for i in string:
		if(i.lower() in letterNumber.keys()):
			cryptLetter=newLetter(i.lower(),letter_shift)
			newList.append(cryptLetter)
		else:
			newList.append(i)
			
	return newString.join(newList)
			
			
def openFile(fileName):
	f=open(fileName,'r')
	return f.read()
			
def newLetter(letter,shift):
	originalNumber=letterNumber[letter]
	newNumber=originalNumber+shift
	if(newNumber > 26):
		delta=newNumber-26
		for i in letterNumber:
			if(letterNumber[i]==delta):
				return i
	else:
		for i in letterNumber:
			if( letterNumber[i]==newNumber):
				return i
				
def main():
	while True:
		newText=""
		dataSrc=raw_input("Would you like to read text from a file? ")
		if(dataSrc=='y'):
		
			fileNm=raw_input("Please enter the file name: ")
			
			text=openFile(fileNm)
		
		else:
			text=raw_input("Please enter the text you wish to decrypt: ")
			
		try:
			autman=raw_input("Would  you like to manually input the shift value: ")
			if(autman=='y'):
				keyShift=int(raw_input("Please enter the cryptoKey, only intiger: "))
				newText=decrypt(text,keyShift)
				print newText
				
			else:
				shift=1
				while(shift<27):
					newText=decrypt(text,shift)
					print newText
					choice1=raw_input("Would you like to keep this decoded sentence? ")
					if(choice1=='y'):
						break
					else:
						os.system('cls')
						shift+=1
						continue
			
			choice=raw_input("Would you like to decode another sentence? (y) ")
			if(choice=="y"):
				continue
			else:
				print "The programme will now exit: "
				break
					
		except ValueError:
			print "You entered an incorrect Value, Fool!!!"
		
main()
		
			