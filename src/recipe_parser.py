# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 16:24:09 2018

@author: wangs
"""
import re 
from googletrans import Translator
import pandas as pd
import numpy as np
import jaconv
from gensim.models import word2vec

class word_parser:
    
#    def __init__(self):
#        self.
#        self.
    def ch_parser(ch_recipe):
        #中国レシピを整理し、日本語に翻訳する。図面作成、単語ベクトル生成用データを準備する
        
        #変な字を消す、stringとリストの変換
        replacestr1=re.compile('原料：|。')
        replacestr2=re.compile('\\[|\\n| ')
        ch_recipe.loc[:,'ingredients']=ch_recipe.loc[:,'ingredients'].str.replace(replacestr1,'').str.replace('生抽','酱油').str.replace('白糖','糖').str.split('、')
        bigsoupcn=ch_recipe.loc[:,'ingredients'].to_string(index=False,header=False).replace(r']',',').replace(r'...','')
        bigsoupcn2=replacestr2.sub('',bigsoupcn).split(',')
        #日本語に翻訳
        translator=Translator()
        transed_ingre=pd.DataFrame(pd.Series(bigsoupcn2).value_counts()[:500],columns=['frequency'])
        print('中国レシピを日本語に通訳中...')
        trans=translator.translate(transed_ingre.index.tolist(),dest='ja')
        transpair=[]
        #平仮名をカタカナに変換する
        for i in np.arange(5):
            for word in trans[100*i:100*(i+1)]:
                hira=word.text
                kata=jaconv.hira2kata(hira)
                transpair.append(kata)
        #wordcoud、単語ベクトル生成用データを準備する
        transed_ingre.loc[:,'janame'],transed_ingre.loc[:,'frequency']=transpair,transed_ingre.loc[:,'frequency']/10000
        transed_ingre=transed_ingre.set_index('janame')
        cncloudsource=transed_ingre.to_dict()
        cncloudsource=cncloudsource['frequency']
        ch_recipe.loc[:,'ingredientlist']=ch_recipe.loc[:,'ingredients']
        #ランキング、wordcloud作成、単語ベクトル生成用データの出力
        return transed_ingre,cncloudsource,ch_recipe
    def ja_parser(ja_recipe):
        #日本レシピを整理し、図面作成、単語ベクトル生成用データを準備する
        
        p1_data=ja_recipe
        p1_data=p1_data.set_index('recipename')
        
        #変な字を消す、stringとリストの変換
        kako=re.compile(r'([(（].+?[)）])')
        delid=re.compile(r'ID\d{7},')
        graphstr=re.compile(r'\*|〇|▲|□|◇|☆|●|◆|○|◎|┗|★')
        p1_data.loc[:,'ingredientlist']=p1_data.loc[:,'ingredient'].str.replace(kako,'').str.replace(delid,'').str.replace(graphstr,'').str.replace(r'\n','').str.replace(r',,','')
        p1_data.loc[:,'ingredientlist']=jaconv.hira2kata(p1_data.loc[:,'ingredientlist'].str)
        p1_data.loc[:,'ingredientlist']=p1_data.loc[:,'ingredientlist'].str.split(',')
        
        #wordcoud、単語ベクトル生成用データを準備する
        bigsoup=p1_data.loc[:,'ingredientlist'].to_string(index=False,header=False).replace('、',',').replace('[','').replace('\n','').replace(']','').replace('  ','').replace(' ','').replace('しょうが','生姜').replace('☆','').replace('しょうゆ','醤油').replace('オリーブ油','オリーブオイル').replace('にんじん','人参').replace('葱','ねぎ')
        littlesoup=bigsoup.split(',')
        littlesoup=pd.Series(littlesoup)
        frequency=(littlesoup.value_counts()[:500])/len(ja_recipe.index)
        
        #平仮名をカタカナに変換する
        kataindex=[]
        for x in frequency.index:
            y=jaconv.hira2kata(x)
            kataindex.append(y)
        frequency.index=kataindex
        jacloudsource=frequency.to_dict()
        frequency=pd.Series(frequency)
        
        #ランキング、wordcloud作成、単語ベクトル生成用データの出力
        return frequency,jacloudsource,p1_data
    
    def new_recipe_creater(allrecipe,new_ingre):
        #新レシピの生成：元食材の単語ベクトルと近い食材を新レシピの食材にする。ある程度の変化を残すため、相関性第三位の食材を選ぶ。
        ingredient_vector=word2vec.Word2Vec(allrecipe.loc[:,'ingredientlist'],size=65,min_count=70)
        for x in new_ingre:
            new_x=ingredient_vector.wv.most_similar(x)[2]
            print(new_x)