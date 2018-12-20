from data import data

def hxt(end_pt, lens):
    pivot = data.df.iloc[end_pt].close
    S = 0
    for i in range(lens):
        inx = end_pt+i
        pprice = (data.df.iloc[inx].close + data.df.iloc[inx].open)/2 - pivot
        S = S + pprice * data.POINT_SIZE
    return S / lens