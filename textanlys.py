#this programme is a statistical analysis of vowels in a word document

vowelcount=0
lettercount=0
vowels=("a","e","i","o","u","y")

document=open("C:\Users\Brax\Documents\sample.txt","r+")

doc1=list(document.read())

for letter in doc1:
    lettercount+=1
    if letter in vowels:
        vowelcount+=1
        doc1[lettercount-1]="x"

print(lettercount)
print(vowelcount)

doc2="".join(doc1)
print(doc2)

document.close()

documentwrite=open("C:\Users\Brax\Documents\sample1.txt", "w")

documentwrite.write(doc2)
documentwrite.close()
