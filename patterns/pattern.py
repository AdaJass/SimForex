from data import data
pt_from = 'EURAUD60.csv'
pt_length = 16
ind1 = 4
ind2 = 12
ind3 = 24


def corejudge(pt_start_time):
    averbody = data.aver_bodysize_of_time(pt_start_time)
    avervolume = data.aver_volume_of_time(pt_start_time) 
    bodylittlebigger = 0
    volumelittlesmaller = 0
    maxvolume = avervolume
    for i in range(pt_length):
        indx = data.df[data.df.date == pt_start_time].index +i
        if abs(data.df.iloc[indx].close - data.df.iloc[indx].open)*data.POINT_SIZE > averbody*2:
            return False
        if abs(data.df.iloc[indx].close - data.df.iloc[indx].open)*data.POINT_SIZE > averbody*1.2:
            bodylittlebigger+=1
        if bodylittlebigger >5:
            return False
        timenow = data.df.iloc[indx].date
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
    
