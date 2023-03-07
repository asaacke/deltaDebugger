import os;
import sys;
import subprocess

def main():
    if len(sys.argv) < 3:
        sys.exit("Incorrect arguments entered")
    
    n = sys.argv[1]
    interestingFunc = sys.argv[2]
    
    if len(sys.argv) > 3:
        for i in range(3, len(sys.argv)):
            interestingFunc += " "
            interestingFunc += sys.argv[i]
    c = []
    for i in range(int(n)):
        c.append(i)

    d = Delta(interestingFunc) 
    subset = d.DD([], c)
    #output = []
    #lsubset = len(subset)
    if not isinstance(subset, int):
        subset.sort()
    #else:
    #    for i in range(len(subset)):
    #        lsubseti = len(subset[i])
            
    #        if lsubseti > 1:
    #            for j in range(l):
    #                output.append(subset[l][j])
            
    #        if lsubseti == 1:
    #            output.append(subset[i])

    #    subset.sort()
    print(subset)
    return

class Delta():

    def __init__(self, interestingFuncIn):
        self.interestingFunc = interestingFuncIn
    

    def DD(self, P, c):
        l = len(c)
        if l == 1:
            return c[0]

        mid = l // 2
        
        p1 = []

        for i in range(mid):
            p1.append(c[i])

        p2 = []
        for i in range(mid, l):
            p2.append(c[i])
        
        strp = " ".join(str(x) for x in P)
        strc = " ".join(str(x) for x in c)
        strp1 = " ".join(str(x) for x in p1)
        strp2 = " ".join(str(x) for x in p2)
        str1 = " ".join(str(x) for x in P + p1)
        
        result1 = os.system(self.interestingFunc + " " + str1)
        if result1:
            l = self.DD(P, p1)
            return l
        
        str2 = " ".join(str(x) for x in P + p2)
        result2 = os.system(self.interestingFunc + " " + str2)
        if result2:
            return self.DD(P, p2)
        else:
            output = []
            call1 = self.DD(P + p2, p1)
            if isinstance(call1, int):
                output.append(call1)
            else:
                for i in range(len(call1)):
                    output.append(call1[i])

            call2 = self.DD(P + p1, p2)
            if isinstance(call2, int):
                output.append(call2)
            else:
                for i in range(len(call2)):
                    output.append(call2[i])

            return output
            #return [self.DD(P + p2, p1)] + [self.DD(P + p1, p2)]
        
        


if __name__ == "__main__":
    main()


#psuedo
#DD(P, {c1, ..., cn}){
#if n = 1 then return {c1}
#let P1 = {c1, … cn/2}
#let P2 = {cn/2+1, …, cn}
#if Interesting(P P1) = Yes then return DD(P,P1)
#if Interesting(P P2) = Yes then return DD(P,P2)
#else return DD(P P2, P1) DD(P P1, P2)
#}
