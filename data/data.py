import pandas as pd
import os
from datetime import datetime, timedelta

POINT_SIZE = 1e5

print('invoked!')
df = pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)),'EURAUD60.csv'))
df['date']=df['date'].apply(lambda x:datetime.strptime(x, '%Y.%m.%d-%H:%M'))

def aver_volume_of_time(t):
    v = []
    subset = df[df.date < t]
    index = -1
    for i in range(30):
        while True:
            if datetime.hour(subset.iloc[index].date) == datetime.hour(t):
                v.append(subset.iloc[index].volume)
                break
            index-=1
    v.sort()
    return int((v[14] + v[15] +v[16])/3)

def aver_weekday_volume_of_time(t):
    v = []
    subset = df[df.date < t]
    index = -1
    for i in range(5):
        while True:
            if datetime.weekday(subset.iloc[index].date) == datetime.weekday(t) and datetime.hour(subset.iloc[index].date) == datetime.hour(t):
                v.append(subset.iloc[index].volume)
                break
            index-=1
    v.sort()
    return int((v[0] + v[1] +v[2] + v[3] +v[4])/5)


def aver_bodysize_of_time(t):
    v = []
    subset = df[df.date < t]
    index = -1
    for i in range(30):
        while True:
            if datetime.hour(subset.iloc[index].date) == datetime.hour(t):
                bds = abs(subset.iloc[index].close - subset.iloc[index].open) * POINT_SIZE
                v.append(bds)
                break
            index-=1
    v.sort()
    return int((v[14] + v[15] +v[16])/3)
