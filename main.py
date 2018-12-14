from patterns import pattern as pt
import similarity as sim
from data import data
import hxt

ind1=[]
ind2=[]
ind3=[]

for i in range(200,len(data.df)):
    tempt = pt.build(data, i)
    if sim.sim(tempt, pt.standard) < pt.threshold:
        end_pt = i + pt.pt_length
        ind1.append(hxt.hxt(end_pt, pt.ind1))   # S/t ~ h
        ind2.append(hxt.hxt(end_pt, pt.ind2))
        ind3.append(hxt.hxt(end_pt, pt.ind3))

ind1.sort()
ind2.sort()
ind3.sort()
