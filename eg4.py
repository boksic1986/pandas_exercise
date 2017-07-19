# -*-coding:utf-8-*-
# !/usr/bin/env python
# Author           :               Jiucheng
# Email            :        chenjiucheng@1gene.com.com
# Last modified    :        
# Description      :        
# update      	   :               2017/6/26     
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

tips = pd.read_csv('/lustre/project/og04/chenjiucheng1608/Vcf_com/vcf_combines/Vcf_combine/libs/tips.csv')

print(tips.head(10))
# print(tips.columns)
print('\n'*5)
# print(tips.loc[10:15, ['total_bill', 'tip']])

first = tips.groupby('day')[['total_bill', 'tip']].first()
hdf = tips.set_index(['day', 'time', 'sex', 'smoker', 'size']).sort_index()

# print(first)
# print(hdf)

tps = (pd.read_csv('/lustre/project/og04/chenjiucheng1608/Vcf_com/vcf_combines/Vcf_combine/libs/tips.csv')
       .rename(columns = {'sex':'gender'})
       .assign(real_bill = lambda x: x['total_bill'] + x['tip'],
               percent = lambda x: x['tip'] / x['total_bill'])
       )

tps2 = (tps.dropna(subset = ['percent'])
        .sort_values('total_bill')
        # .drop(['day', 'time'], axis = 1)
        .query('size > 2 & percent < 0.7')
        .groupby(['gender','smoker']).apply(lambda x:x.sort_values('real_bill', ascending=False).head())
        .drop(['day', 'time', 'smoker', 'gender'], axis=1)
        )

tps3 = (pd.read_csv('/lustre/project/og04/chenjiucheng1608/Vcf_com/vcf_combines/Vcf_combine/libs/tips.csv')
       .rename(columns = {'sex':'gender'})
       .assign(real_bill = lambda x: x['total_bill'] + x['tip'],
               percent = lambda x: x['tip'] / x['total_bill'])
       .dropna(subset = ['percent'])
       .query('size > 2 & percent < 0.7')
       .groupby(['gender', 'smoker']).apply(lambda x: x.sort_values('total_bill').head())
       .drop(['day', 'time', 'smoker', 'gender'], axis=1)
       )




# print(tps2.head())
# print(tps2)
print(tps3)