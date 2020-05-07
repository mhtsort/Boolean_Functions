import itertools

def pb(x):
	s=lambda a,b:x
	pbool(s)
minterm={0:(False,False,False),
         1:(False,False,True),
         2:(False,True,False),
         3:(False,True,True),
         4:(True,False,False),
         5:(True,False,True),
         6:(True,True,False),
         7:(True,True,True)}
mintermexp={
    }
m=mintermexp
def minterms(n):
    *a,= itertools.product([False,True],repeat=n)    
    return a
def boolfunct(expr,varnum,toprint=True):

    if toprint:
        minterm=minterms(varnum)
        for i in minterm:
            for val in i:
                print(1 if val else 0,sep="",end=" | ")
            print(f"\t {(1 if expr(*i) else 0)}")
    else:
        output=""
        minterm=minterms(varnum)
        for i in minterm:
            for val in i:
                output=output+("1" if val else "0")+" | "
            output=output+f"\t {(1 if expr(*i) else 0)}\n"
        return output    
ops="abcdefghi"
def createminterms():
    for j in range(len(minterm)):
        expr=""
        for i,t in enumerate(minterm.get(j)):
            expr=expr+(""if t else "not ")+ops[i]+" and "
        mintermexp[j]=expr[:-4]
        print(expr[:-4])

createminterms()
def test():
    outcol1=[]
    outcol2=[]
    for i in range(len(m)):
        x=eval("lambda a,b,c:"+str(m[i]))
        boolfunct(x,3)
        print("=========================")
