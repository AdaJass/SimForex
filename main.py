from patterns import pattern as pt
import similarity as sim
from data import data
import hxt
import matplotlib.pyplot as plt


ind1=[]
ind2=[]
ind3=[]

for i in range(200,len(data.df),10):
    timenow = data.df.iloc[i].date
    if pt.corejudge(timenow):
        end_pt = i + pt.pt_length 
        ind1.append(hxt.hxt(end_pt, pt.ind1))   # S/t ~ h
        ind2.append(hxt.hxt(end_pt, pt.ind2))
        ind3.append(hxt.hxt(end_pt, pt.ind3))

ind1.sort() 
ind2.sort()
ind3.sort()
plt.plot(ind1)
plt.plot(ind2)
plt.plot(ind3)
plt.show()