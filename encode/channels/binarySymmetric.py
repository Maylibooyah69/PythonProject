#this right here is a binary symmetric channel for texts
#f is the probability P(message!=signal)
#will do image implementation
from random import random as rdm

message="Lolita, light of my life, fire of my loins. My sin, my soul. Lo-lee-ta: the tip of the tongue taking a trip of three steps down the palate to tap, at three, on the teeth. Lo. Lee. Ta. She was Lo, plain Lo, in the morning, standing four feet ten in one sock. She was Lola in slacks. She was Dolly at school. She was Dolores on the dotted line. But in my arms she was always Lolita. Did she have a precursor? She did, indeed she did. In point of fact, there might have been no Lolita at all had I not loved, one summer, an initial girl-child. In a princedom by the sea. Oh when? About as many years before Lolita was born as my age was that summer. You can always count on a murderer for a fancy prose style. Ladies and gentlemen of the jury, exhibit number one is what the seraphs, the misinformed, simple, noble-winged seraphs, envied. Look at this tangle of thorns."
f=0.1
f_=1-f
#print(f,f_)
#print(rdm())

def str2ascii(s):
    out=[]
    for i in s:
        out.append(ord(i))
    return out

def str2bin(s):
    out=[]
    for i in s:
        asc=ord(i)
        bi=bin(asc)
        out.append(bi)
    return out

def bin2str(s):
    return "".join(chr(int(i,2)) for i in s)

def biST(msg): #this function takes in a list of binary ascii code of strings
    out=[]
    for i in msg:
        if rdm()<f:
            out.append(str(int(0==i)))
        else:
            out.append(str(i))
    return out

def compdiff(og,re): ##returns the noise vector
    out=[]
    for i in zip(og,re):
        if i[0]==i[1]:
            out.append(str(0))
        else:
            out.append(str(1))
    return "".join(out)

##terminal display
print("Chance of flipping a single bit: f="+str(f))
print("Message: \n"+message)
m=str2bin(message)
t=biST(m)
r=bin2str(t)
print("Received message: \n"+r)
print("Binary noise vector: \n"+compdiff(message,r))
