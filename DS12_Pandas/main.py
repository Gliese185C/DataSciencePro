import pandas as pd

pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

adv1_df = pd.read_csv('advertising_1.csv', sep=',', index_col='Number')

#print(adv1_df)
#print(adv1_df.shape)
#print(adv1_df.loc[8, 'Daily Internet Usage'])

adv2_df = pd.read_csv('advertising_2.csv',sep=',',index_col='Number')
#print(adv2_df.loc[533:536,:])
#print(adv2_df.shape)
#print(adv2_df.describe())


non_nulls_cols = adv2_df.dropna(axis=1,how='any')
cols_with_no_nulls = non_nulls_cols.columns.tolist()
#print(cols_with_no_nulls)

adv12_df = adv1_df._append(adv2_df)
#print(adv12_df)
#print(adv12_df['Daily Time Spent on Site'].mean())
#print(adv12_df[adv12_df['Daily Time Spent on Site'].isnull()])

adv3_df = pd.read_csv('advertising_3.csv',sep=',',index_col='Number')
#print(adv3_df[['Ad Topic Line','Clicked on Ad']])
adv123_df = pd.concat([adv12_df,adv3_df],axis=0)
#print(adv123_df)

#print(adv123_df[adv123_df['Clicked on Ad'] == 1])

success_adv_df = adv123_df[adv123_df['Clicked on Ad'] == 1]
#print(success_adv_df.shape)

users_df = pd.read_csv('users.csv', sep=',')
#print(users_df)
#print(users_df.describe())

success_adv_df = success_adv_df.reset_index()
success_full_df = success_adv_df.merge(users_df, on='Number', how='inner')
#print(success_full_df)

#print(success_full_df[['Ad Topic Line','City','Country']].describe())

#print(success_full_df['Country'].value_counts())
#print(success_full_df[success_full_df['Country'] == success_full_df['Country'].value_counts().index[0]])

filtered_df = success_full_df[(success_full_df['Country'] == success_full_df['Country'].value_counts().index[0]) &
                              (success_full_df['Daily Internet Usage'] > 120) &
                              (success_full_df['Age'] < 30)]

#print(filtered_df)

filtered_df2 = filtered_df[(filtered_df['Daily Time Spent on Site'].isnull()) | (filtered_df['Daily Time Spent on Site'] > 55)]

#print(filtered_df2)

model_df = adv123_df[adv123_df['Ad Topic Line'].str.contains("model")]
#print(model_df)

model_popular_df = model_df[model_df['Daily Time Spent on Site'] > model_df['Daily Time Spent on Site'].mean()]

print(model_popular_df)