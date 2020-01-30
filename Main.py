from Fonction.Syracuse import *
import numpy as np

if __name__ == '__main__':
    mySyracuse= Syracuse()
    theTab=mySyracuse.table()
    theTabVol = mySyracuse.tableThroughtFunc(mySyracuse.tempsDeVol, theTab)
    theMatrixVol = np.array(theTabVol)
    print(theMatrixVol)
    #mySyracuse.table()