import pickle
f=open('vaccines_text.txt', 'r')
f1=open('vaccines.dat', 'wb')
rows=f.readlines()
for row in rows:
    for word in row.split():
        word=word.replace('_', '  ')
    pickle.dump(row,f1)
f.close()
f1.close()
