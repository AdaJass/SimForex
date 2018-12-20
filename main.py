from patterns import pattern as pt
import similarity as sim
from data import data
import hxt
import matplotlib.pyplot as plt


ind1=[]
ind2=[]
ind3=[]
i=80000
while i<len(data.df):
    timenow = data.df.iloc[i].date
    # print(timenow)
    isok = pt.direction(timenow)
    if isok:            
        end_pt = i+3       
        ind1.append(hxt.hxt(end_pt, pt.ind1))   # S/t ~ h
        ind2.append(hxt.hxt(end_pt, pt.ind2))
        ind3.append(hxt.hxt(end_pt, pt.ind3))
        print('fit the conditions with marks of ind3: ', ind3[-1],' now the time is: ',timenow) 
        i=i+10       
    else:
        i=i+2    

ind1.sort() 
ind2.sort()
ind3.sort()

with open('./patterns/result.txt','w') as f:
    f.write(str(ind1)+'\n')
    f.write(str(ind2)+'\n')
    f.write(str(ind3)+'\n')

plt.plot(ind1)
plt.plot(ind2)
plt.plot(ind3)
plt.show()