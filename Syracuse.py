import matplotlib.pyplot as plt

class Syracuse:

    def __init__(self, a, b):
        self.a=3
        self.b=1
    
    """
        Apply ont step of the Syracuse-like function :
        (if mod 2) f(x) = x/2
        (else) f(x) = ax+b 
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
        exemple : n=7 for a=3 and b=1 will return [7, 11, 17, 13, 5, 1, 4, 2, 1]
    """
    def listAllVal(self, n):
        listVal=[n]
        next=self.oneStep(n)
        while((not listVal.__contains__(next)) and len(listVal)<=500 ):
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

    """
        flyingTime : if you want to know how long before the function loop
        exemple : for [7, 11, 17, 13, 5, 1, 4, 2, 1] will return 9
    """
    def flyingTime(self, l):
        return len(l)-1

    """
        loopSize : if you want to know the size of the loop
        exemple : for [7, 11, 17, 13, 5, 1, 4, 2, 1] will return 3
    """
    def loopSize(self, l):
        next=self.oneStep(l[-1])
        return len(l)-l.index(next)

    """
        stopingVal : if you want to know the first value that repeat
        exemple : for [7, 11, 17, 13, 5, 1, 4, 2, 1] will return 1
    """
    def stopingVal(self, l):
        return l[-1]

