from Syracuse import *
import matplotlib.pyplot as plt
import numpy as np

def chooseSetup():
    isMultiple = False
    while True :
        userInput = input("Run for one or multiple sequence ? (o/m) ")
        if(userInput=="o" or userInput=="m"):
            if(userInput=="m"):
                isMultiple = True
            break
    isShowing = False
    while True :
        userInput = input("Show the matrix ? (y/n) ")
        if(userInput=="n" or userInput=="y"):
            if(userInput=="y"):
                isShowing = True
            break

    if(isMultiple):
        print("Number of syracuze-like function run (your input is squared, advice 10)")
        print("That will test every function of the form ax+b with a and b between 0 and and input")
        multipleSize = 0
        while True:
            try:
                multipleSize = int(input("What table size do you want ? "))
            except ValueError:
                print("Please input a integer")
                continue
            else:
                break
        print("Number of values tested for each function (your input is squared, advice 10)")
        valueSize = 0
        while True:
            try:
                valueSize = int(input("What table size do you want ? "))
            except ValueError:
                print("Please input a integer")
                continue
            else:
                break
        isSaveRecap = False
        while True :
            userInput = input("Save recap matrix output ? (y/n) ")
            if(userInput=="y" or userInput=="n"):
                if(userInput=="y"):
                    isSaveRecap = True
                break
        isSaveEvery = False
        while True :
            userInput = input("Save every function matrix output ? (y/n) ")
            if(userInput=="y" or userInput=="n"):
                if(userInput=="y"):
                    isSaveEvery = True
                break
        runForMultiple(multipleSize, valueSize, isSaveRecap, isSaveEvery, isShowing)
    else :
        print("Default values :")
        print("     ax+b where a=3 and b=1")
        print("     output a 10*10 table")
        isDefault = False
        while True :
            userInput = input("Do you want to use default values ? (y/n) ")
            if(userInput=="y" or userInput=="n"):
                if(userInput=="y"):
                    isDefault = True
                break
        a = 3
        b = 1
        size = 10
        if not isDefault:
            while True:
                try:
                    a = int(input("Value for a : "))
                except ValueError:
                    print("Please input a integer")
                    continue
                else:
                    break
            while True:
                try:
                    b = int(input("Value for b : "))
                except ValueError:
                    print("Please input a integer")
                    continue
                else:
                    break
            print("Number of values tested (your input is squared, advice 10)")
            while True:
                try:
                    size = int(input("Value for size : "))
                except ValueError:
                    print("Please input a integer")
                    continue
                else:
                    break
        isSave = False
        while True :
            userInput = input("Save matrix output ? (y/n) ")
            if(userInput=="y" or userInput=="n"):
                if(userInput=="y"):
                    isSave = True
                break
        runForSingle(a, b, size, isSave, isShowing)

def runForMultiple(multipleSize, valueSize, isSaveRecap, isSaveEvery, isShowing):
    print("todo mul")

def runForSingle(a, b, size, isSave, isShowing):
    mySyracuse= Syracuse(a, b)
    theTab=mySyracuse.table(size)
    theTabVol = mySyracuse.tableThroughtFunc(mySyracuse.flyingTime, theTab)
    theMatrixVol = np.array(theTabVol)
    print(theMatrixVol)

    plt.imshow(theMatrixVol)
    if isShowing :
        plt.show()
    if isSave :
        fileName = "img/{0}x+{1}.png".format(a, b)
        plt.savefig(fileName)



if __name__ == '__main__':
    chooseSetup()
