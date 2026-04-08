import pandas as pd 
import numpy as np 

#Data set 

txn_data = {
    'txn_id': range(1001, 1008),
    'cust_id': ['C-01', 'C-02', 'C-01', 'C-03', 'C-02', 'C-01', 'C-04'],
    'amount': [500, 12000, 450, 8000, 15000, 300, 20],
    'type': ['debit', 'debit', 'debit', 'credit', 'debit', 'debit', 'debit'],
    'location': ['NY', 'LDN', 'NY', 'TK', 'LDN', 'NY', 'NY']
}
df_bank = pd.DataFrame(txn_data)

#boolean mask on amount 
df_bank['is_audit_required']= df_bank['amount'] > 500
print(df_bank)


#calculate the debit amount based on the cust-id
#unique_cust_id  =df_bank['cust_id'].unique()
df_debit = df_bank[df_bank['type']=='debit']
df_cust_id = df_debit.groupby('cust_id')[['amount']].sum().reset_index()
print(df_cust_id)

#Outlier detection and creation of column risk_level if the amount is 5x mean transaction amount
mean_amt = df_bank['amount'].mean()
#filter based on cust_id
df_cust_id_all = df_bank.groupby('cust_id')[['amount']].sum().reset_index() 
risk_level = np.where(df_cust_id_all['amount'] > mean_amt,'High Risk', 'Standard') 
df_cust_id_all = df_cust_id_all.assign(risk_level = risk_level)
print(df_cust_id_all)


#Application of 0.5% International processing fee for transactions outside NY
df_bank_new = df_bank.copy()  #using this for a proper copy of dataframe, rather than creating another pointer
NY_false = df_bank_new['location'] != 'NY'
df_bank_new.loc[NY_false, 'amount'] = df_bank_new.loc[NY_false, 'amount'] *1.05
print(df_bank)
print(df_bank_new)