import pickle
def write():
    f= open("binaryfile.dat", "wb")
    list=["Covishield", "Covaxin", "Sputnik", "ZyCoV-D"]
    pickle.dump(list, f)
    f.close()
write()
