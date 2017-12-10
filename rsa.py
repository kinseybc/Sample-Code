#This programme demonstrates the functionality of the RSA encryption scheme
'''Programme is initialized with the following values:
Max Value: 7*13=91
Priv_key=29
Pub_key=5
'''
asciivalues={'a':97,'b':98,'c':99,'d':100,'e':101,'f':102,'g':103,'h':104,'i':105,'j':106,'k':107,'l':108,'m':109,'n':110,'o':111,'p':112,'q':113,'r':114,'s':115,'t':116,'u':117,'v':118,'w':119,'x':120,'y':121,'z':122,'A':65,'B':66,'C':67,'D':68,'E':69,'F':70,'G':71,'H':72,'I':73,'J':74,'K':75,'L':76,'M':77,'N':78,'O':79,'P':80,'Q':81,'R':82,'S':83,'T':84,'U':85,'V':86,'W':87,'X':88,'Y':89,'Z':90}
priv_key=29
pub_key=5
max_value=91

def encrypt(ascii,pub_key,max_value):
	encrVal=(ascii*ascii)%max_value
	for x in range(0,(pub_key-2)):
		encrVal=(ascii*encrVal)%max_value
		#print encrVal
	return encrVal
	
def decrypt(ascii,p_key,max_value):
	dencrVal=(ascii*ascii)%max_value
	for x in range(0,(p_key-2)):
		dencrVal=(ascii*dencrVal)%max_value
		#print dencrVal
	return dencrVal
	
def main():
	while True:
		print "1)Encrpyt Message"
		print "2)Decrypt message"
		choice=int(raw_input("What would you like to do?"))
		cryptedMsg=[]
		if(choice==1):
			msg=raw_input("Please enter your message to encrypt: ")			
			for letter in msg:
				if(asciivalues.get(letter)):
					encrLetter=encrypt(asciivalues[letter],pub_key,max_value)
					cryptedMsg.append(str(encrLetter))
				else:
					cryptedMsg.append(str(letter))
			break
		
		elif(choice==2):
			msg=raw_input("Please enter your message to decrypt: ")
			break
		else:
			continue
	print "".join(cryptedMsg)

			
#print encrypt(67,pub_key,max_value)
#print decrypt(58,priv_key,max_value)

main()