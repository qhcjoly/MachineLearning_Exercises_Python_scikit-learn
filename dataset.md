## 検証用データセット

### Iris データセット : （csvフォーマット）
URL : https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

全サンプル数 150 個の内、アヤメの品種（"setosa", "versicolor", "versicolor" ）は、以下のように構成されている。</br
- 先頭（行）から 50 個が、品種 : "setosa" 
- 次の 50 個が 品種 : "versicolor" 
- 最後の 50 個が、品種 "virginica"

</br>

### ワインデータセット：（csvフォーマット）

URL : https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data</br>

コラムにラベルを追加して記載した表

||Class label  |Alcohol  |Malic acid   |Ash  |Alcalinity of ash|Magnesium |Total phenols|Flavanoids|Nonflavanoid phenols|Proanthocyanins|Color intensity|Hue|OD280/OD315 of diluted wines|Proline|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|0 |1 |14.23 |1.71  |2.43 |15.6 |127 |2.80|3.06|0.28|2.29|5.640000|1.04|3.92|1065|
|1 |1 |13.20 |1.78  |2.14 |11.2 |100 |2.65|2.76|0.26|1.28|4.380000|1.05|3.40|1050|
|2 |1 |13.16 |2.36  |2.67 |18.6 |101 |2.80|3.24|0.30|2.81|5.680000|1.03|3.17|1185|
|3 |1 |14.37 |1.95  |2.50 |16.8 |113 |3.85|3.49|0.24|2.18|7.800000|0.86|3.45|1480|
|4 |1 |13.24 |2.59  |2.87 |21.0 |118 |2.80|2.69|0.39|1.82|4.320000|1.04|2.93|735|  
|5 |1 |14.20 |1.76  |2.45 |15.2 |112 |3.27|3.39|0.34|1.97|6.750000|1.05|2.85|1450|
|...|...|...|...|...|...|...|...|...|...|...|...|...|...|...|
|170|3|12.20|3.03|2.32|19.0|96 |1.25|0.49|0.40|0.73|5.500000  |0.66|1.83|510|   
|171|3|12.77|2.39|2.28|19.5|86 |1.39|0.51|0.48|0.64|9.899999  |0.57|1.63|470|  
|172|3|14.16|2.51|2.48|20.0|91 |1.68|0.70|0.44|1.24|9.700000  |0.62|1.71|660|  
|173|3|13.71|5.65|2.45|20.5|95 |1.68|0.61|0.52|1.06|7.700000  |0.64|1.74|740|  
|174|3|13.40|3.91|2.48|23.0|102|1.80|0.75|0.43|1.41|7.300000  |0.70|1.56|750|  
|175|3|13.27|4.28|2.26|20.0|120|1.59|0.69|0.43|1.35|10.200000 |0.59|1.56|835|  
|176|3|13.17|2.59|2.37|20.0|120|1.65|0.68|0.53|1.46|9.300000  |0.60|1.62|840| 
|177|3|14.13|4.10|2.74|24.5|96 |2.05|0.76|0.56|1.35|9.200000  |0.61|1.60|560| 

</br>

### Brest Cancer Wisconsin データセット：（csvフォーマット）

URL : https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data

悪性腫瘍細胞と良性腫瘍細胞の 569 個のサンプルが含まれている。</br> 1 列目は固有の ID 、2 列目は悪性 [malignant] or 良性 [belign] を表すラベル、3 ~ 32 列目には、細胞核のデジタル画像から算出された 30 個の実数値の特徴量が含まれれいる。

|行番号|ID|悪性（M）/良性（B）|1|2|3|4|5|6|7|8|...|22|23|24|25|26|27|28|29|30|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|1|842302  |M  |17.990  |10.38  |122.80  |1001.0  |0.11840  |0.27760  |0.300100|0.147100|...|25.380|17.33|  184.60  |2019.0  |0.16220|  0.66560| 0.71190|  0.26540|  0.4601|  0.11890 |
|2|842517  |M  |20.570  |17.77  |132.90  |1326.0  |0.08474  |0.07864  |0.086900|0.147100|...|25.380|  17.33  |184.60  |2019.0  |0.16220  |0.66560|0.24160  |0.18600  |0.2750  |0.08902|
|3|84300903  |M  |19.690  |21.25  |130.00  |1203.0  |0.10960  |0.15990  |0.197400|0.127900   |...|23.570  |25.53  |152.50  |1709.0  |0.14440  |0.42450|0.45040  |0.24300  |0.3613  |0.08758|
|...|
|568|927241  |M  |20.600  |29.33  |140.10  |1265.0  |0.11780  |0.27700  |0.351400|0.152000   |...|25.740  |39.42  |184.60  |1821.0  |0.16500  |0.86810|0.93870  |0.26500  |0.4087  |0.12400|
|569|92751  |B   |7.760  |24.54   |47.92   |181.0  |0.05263  |0.04362  |0.000000|0.000000|...|9.456  |30.37   |59.16   |268.6  |0.08996  |0.06444|0.00000  |0.00000  |0.2871  |0.07039|

</br>

### MNIST：（手書き数字文字画像データ）

URL : http://yann.lecun.com/exdb/mnist/

### 渦巻きデータ：（csvフォーマット）

URL : https://github.com/Yagami360/MachineLearning_Exercises_Python_scikit-learn/blob/master/EnsembleLearning_scikit-learn/data/naruto.csv

２クラス（0 or 1）識別問題用の渦巻状のデータ。
