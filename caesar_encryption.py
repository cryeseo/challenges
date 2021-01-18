word = input("What is your word?")

lowered = str(word.lower())
    
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

encryption = []

for i in range(len(lowered)):
    for c in range(len(alphabet)):
        if lowered[i] == alphabet[c]:
            encryption += alphabet[c+3]

def listToString(lst):  
     string = ""  
     for l in lst:  
            string += l   
    
     return string

print(listToString(encryption))        
