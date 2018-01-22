import tushare as ts
import pandas as pd

loc = 'C:\\Users\\Caesar\\Desktop\\Data\\share.xlsx'
df = pd.read_excel(loc, 0)

shareHis = ts.get_hist_data('002289')
shareHis = shareHis[['p_change']]
shareHis = shareHis[0:5]
for codes in df[['code']].values:
    choose = True
    num = str(codes[0]).zfill(6)
    shareHis = ts.get_hist_data(num)
    if shareHis is not None :
        shareHis = shareHis[['p_change']]
        shareHis = shareHis[0:5]

        for i in range(1,5):
            if(abs(shareHis.values[i][0])>3):
                choose = False
                break
        if choose and shareHis.values[0][0] > 6:
            print(num)
