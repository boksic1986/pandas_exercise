#-*-coding:utf-8-*-
#!/usr/bin/env python
# Author           :               Jiucheng
# Email            :        chenjiucheng@1gene.com.com
# Last modified    :        
# Description      :        
# update      	   :               2017/6/25     

import pandas as pd
import numpy as np

s = pd.Series([1, 3, 5, np.nan, 6, 8], index = list('abcdef'), name = 'GENE')
s2 = pd.Series(np.random.randn(7))
print(s)
# print(s2)
# print(s.index)
# print(s.name)
# print(s.size)

