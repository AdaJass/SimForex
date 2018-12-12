
basename='./data/EURAUD60'

with open(basename+'.csv','r') as f:
    lines = f.readlines()
for index,line in enumerate(lines):
    lines[index] = lines[index][:10] +'-' + lines[index][11:]
    # print(lines[index])
    # exit()
with open(basename+'.csv','w') as f:
    f.writelines(lines)
