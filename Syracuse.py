import numpy as np
import copy

class Syracuse:

    def __init__(self, a, b):
        self.a=a
        self.b=b
    
    """
        Apply ont step of the Syracuse-like function :
        (if mod 2) f(x) = x/2
        (else) f(x) = ax+b 
        as ax+b doesn't always generate a even number we don't use the shortcut f(x) = (ax+b)/2
    """
    def oneStep(self, n):
        res=0
        if (n%2==0):
            res=n/2
        else:
            res=self.a*n+self.b
        return res

    """
        Apply the Syracuse-like function to n and return the list of value generated
        exemple : n=6 for a=3 and b=1 will return [6, 3, 10, 5, 16, 8, 4, 2, 1, 4]
        note : return an empty list if it doesn't loop after 500 step
    """
    def listAllVal(self, n):
        listVal=[n]
        next=self.oneStep(n)
        while((not listVal.__contains__(next)) and len(listVal)<=500 ):
            listVal.append(next)
            next=self.oneStep(next)
        if(len(listVal)==500):
            return []
        listVal.append(next)
        return listVal

    """
        Create a list of size size containning list of size size elements
        Element are the syracuse suite for the the number n given by the position of the element n = size*colone + row + 1
        example : size 2 will return [[[1, 4, 2, 1], [2, 1, 4, 2]], [[3, 10, 5, 16, 8, 4, 2, 1, 4], [4, 2, 1, 4]]]
    """
    def syracuseTable(self, size):
        tab=[]
        for i in range(size):
            row=[]
            for j in range(size):
                l = self.listAllVal(size*i+j+1)
                row.append(l)
            tab.append(row)
        return tab

    def listLoop(self, tab):
        return null

    """
        Apply func to every element of tab
        func should be :
        - flyingTime : if you want to know how long before the function loop
        - loopSize : if you want to know the size of the loop
        - stopingVal : if you want to know the first value to repeat
    """
    def tableThroughtFunc(self, func, tab):
        tabRes = copy.deepcopy(tab)
        for row in range(len(tab)):
            for elem in range(len(tab[row])):
                tabRes[row][elem]=func(tab[row][elem])
        return(tabRes)

    """
        flyingTime : if you want to know how long before the function loop
        exemple : for [6, 3, 10, 5, 16, 8, 4, 2, 1, 4] will return 9
    """
    def flyingTime(self, l):
        if not l:
            return np.NaN
        return len(l)-1

    """
        loopSize : if you want to know the size of the loop
        exemple : for [6, 3, 10, 5, 16, 8, 4, 2, 1, 4] will return 3
    """
    def loopSize(self, l):
        if not l:
            return np.NaN
        next=self.oneStep(l[-1])
        return len(l)-l.index(next)

    """
        stopingVal : if you want to know the first value that repeat
        exemple : for [6, 3, 10, 5, 16, 8, 4, 2, 1, 4] will return 4
    """
    def stopingVal(self, l):
        if not l:
            return np.NaN
        return l[-1]
 
    """
        highestVal : if you want to know the highest value
        exemple : for [6, 3, 10, 5, 16, 8, 4, 2, 1, 4] will return 16
    """
    def highestVal(self, l):
        if not l:
            return np.NaN
        return max(l)

