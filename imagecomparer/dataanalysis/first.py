from io import StringIO
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = """total_bill,tip,size
16.99,1.01,2
10.34,1.66,3
21.01,3.5,3
23.68,3.31,2
24.59,4.71,4
8.77,2,4
26.88,3.12,2
15.04,1.96,4
14.78,3.23,2
10.27,1.71,2
35.26,5,2
15.42,1.57,4
18.43,3.02,2
14.83,3.02,3"""
tips = pd.read_csv(StringIO(data), sep=",")
# tips = pd.read_csv('tips.csv')
g = sns.PairGrid(tips)
g.map_diag(sns.distplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)



plt.show()