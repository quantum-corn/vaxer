import pickle
f=open('centers text.txt', 'r')
f1=open('centers text.dat', 'wb')
while True:
    line=f.readline()
    for word in line.split():
        word=word.replace('_', '  ')
        pickle.dump(word,f1)
        pickle('\n',f1)
f.close()      
            
