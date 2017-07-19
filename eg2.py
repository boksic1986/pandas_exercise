# -*-coding:utf-8-*-
# !/usr/bin/env python
# Author           :               Jiucheng
# Email            :        chenjiucheng@1gene.com.com
# Last modified    :        
# Description      :        
# update      	   :               2017/6/26     
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(15, 4),
                  index = pd.date_range('20170101', periods = 15),
                  columns = list('ABCD'))

df1 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20170102'),
                    'C': pd.Series(1, index = list(range(4)), dtype = 'float'),
                    'D': np.array([3] * 4, dtype = 'int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'}

                   )

df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four'] * 3

df2[df2['E'].isin(['one', 'two'])]
print(df1)
print(df1.dtypes)
