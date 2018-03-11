# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 20:51:11 2018

@author: wangs
"""
import jaconv
import pandas as pd
import numpy as np
f=open(r'D:\Files\Python\my program\cookpad analysis real\material\yasai_list.txt','r')
y=pd.read_csv(r'D:\Files\Python\my program\cookpad analysis real\material\recipe_ja.csv')
y=
yasai=f.read().splitlines()
transpair=pd.DataFrame(yasai)
miao=pd.Series(['おう','ちょう']).to_string(index=False,header=False)
transpair=transpair.append(miao,ignore_index=True)
transpair.append()
for x in transpair[0]:    
    x=jaconv.hira2kata(x)
    print(x)

    
"""
for x in yasai.index:
    y=jaconv.hira2kata(x)
    transpair.append(y)
    print(y)
print(transpair)
"""