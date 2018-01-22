import tushare as ts
import pandas as pd

loc = 'C:\\Users\\Caesar\\Desktop\\Data\\share.xlsx'
df = pd.read_excel(loc, 0)

df_out = pd.DataFrame(columns=['code', 'value'])

for codes in df[['code']].values:
    #print(codes[0])
    #20日历史数据
    code = str(codes[0]).zfill(6)
    df = ts.get_hist_data(code)
    #print(type(df))
    if df is not None :
        turnover_df = df[['turnover']]
        if turnover_df.empty != True :
            turnover = turnover_df.values[0][0]
            if turnover>=15:
                row = {'code': code, 'value': turnover}
                df_out = df_out.append(row, ignore_index=True)
                print(code)
                print(str(turnover))


path = 'C:\\Users\\Caesar\\Desktop\\test.xlsx'
df_out.to_excel(path)