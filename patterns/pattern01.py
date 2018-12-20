from data import data
pt_from = 'EURAUD60.csv'
pt_length = 16
ind1 = 4
ind2 = 12
ind3 = 24
averbody = 0
avervolume = 0

def corejudge(pt_start_time):
    global averbody
    global avervolume
    averbody = data.aver_bodysize_of_time(pt_start_time)
    avervolume = data.aver_volume_of_time(pt_start_time) 
    bodylittlebigger = 0
    volumelittlesmaller = 0
    maxvolume = avervolume
    index = data.df[data.df.date == pt_start_time].index.values[0]
    for i in range(pt_length):        
        indx =  index - i
        body = float(data.df.iloc[indx].close) - float(data.df.iloc[indx].open)
        if abs(body)*data.POINT_SIZE > averbody*2:
            return False
        if abs(body)*data.POINT_SIZE > averbody*1.2:
            bodylittlebigger+=1
        if bodylittlebigger >5:
            return False
        timenow = data.df.iloc[indx].date
        # print("this is pattern's time: ",timenow)        
        if 1.2*data.aver_volume_of_time(timenow) > data.df.iloc[indx].volume:
            volumelittlesmaller +=1
        if volumelittlesmaller>8:
            return False
        if data.df.iloc[indx].volume > data.aver_volume(timenow, 60)*2:
            return True
        if data.df.iloc[indx].volume > maxvolume:
            maxvolume = data.df.iloc[indx].volume
    if maxvolume > avervolume*2:
        return True
    return False        
    
def direction(pt_start_time):    
    if corejudge(pt_start_time):
        global averbody
        global avervolume
        indx = data.df[data.df.date == pt_start_time].index.values[0] + pt_length
        body = float(data.df.iloc[indx].close) - float(data.df.iloc[indx-pt_length].open)
        for i in range(10):
            index = indx+i
            cbd = float(data.df.iloc[index].close) - float(data.df.iloc[index].open)
            if body > 0 and cbd*data.POINT_SIZE > averbody*1.5 and data.df.iloc[index].date.hour >= 4 and data.df.iloc[index].date.hour < 16:
                return True, i
    return False, -1


