# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 16:58:57 2018

@author: wangs
"""

from bin.main import main
"""
    environment: python3+wordcloud+googletrans(日本語翻訳)+gensim(自然言語処理)
    
    Recipe analysis/
    	manage.py #分析を実行する
	    bin/
	     	__init__.py
		   main.py ランキング,wordcloud図面の作成,新レシピ,健康性評価の生成
	    config/
	  	    settings.py　    データの読み込み
	    material/
		    recipe_cn.json、 recipe_jp.json 　  中国レシピ集　日本レシピ集
		    yasai_list.txt	 野菜のリスト
		    wordcloud pic.jpg　wordcloud作成用
	    src/
		    parser.py	データの通訳、処理および単語ベクトルの生成

"""
    #分析を行う
if __name__ == '__main__':
    main()