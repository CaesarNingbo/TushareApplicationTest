import tushare as ts
import datetime
import pandas as pd
#获取所有股票数据
#print(ts.get_today_all())
#处理日期
now_time = datetime.datetime.now()
yes_time = now_time + datetime.timedelta(days=-30)
yes_time_nyr = yes_time.strftime('%Y-%m-%d')
#按市值最小排行
#df = ts.get_stock_basics()
#df = df.sort_values(by='totalAssets', ascending=True)
#print(df[['name','industry','totalAssets']])
loc = 'C:\\Users\\Caesar\\Desktop\\Data\\share.xlsx'
df = pd.read_excel(loc, 0)

#输出的execl_dataframe
df_out = pd.DataFrame(columns=['code', 'value'])
#沪深300
#share300 = ts.get_hs300s()
for codes in df[['code']].values:
    #print(codes[0])
    #20日历史数据
    code = str(codes[0]).zfill(6)
    df = ts.get_hist_data(code,start=yes_time_nyr)
    #print(type(df))
    if df is not None :
        close_df = df[['close']]
        #当天收盘价
        if close_df.empty != True :
            close_today = close_df.values[0][0]
            #print(close_today)
            #print(close_df)
            #20日收市价标准差
            total = 0#总价
            count = 0#总数
            eva = 0#均值
            sd = 0#标准差
            #循环一次求平均值
            for values in close_df.values:
                total += values[0]
                count += 1
            eva = total/count
            #print('count='+ str(count))
            #再循环一次求标准差
            for values in close_df.values:
                sd += (eva - values[0])**2
            sd = sd/count
            sd = sd ** 0.5

            #up线和down线
            ma20 = df[['ma20']].values[0][0]
            up = ma20+(2*sd)
            down = ma20-(2*sd)

            #%b指标
            if up-down !=0:
                sign_b = (close_today-down)/(up-down)
                if sign_b <0:
                    row = {'code':code,'value':sign_b}
                    df_out = df_out.append(row,ignore_index=True)
                    print(str(codes[0]).zfill(6))
                    print(sign_b)
print(df_out)

path = 'C:\\Users\\Caesar\\Desktop\\test.xlsx'
df_out.to_excel(path)