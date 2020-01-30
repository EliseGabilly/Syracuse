class Syracuse:

    def __init__(self):
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
        while(next!=1):
        # while(not listVal.__contains__(next)):
            listVal.append(next)
            next=self.oneStep(next)
        # print("Temps de vol : "+str(len(listVal)))
        # print(listVal)
        return listVal

    def tempsDeVol(self, l):
        return len(l)

    def taileBoucle(self, l):
        next=self.oneStep(l[-1])
        return len(l)-l.index(next)

    def valeurDarret(self, l):
        return l[-1]

    def table(self):
        tab=[]
        size=10
        for i in range(size):
            row=[]
            for j in range(size):
                row.append(self.listAllVal(size*i+j+1))
            tab.append(row)
        return tab

    def tableThroughtFunc(self, func, tab):
        for row in range(len(tab)):
            for elem in range(len(tab[row])):
                tab[row][elem]=func(tab[row][elem])
        return(tab)

    # def table2matrix(self, tab):
