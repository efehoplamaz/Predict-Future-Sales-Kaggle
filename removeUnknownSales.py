import pandas as pd

df_sales_train =  pd.read_csv('./data/sales_train.csv')

for index, row in df_sales_train.iterrows():
    if row.item_cnt_day < 0:
        df_sales_train.drop(index, inplace=True)

df_sales_train.to_csv('sales_train_unknown_removed.csv')