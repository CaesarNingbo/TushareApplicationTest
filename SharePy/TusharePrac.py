import tushare as ts
import datetime
import pandas as pd
#df = ts.get_today_all()
#df = ts.get_hs300s()
#path = 'C:\\Users\\Caesar\\Desktop\\test.xlsx'
#df.to_excel(path)

loc = 'C:\\Users\\Caesar\\Desktop\\test.xlsx'
df = pd.read_excel(loc, 0)
#处理日期
now_time = datetime.datetime.now()
yes_time = now_time + datetime.timedelta(days=-5)
yes_time_nyr = yes_time.strftime('%Y-%m-%d')

for codes in df[['code']].values:
    code = str(codes[0]).zfill(6)
    df = ts.get_hist_data(code,start=yes_time_nyr)
    p_change = df[['p_change']]
    if p_change.empty != True:
        p_change_today = p_change.values[0][0]
        if p_change_today > 5:
            print(code)
            print(p_change_today)
