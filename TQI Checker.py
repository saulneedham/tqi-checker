from termcolor import colored as coloured #up the uk

Tcharacters=[]
Qcharacters=[]
Icharacters=[]
synonyms=[]
techniques=[]

file = open('inference_synonyms.txt')
lines = file.readlines()
for i in lines:
    i=i.replace('\n','')
    synonyms.append(i)
file = open('techniques.txt')
lines = file.readlines()
for i in lines:
    i=i.replace('\n','')
    techniques.append(i)
text=input('Welcome to TQI Checker! Please enter your text below:' + '\n')
print ('---------------------------------------------------------------')

#Quotes
def qCheck(qStart,qEnd):
    quote=False
    i=0
    while i!=len(text):
        if quote==True:
            if text[i]!=qEnd:
                Qcharacters.append(i)
            else:
                quote=False
                Qcharacters.append(i)
        elif text[i]==qStart:
            Qcharacters.append(i)
            quote=True
        i=i+1
qCheck('“','”')
if len(Qcharacters)==0:
    qCheck('"','"')
if len(Qcharacters)==0:
    qCheck('‘','’')
if len(Qcharacters)==0:
    qCheck("'","'")

#Inference
for n in range(len(synonyms)):
    i=0
    while i!=len(text):
        synonymLen=len(synonyms[n])
        if text[i:i+synonymLen]==synonyms[n] and text[i+synonymLen]==' ':
            i=i+synonymLen
            while text[i]!='.':
                if i not in Qcharacters:
                    Icharacters.append(i)
                i=i+1
        else:
            i=i+1
Icharacters.sort()

#Techniques
for n in range(len(techniques)):
    i=0
    while i!=len(text):
        techniqueLen=len(techniques[n])
        if text[i:i+techniqueLen].lower()==techniques[n] and text[i+techniqueLen]!='d':
            originalI=i
            while i!=originalI+techniqueLen and (i not in Qcharacters or Icharacters):
                Tcharacters.append(i)
                i=i+1
        i=i+1
Tcharacters.sort()
#
print(coloured('Techniques', 'red'))
print(coloured('Quotes', 'green'))
print(coloured('Inference', 'blue'))
print('---------------------------------------------------------------')
for i in range(len(text)):
    if i in Tcharacters:
        letter=(coloured(text[i], 'red'))
    elif i in Qcharacters:
        letter=(coloured(text[i], 'green'))
    elif i in Icharacters:
        letter=(coloured(text[i], 'blue'))
    else:
        letter=(text[i])
    print(letter,end='')