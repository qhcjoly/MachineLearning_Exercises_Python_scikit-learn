# -*- coding:utf-8 -*-
# Anaconda 4.3.0 環境

import numpy
import matplotlib.pyplot as plt

# scikit-learn ライブラリ関連
from sklearn import datasets                            #
from sklearn.metrics import accuracy_score              # 

# 自作クラス
import Plot2D
import DataPreProcess


def main():
    print("Enter main()")
    #=============================================================================================
    # カーネル主成分分析 [kernelPCA による教師なしデータの次元削除、特徴抽出
    # scikit-learn ライブラリでのカーネル主成分分析使用
    #=============================================================================================

    #====================================================
    #   Data Preprocessing（前処理）
    #====================================================
    #----------------------------------------------------
    #   read & set  data
    #----------------------------------------------------
    
    
    #========================================================================
    # Learning Process (scikit-learn のPCAクラスを使用)＆
    #========================================================================
    # PCA で次元削除
    

    #====================================================
    #   汎化性能の評価
    #====================================================

    #-------------------------------
    # 識別率を計算＆出力
    #-------------------------------
    

    #--------------------------------------------------------
    # 次元削除した主成分空間での散布図
    #--------------------------------------------------------
    
    print("Finish main()")
    return
    
if __name__ == '__main__':
     main()