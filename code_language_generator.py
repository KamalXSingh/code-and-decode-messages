'''st=input("")
word=st.split(" ")             #The split() method splits a string into a list
print(word)'''

'''a="kamal"
b="sad"                       #IGNORE
c=a.join(b)
print(c)'''


#HERE STARTS THE PROGRAM

import random as r
rand=('abcdefghijklmnopqrstuvwxyz')

coding= True
if coding:
    text=input("enter the message: ")
    words=text.split(" ")
    nwords=[]
    for word in words:
        if len(word)>=3:
            r1=r.choice(rand)
            r2=r.choice(rand)
            r3=r.choice(rand)
            r4=r.choice(rand)                       
            r5=r.choice(rand)                       
            r6=r.choice(rand)
            
            wordnew= r1+r2+r3 + word[1:]+word[0]+ r4+r5+r6

            nwords.append(wordnew)
        else:
            nwords.append(word[::-1])
    print(' '.join(nwords))        

else:
    text=input("enter the code: ")
    words=text.split(" ")                                           #when decoding a code, make sure to make "coding=False" in line16.
    nwords=[]
    for word in words:
        if len(word)>=3:
            decode=word[3:-3]
            decode=decode[-1] +decode[0:-1]
            nwords.append(decode)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))


