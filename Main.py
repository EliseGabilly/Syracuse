from numpy.lib.function_base import average
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
    theTab=mySyracuse.syracuseTable(size)

    if isSave or isShowing :
        name = "{0}x+{1}_{2}".format(a, b, size)
        #create figure
        fig = plt.figure()
        plt.suptitle(name)

        #fig 1 - flying time
        theTabVol = mySyracuse.tableThroughtFunc(mySyracuse.flyingTime, theTab)
        theMatrixVol = np.array(theTabVol)
        fig.add_subplot(2, 3, 1)
        plt.imshow(theMatrixVol)
        plt.title("Flying time")

        #fig 2 - Highest Val
        theTabHigh = mySyracuse.tableThroughtFunc(mySyracuse.highestVal, theTab)
        theMatrixHigh = np.array(theTabHigh)
        fig.add_subplot(2, 3, 2)
        plt.imshow(theMatrixHigh)
        plt.title("Highest value")

        #fig 3 - Stoping value
        theTabStop = mySyracuse.tableThroughtFunc(mySyracuse.stopingVal, theTab)
        theMatrixStop = np.array(theTabStop)
        fig.add_subplot(2, 3, 3)
        plt.imshow(theMatrixStop)
        plt.title("Stoping value")

        #fig 4 - Flying time
        fTabVol = flatten(theTabVol)
        fig.add_subplot(2, 3, 4)
        plt.plot(range(1, len(fTabVol)+1), fTabVol, '.')
        plt.title("Flying time")

        #fig 5 - Highest Val
        fTabHigh = flatten(theTabHigh)
        fig.add_subplot(2, 3, 5)
        plt.plot(range(1, len(fTabHigh)+1), fTabHigh, '.')
        plt.title("Highest value")

        #fig 6 - Data
        fig.add_subplot(2, 3, 6)
        txt = "Valid data : {0}%".format(100, [1, 2, 4])
        txt = txt.join("Highest flying time : {0}".format(max(fTabVol)))
        txt = txt.join("Average flying time : {0}".format(average(fTabVol)))
        txt = txt.join("Highest value : {0}".format(max(theTabHigh)))
        txt = txt.join("Average highest value : {0}".format(average(theTabHigh)))
        loopingList = mySyracuse.listLoop(flatten(theTab))
        txt = txt.join("\nLooping lists ({0}): \n".format(len(loopingList)))
        for i in loopingList:
            txt = txt.join(i+"\n")
        plt.text(0.05, 0.9, txt, dict(size=10))
        plt.axis('off')
        plt.title("Data")


        #Show and save
        if isShowing :
            plt.show()
        if isSave :
            fileName = "img/{0}.png".format(name)
            plt.savefig(fileName)

def flatten(t):
    return [item for sublist in t for item in sublist]

if __name__ == '__main__':
    chooseSetup()
