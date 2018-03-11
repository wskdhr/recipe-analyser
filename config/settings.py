# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 16:07:00 2018

@author: wangs
"""
import os
import pandas as pd
from PIL import Image
import numpy as np
import jaconv
import json
import csv


    
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


    
recipe_ch=pd.read_json(os.path.join(BASE_DIR,'material/recipe_ch.json'),orient='records',lines=True)
recipe_ch.loc[:,'ingredients']=recipe_ch.loc[:,'ingredients']#.apply(''.join)
recipe_ja=pd.read_json(os.path.join(BASE_DIR,'material/recipe_ja.json'),orient='records',lines=True)
recipe_ja.loc[:,'ingredient']=recipe_ja.loc[:,'ingredient'].apply(','.join)
donuts=np.array(Image.open(os.path.join(BASE_DIR,'material/wordcloud pic.jpg')))
f=open(os.path.join(BASE_DIR,'material/yasai_list.txt'),'r')
o_yasai=f.read().splitlines()
yasai=[]
for x in o_yasai:
    y=jaconv.hira2kata(x)
    yasai.append(y)

