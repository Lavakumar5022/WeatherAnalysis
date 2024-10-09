import pandas as pd
import numpy as np 

df=pd.read_csv('T3minidata.csv',encoding='unicode_escape')

# print(df.columns)
low=df['Average humidity (%)'].min()
# print("LOW",low)
low_day=df[df['Average humidity (%)']==low]['Day'].iloc[0]
lowdatetime=pd.to_datetime(low_day,format='%d-%m-%Y').month
# print(low_day)
# print(lowdatetime)

df['Day1']=pd.to_datetime(df['Day'],format='%d-%m-%Y')
df['month']=df['Day1'].dt.month
df_month= df.groupby('month')
df_median=df_month['Maximum gust speed (mph)'].median()
# print(df_median.idxmax())


#Q6 Average of Avg Temp from March 2010 to May 2012
st_date='2010-03-01'
end_date='2012-05-31'
df['day']=pd.to_datetime(df['Day'], format='%d-%m-%Y')
#filtering data
df_new=df[(df['day']>=st_date) & (df['day']<=end_date) ]
#Avg of Avg Temp
avg=df_new['Average temperature (°F)'].mean()
print(round(avg,2))

#Q7 Find the range of Ab=vg Temp on Dec-2010
st_date1='2010-12-01'
end_date1='2010-12-31'
ndf=df[(df['day']>=st_date1)&(df['day']<=end_date1)]
max1=ndf['Average temperature (°F)'].max()
min1=ndf['Average temperature (°F)'].min()
diff=round(max1-min1,2)
print("DIFF",diff)

#Q8 Out of all available records, which day has the highest difference btween Max pressure and Min pressure. [format:'YYYY-MM-DD']
df['diff_press']=df['Maximum pressure ']-df['Minimum pressure ']
max_diff=df['diff_press'].max()
req_day=df[df['diff_press']==max_diff]['day'].iloc[0]
print(req_day.strftime('%Y-%m-%d'))

#Q9 How many days falls under median(Equal to median) of Barometer reading
median_bar=df['Average barometer (in)'].median()
no_of_days9=len(df[df['Average barometer (in)']==median_bar]['Average barometer (in)'])
print(no_of_days9)

#Q10 Out of all the available records how many days are with in one standard deviation of Average Temperature
mean_temp=df['Average temperature (°F)'].mean()
std_temp=df['Average temperature (°F)'].std()
l=mean_temp-std_temp
u=mean_temp+std_temp
no_of_days10=len(df[(df['Average temperature (°F)']>=l)& (df['Average temperature (°F)']<=u)])
print(no_of_days9)