import pandas as pd
import numpy as np

data = {
    'server_id': ['SRV-101', 'SRV-102', 'SRV-103', 'SRV-104', 'SRV-105', 'SRV-106'],
    'region': ['US-East', 'EU-West', 'US-East', 'Asia-South', 'EU-West', 'US-East'],
    'cpu_usage_pct': [85.5, 42.1, np.nan, 91.2, 33.5, 88.0], # Missing value included
    'mem_usage_gb': [16, 8, 32, 12, 4, 16],
    'uptime_days': [120, 5, 45, 200, 12, 80]
}
df_infra = pd.DataFrame(data)

#test ground
#find the rows with nan values 
#df_infra[df_infra['cpu_usage_pct].isna()] using boolean indexing, returns rows that have nan 


#Data Sanitation
#imputation, replacing with a statistical value, in this case, the mean values of the cpu_usage_pct
median_cpu  = df_infra['cpu_usage_pct'].median()
df_infra['cpu_usage_pct'] = df_infra['cpu_usage_pct'].fillna(median_cpu)


#Resource Normalization 
load_score = np.array((df_infra['cpu_usage_pct']*df_infra['mem_usage_gb'])/100)
df_infra['load_score'] = load_score #easiest assignment of new column 
#more pragmatic approach
#df_infra = df_infra.assign(load_score=load_score)
print(type(df_infra))

#Threshold Alerting
ser = df_infra[df_infra['cpu_usage_pct']>80]
alert = ser[ser['uptime_days']>100]
print(alert)
print(type(alert)) #still a dataframe, should actually use the logical operator 

#Regional Aggregation
#find unique regions and creating a new data frame using two ways: combining list and dictionary 
unique_keys = df_infra['region'].unique()
new_data_list = []
mean_load_score = []
for key in unique_keys: 
    temp_region_df = df_infra[df_infra['region']== key]
    load_score_avg = temp_region_df['load_score'].mean()
    mean_load_score.append(load_score_avg)
    new_data_list.append({'region': key, 'mean_load_score':load_score_avg})
new_data_by_region ={'region':unique_keys,'mean_load_score': mean_load_score} 
print(new_data_by_region)
df_by_region =pd.DataFrame(new_data_by_region)
df_by_region2 = pd.DataFrame(new_data_list)
print(df_by_region)
print(df_by_region2) #only assessed if string array in dictionary didn't affect the arrangements of the keys

 
#using groupby method
groupby_df = df_infra.groupby('region')[['load_score']].mean().reset_index()
#reset_index() method gives a more clean dataframe 
print(groupby_df)