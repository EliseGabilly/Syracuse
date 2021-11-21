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
        runForMultiple(multipleSize, valueSize, isSaveRecap, isSaveEvery)
    else :
        isShowing = False
        while True :
            userInput = input("Show the output plot ? (y/n) ")
            if(userInput=="n" or userInput=="y"):
                if(userInput=="y"):
                    isShowing = True
                break
        isSave = False
        while True :
            userInput = input("Save output plot ? (y/n) ")
            if(userInput=="y" or userInput=="n"):
                if(userInput=="y"):
                    isSave = True
                break
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
        runForSingle(a, b, size, isSave, isShowing)

def runForMultiple(multipleSize, valueSize, isSaveRecap, isSaveEvery):
    #create figures
    figFlying, axsFlying = plt.subplots(multipleSize, multipleSize+1)
    figFlying.suptitle("Flying")
    figHighest, axsHighest = plt.subplots(multipleSize, multipleSize+1)
    figHighest.suptitle("Highest")
    figStoping, axsStoping = plt.subplots(multipleSize, multipleSize+1)
    figStoping.suptitle("Stoping")
    figFlyingPlot, axsFlyingPlot = plt.subplots(multipleSize, multipleSize+1)
    figFlyingPlot.suptitle("FlyingPlot")
    figHighestPlot, axsHighestPlot = plt.subplots(multipleSize, multipleSize+1)
    figHighestPlot.suptitle("HighestPlot")
    figData, axsData = plt.subplots(multipleSize, multipleSize+1)
    figData.suptitle("Data")

    #HeatMap recap
    hpValidity = np.empty((multipleSize, multipleSize))
    hpValidity[:] = np.NaN
    hpFly = np.empty((multipleSize, multipleSize))
    hpFly[:] = np.NaN
    hpHigh = np.empty((multipleSize, multipleSize))
    hpHigh[:] = np.NaN
    hpNbLoop = np.empty((multipleSize, multipleSize))
    hpNbLoop[:] = np.NaN

    for a in range(1, multipleSize+1):
        mySyracuse= Syracuse(0, 0)
        print("a = {0}".format(a))
        for b in range(1, multipleSize+1):
            mySyracuse.updateAB(a, b)
            print("     b = {0}".format(b))
            oneTab = runForSingle(a, b, valueSize, isSaveEvery, False) #isShowing set to false as we doesn't want to open too much window
            
            #Heat map
            #flying time
            theTabVol = mySyracuse.tableThroughtFunc(mySyracuse.flyingTime, oneTab)
            theMatrixVol = np.array(theTabVol)
            axsFlying[b-1][a].imshow(theMatrixVol)
            axsFlying[b-1][a].axis('off')
            #Highest Val
            theTabHigh = mySyracuse.tableThroughtFunc(mySyracuse.highestVal, oneTab)
            theMatrixHigh = np.array(theTabHigh)
            axsHighest[b-1][a].imshow(theMatrixHigh)
            axsHighest[b-1][a].axis('off')
            #Stoping value
            theTabStop = mySyracuse.tableThroughtFunc(mySyracuse.stopingVal, oneTab)
            theMatrixStop = np.array(theTabStop)
            axsStoping[b-1][a].imshow(theMatrixStop)
            axsStoping[b-1][a].axis('off')

            #Plot
            #flying time
            fTabVol = flatten(theTabVol)
            axsFlyingPlot[b-1][a].plot(range(1, len(fTabVol)+1), fTabVol, 'o', markersize=0.5)
            axsFlyingPlot[b-1][a].set_xticks([])
            axsFlyingPlot[b-1][a].set_yticks([])
            #Highest Val
            fTabHigh = flatten(theTabHigh)
            axsHighestPlot[b-1][a].plot(range(1, len(fTabHigh)+1), fTabHigh, 'o', markersize=0.5)
            axsHighestPlot[b-1][a].set_xticks([])
            axsHighestPlot[b-1][a].set_yticks([])

            #Data
            validity = (len(fTabVol) - fTabVol.count(np.NaN))/len(fTabVol)*100
            txt=""
            if validity>1:
                txt = "Valid : {0}%\n".format(validity)
                txt += "Max fly : {0}\n".format(max(fTabVol))
                txt += "Max val : {:.2e}\n".format(max(fTabHigh))
                loopingList = mySyracuse.listLoop(flatten(oneTab))
                txt +="Looping lists ({0}): \n".format(len(loopingList))
                if(len(loopingList)<=5):
                    for i in loopingList:
                        if(len(i)>7):
                            txt += "'{2}' {0}...{1}\n".format(str(i[0:3]), str(i[-4:-1]), len(i))
                        else :
                            txt += "'{0}' {1}\n".format(len(i), i)
                hpValidity[b-1][a-1] = validity
                hpFly[b-1][a-1] = max(fTabVol)
                hpHigh[b-1][a-1] = max(fTabHigh)
                hpNbLoop[b-1][a-1] = len(loopingList)
                
            axsData[b-1][a].text(0.05, 0.1, txt, dict(size=10))
            axsData[b-1][a].axis('off')

    #add title to columns and rows
    cols = ['']+['A = {}'.format(col) for col in range(1, multipleSize+1)]
    rows = ['B = {}'.format(row) for row in range(1, multipleSize+1)]
    #Flying time
    for ax, col in zip(axsFlying[0], cols):
        ax.set_title(col)
    for ax, row in zip(axsFlying[:,0], rows):
        ax.text(0.9, 0.5, row, dict(size=10), rotation = 90)
        ax.axis('off')
    figFlying.tight_layout()
    #Highest value
    for ax, col in zip(axsHighest[0], cols):
        ax.set_title(col)
    for ax, row in zip(axsHighest[:,0], rows):
        ax.text(0.9, 0.5, row, dict(size=10), rotation = 90)
        ax.axis('off')
    figHighest.tight_layout()
    #Stoping value
    for ax, col in zip(axsStoping[0], cols):
        ax.set_title(col)
    for ax, row in zip(axsStoping[:,0], rows):
        ax.text(0.9, 0.5, row, dict(size=10), rotation = 90)
        ax.axis('off')
    figStoping.tight_layout()
    #Flying time plot
    for ax, col in zip(axsFlyingPlot[0], cols):
        ax.set_title(col)
    for ax, row in zip(axsFlyingPlot[:,0], rows):
        ax.text(0.9, 0.5, row, dict(size=10), rotation = 90)
        ax.axis('off')
    figFlyingPlot.tight_layout()
    #Highest value
    for ax, col in zip(axsHighestPlot[0], cols):
        ax.set_title(col)
    for ax, row in zip(axsHighestPlot[:,0], rows):
        ax.text(0.9, 0.5, row, dict(size=10), rotation = 90)
        ax.axis('off')
    figHighestPlot.tight_layout()
    #Highest value
    for ax, col in zip(axsData[0], cols):
        ax.set_title(col)
    for ax, row in zip(axsData[:,0], rows):
        ax.text(0.9, 0.5, row, dict(size=10), rotation = 90)
        ax.axis('off')
    figData.tight_layout()

    if isSaveRecap:
        fileName = "img/recapFlying_{0}_{1}.png".format(multipleSize, valueSize)
        figFlying.set_size_inches((multipleSize*2, multipleSize*2), forward=False)
        figFlying.savefig(fileName)
        fileName = "img/recapHighest_{0}_{1}.png".format(multipleSize, valueSize)
        figHighest.set_size_inches((multipleSize*2, multipleSize*2), forward=False)
        figHighest.savefig(fileName)
        fileName = "img/recapStoping_{0}_{1}.png".format(multipleSize, valueSize)
        figStoping.set_size_inches((multipleSize*2, multipleSize*2), forward=False)
        figStoping.savefig(fileName)
        fileName = "img/recapFlyingPlot_{0}_{1}.png".format(multipleSize, valueSize)
        figFlyingPlot.set_size_inches((multipleSize*2, multipleSize*2), forward=False)
        figFlyingPlot.savefig(fileName)
        fileName = "img/recapHighestPlot_{0}_{1}.png".format(multipleSize, valueSize)
        figHighestPlot.set_size_inches((multipleSize*2, multipleSize*2), forward=False)
        figHighestPlot.savefig(fileName)
        fileName = "img/recapData_{0}_{1}.png".format(multipleSize, valueSize)
        figData.set_size_inches((multipleSize*2.8, multipleSize*2), forward=False)
        figData.savefig(fileName)

    #Visual data recap
    figHMR, axsHMR = plt.subplots(2,2) #HMR for heat map recap
    figHMR.suptitle("Visual data recap")
    axsHMR[0][0].imshow(hpValidity, extent=[0.5, multipleSize+0.5, multipleSize+0.5, 0.5])
    axsHMR[0][0].set_title("Validity")
    axsHMR[0][1].imshow(hpHigh, extent=[0.5, multipleSize+0.5, multipleSize+0.5, 0.5])
    axsHMR[0][1].set_title("Max Hight")
    axsHMR[1][0].imshow(hpFly, extent=[0.5, multipleSize+0.5, multipleSize+0.5, 0.5])
    axsHMR[1][0].set_title("Max fly")
    axsHMR[1][1].imshow(hpNbLoop, extent=[0.5, multipleSize+0.5, multipleSize+0.5, 0.5])
    axsHMR[1][1].set_title("Nb Loop")

    plt.show()
    if isSaveRecap:
        fileName = "img/visualDataRecap_{0}_{1}.png".format(multipleSize, valueSize)
        figHMR.set_size_inches((multipleSize*2, multipleSize*2), forward=False)
        figHMR.savefig(fileName)


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
        plt.plot(range(1, len(fTabVol)+1), fTabVol, 'o', markersize=1)
        plt.title("Flying time")

        #fig 5 - Highest Val
        fTabHigh = flatten(theTabHigh)
        fig.add_subplot(2, 3, 5)
        plt.plot(range(1, len(fTabHigh)+1), fTabHigh, 'o', markersize=1)
        plt.title("Highest value")

        #fig 6 - Data
        fig.add_subplot(2, 3, 6)
        validity = (len(fTabVol) - fTabVol.count(np.NaN))/len(fTabVol)*100
        txt = "Valid data : {0}%\n\n".format(validity)
        txt += "Highest flying time : {0}\n".format(max(fTabVol))
        txt += "Average flying time : {0}\n".format(average(fTabVol))
        txt += "Highest value : {0}\n".format(max(fTabHigh))
        txt += "Average highest value : {0}\n\n".format(average(fTabHigh))
        loopingList = mySyracuse.listLoop(flatten(theTab))
        txt +="\nLooping lists ({0}): \n".format(len(loopingList))
        if(len(loopingList)>5):
            txt +="to many different loop to show"
        else :
            for i in loopingList:
                if(len(i)>11):
                    txt += "'{2}' {0}...{1}\n".format(str(i[0:5]), str(i[-6:-1]), len(i))
                else :
                    txt += str(i)+"\n"
        plt.text(0.05, 0.1, txt, dict(size=10))
        plt.axis('off')
        plt.title("Data")


        #Show and save
        if isShowing :
            plt.show()
            if isSave and validity<10:
                print("Only a validity of {0} for {1}".format(validity, name))
        if isSave and validity>10:
            fileName = "img/{0}.png".format(name)
            fig.set_size_inches((10, 7), forward=False)
            fig.savefig(fileName)
    return theTab

def flatten(t):
    return [item for sublist in t for item in sublist]

if __name__ == '__main__':
    chooseSetup()
