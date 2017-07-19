# -*-coding:utf-8-*-
# !/usr/bin/env python
# Author           :               Jiucheng
# Email            :        chenjiucheng@1gene.com.com
# Last modified    :        
# Description      :        
# update      	   :               2017/6/26     
import pandas as pd
import numpy as np

df3 = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                    'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                    'C': np.random.randn(8),
                    'D': np.random.randn(8)})


def xs(row):
    res = {i: '|'.join([str(_i) for _i in row[i]]) for i in ['C', 'D']}
    return pd.Series(res)




df4 = df3.groupby(['A', 'B']).apply(xs)
print(df4.stack().unstack(1))
# print(df3)





df = pd.DataFrame(
    {'animal': 'cat dog cat fish dog cat cat'.split(), 'size': list('SSMMMLL'),
     'weight': [8, 10, 11, 1, 20, 12, 12],
     'adult': [False] * 5 + [True] * 2})

s2 = df.groupby('animal').apply(lambda subf: subf['size'][subf['weight'].idxmax()])

print(df)
print(s2)