from patterns import pattern as pt
import similarity as sim
from data import data
import hxt
import matplotlib.pyplot as plt


ind1=[]
ind2=[]
ind3=[]
i=200
while i<len(data.df):
    timenow = data.df.iloc[i].date
    print(timenow)
    isok, ii = pt.direction(timenow)
    if isok:            
        end_pt = i + pt.pt_length + ii        
        ind1.append(hxt.hxt(end_pt, pt.ind1))   # S/t ~ h
        ind2.append(hxt.hxt(end_pt, pt.ind2))
        ind3.append(hxt.hxt(end_pt, pt.ind3))
        print('fit the conditions with marks of ind3: ', ind3[-1])        
    i = i+10    

ind1.sort() 
ind2.sort()
ind3.sort()

with open('result1.txt','w') as f:
    f.write(str(ind1))
    f.write(str(ind2))
    f.write(str(ind3))

plt.plot(ind1)
plt.plot(ind2)
plt.plot(ind3)
plt.show()
