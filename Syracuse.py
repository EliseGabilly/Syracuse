import matplotlib.pyplot as plt

class Syracuse:

    def __init__(self, a, b):
        self.a=3
        self.b=1
    
    def oneStep(self, n):
        res=0
        if (n%2==0):
            res=n/2
        else:
            res=self.a*n+self.b
        return res

    def listAllVal(self, n):
        listVal=[n]
        next=self.oneStep(n)
        while(not listVal.__contains__(next)):
            listVal.append(next)
            next=self.oneStep(next)
        return listVal

    """
        Create a list of size size containning list of size size
        example : size 3 will return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    def table(self, size):
        tab=[]
        for i in range(size):
            row=[]
            for j in range(size):
                row.append(self.listAllVal(size*i+j+1))
            tab.append(row)
        return tab

    """
        Apply func to every element of tab
        func should be :
        - flyingTime : if you want to know how long before the function loop
        - loopSize : if you want to know the size of the loop
        - stopingVal : if you want to know the first value to repeat
    """
    def tableThroughtFunc(self, func, tab):
        for row in range(len(tab)):
            for elem in range(len(tab[row])):
                tab[row][elem]=func(tab[row][elem])
        return(tab)

    #flyingTime : if you want to know how long before the function loop
    def flyingTime(self, l):
        return len(l)

    #loopSize : if you want to know the size of the loop
    def loopSize(self, l):
        next=self.oneStep(l[-1])
        return len(l)-l.index(next)

    #stopingVal : if you want to know the first value to repeat
    def stopingVal(self, l):
        return l[-1]

