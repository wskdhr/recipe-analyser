# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 16:42:01 2018

@author: wangs
"""
import pandas as pd
import os
from config.settings import *
from src.recipe_parser import word_parser
import matplotlib.pyplot as plt 

from wordcloud import WordCloud

#図面作成用Fontの準備
font=r'C:\Windows\Fonts\Meiryo.ttc'
plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False 
#データの読み込む
chinese_recipe_ranking,chinese_recipe_cloud,chinese_recipe_alldata=word_parser.ch_parser(recipe_ch)
japanese_recipe_ranking,japanese_recipe_cloud,japanese_recipe_alldata=word_parser.ja_parser(recipe_ja)


def ranking(recipe,cn_or_ja):
    #食材頻度ランキングの作成
    print('材料ランキング作成中')
    recipe=recipe[:30]
    recipe.plot(kind='bar',figsize=(12,12),title='頻度ランキング'+cn_or_ja)
    plt.savefig(cn_or_ja+'rankingplot.jpg')
    plt.show()
    plt.close()

    
#    recipe_ch=pd.read_csv(r'D:\Files\Python\my program\cookpad analysis real\material\recipe_ch.csv')  
def wordcloudplt(recipe,name):
    #食材頻度のwordcloud
    print('料理wordcloud作成中')
    wordcloud = WordCloud(background_color="white",mask=donuts,relative_scaling=1,font_path=font,ranks_only=True,width=5000, height=5000, margin=2,max_words=500).generate_from_frequencies(recipe)
    plt.imshow(wordcloud)
    plt.show()
    
    wordcloud.to_file(name+'cloudplot.png')
    plt.close()
def healthy_points(recipe,name):
    count=0
    for x in recipe.index[:50]:
        if x in yasai:
            count+=1
    healthy_point=count/50
    labels = 'vegatable', 'others'
    sizes = [healthy_point,1-healthy_point]
    explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  
    
    fig1.savefig(name+'healthy_point.jpg')
    plt.show()
    plt.close()
    print(name,':',healthy_point)
    return 
    
def main():
    
    #ranking(chinese_recipe_ranking,'中華料理')
    #wordcloudplt(chinese_recipe_cloud,'中華料理')
    
    #ranking(japanese_recipe_ranking,'日本料理')
    #wordcloudplt(japanese_recipe_cloud,'日本料理')
    
    #healthy_points(chinese_recipe_ranking,'野菜の割合(中華料理)')
    #healthy_points(japanese_recipe_ranking,'野菜の割合(日本料理)')
    
    old_recipe=input("old recipe:(漢字とカタカナを入力し、食材間「、」で接続)")
    old_recipe=old_recipe.split('、')
    word_parser.new_recipe_creater(japanese_recipe_alldata,old_recipe)