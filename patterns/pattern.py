from data import data
pt_from = 'EURAUD60.csv'
ind1 = 4
ind2 = 12
ind3 = 24

def body_vol(pt_start_time, n):    
    index = data.df[data.df.date == pt_start_time].index.values[0]
    bdvol = 0.0
    for i in range(n):        
        indx =  index - i
        body = abs(float(data.df.iloc[indx].close) - float(data.df.iloc[indx].open))*data.POINT_SIZE
        bdvol += body/data.df.iloc[indx].close
    return bdvol/n
    
def direction(pt_start_time):
    bdvol60 = body_vol(pt_start_time, 60)
    if body_vol(pt_start_time, 3) > bdvol60*1.3:        
        indx = data.df[data.df.date == pt_start_time].index.values[0]
        for i in range(3):
            index = indx + i
            cbd = float(data.df.iloc[index].close) - float(data.df.iloc[index].open)
            if body_vol(pt_start_time, 1) > bdvol60 and cbd*data.POINT_SIZE > 50 and data.df.iloc[indx].date.hour >= 4 and data.df.iloc[indx].date.hour <= 16:
                continue
            else:
                return False
        if i >=2:
            return True
    return False