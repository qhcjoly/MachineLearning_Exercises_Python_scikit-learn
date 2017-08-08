# -*- coding:utf-8 -*-
# Anaconda 4.3.0 環境

import numpy
import matplotlib.pyplot as plt
import pandas

# scikit-learn ライブラリ関連
from sklearn import datasets                            # 
#from sklearn.cross_validation import train_test_split  # scikit-learn の train_test_split関数の old-version
from sklearn.model_selection import train_test_split    # scikit-learn の train_test_split関数の new-version
from sklearn.preprocessing import StandardScaler        # scikit-learn の preprocessing モジュールの StandardScaler クラス
from sklearn.metrics import accuracy_score              # 

# 自作クラス
import DataPreProcess


def main():
    #=========================================
    # 機械学習における前処理の練習プログラム
    #=========================================
    print("Enter main()")

    #-----------------------------------------
    # Practice 1 : 欠損値 NaN の補完
    #-----------------------------------------
    prePro1 = DataPreProcess.DataPreProcess()

    csv_data = '''
                  A,B,C,D
                  1.0,2.0,3.0,4.0
                  5.0,6.0,,8.0
                  10.0,11.0,12.0,
               '''
    
    prePro1.setDataFrameFromCsvData( csv_data )
    prePro1.print( "csv data" )

    prePro1.meanImputationNaN()
    prePro1.print( "欠損値 NaN の平均値補完" )

    #--------------------------------------------------
    # Practice 2 : カテゴリデータの処理
    # 名義 [nominal] 特徴量、順序 [ordinal] 特徴量
    #--------------------------------------------------
    prePro2 = DataPreProcess.DataPreProcess()

    # list から pandas データフレームを作成
    prePro2.setDataFrameFromList(
        list = [ 
                ['green', 'M', 10.1, 'class1'], 
                ['red', 'L', 13.5, 'class2'], 
                ['blue', 'XL', 15.3, 'class1'] 
            ]
    )

    prePro2.print( "list から pandas データフレームを作成" )

    # pandas データフレームにコラム（列）を追加
    prePro2.setColumns( ['color', 'size', 'price', 'classlabel'] )
    prePro2.print( "pandas データフレームにコラム（列）を追加" )
    
    # 順序特徴量 size の map(directionary) を作成
    dict_size = {
        'XL': 3,
        'L': 2,
        'M': 1
    }
    # 作成した map で順序特徴量を整数化
    prePro2.mappingOrdinalFeatures( key = 'size', input_dict = dict_size )
    prePro2.print( "順序特徴量 size の map(directionary) を作成し、作成した map で順序特徴量を整数化" )
    
    # クラスラベルのエンコーディング（ディクショナリマッピング方式）
    prePro2.encodeClassLabel("classlabel")
    prePro2.print( "クラスラベルのエンコーディング（ディクショナリマッピング方式" )

    # カテゴリデータのone-hot encoding
    prePro2.oneHotEncode( categories = ['color', 'size', 'price'], col = 0 )
    prePro2.print( "カテゴリデータのone-hot encoding" )


    #--------------------------------------------------
    # Practice 3 : データセットの分割
    # トレーニングデータとテストデータへの分割
    #--------------------------------------------------
    prePro3 = DataPreProcess.DataPreProcess()

    # Wine データセットの読み込み
    prePro3.setDataFrameFromCsvFile( "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data" )
    
    # 上記URLのWine データセットにはラベルがついてないので, 列名をセット
    prePro3.setColumns( 
        [
            'Class label', 'Alcohol', 'Malic acid', 'Ash',
            'Alcalinity of ash', 'Magnesium', 'Total phenols',
            'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins',
            'Color intensity', 'Hue', 'OD280/OD315 of diluted wines',
            'Proline'
        ] 
    )

    prePro3.print("Wine データセット")

    X_train, X_test, y_train, y_test \
    = prePro3.dataTrainTestSplit( 
        X_input = prePro3.df_.iloc[:, 1:].values,   # iloc : 行、列を番号で指定（先頭が 0）。df_.iloc[:, 1:] = 全行、1~の全列
        y_input = prePro3.df_.iloc[:, 0].values,    #
        ratio_test = 0.3
    )

    #--------------------------------------------------
    # Practice 4 : 特徴量のスケーリング
    # 正規化 [normalization], 標準化 [standardization]
    #--------------------------------------------------
    # わざわざ自作クラス DataPreProcess のオブジェクトを作成し, 
    # 上記の分割データ（ X_train, X_test, y_train, y_test）を設定.
    # ここの設計ウンコード臭がするので, 修正したい
    prePro4_X_train = DataPreProcess.DataPreProcess()
    prePro4_X_test  = DataPreProcess.DataPreProcess()
    prePro4_y_train = DataPreProcess.DataPreProcess()
    prePro4_y_test  = DataPreProcess.DataPreProcess()

    prePro4_X_train.setDataFrameFromDataFrame( X_train )
    prePro4_X_test.setDataFrameFromDataFrame( X_test )
    prePro4_y_train.setDataFrameFromDataFrame( y_train )
    prePro4_y_train.setDataFrameFromDataFrame( y_test )

    # 分割データ（トレーニングデータ、テストデータ）を出力
    prePro4_X_train.print( "トレーニングデータ" )
    prePro4_X_test.print("テストデータ")
    prePro4_y_train.print("トレーニング用教師データ")
    prePro4_y_test.print("テスト用教師データ")

    #--------------------------------------------------
    # Practice 5 : 有益な特徴量の選択
    # L1正則化による疎な解
    #--------------------------------------------------

    print("Finish main()")
    return

    
if __name__ == '__main__':
     main()

