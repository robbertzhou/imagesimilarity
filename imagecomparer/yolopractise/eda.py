import base64
from io import BytesIO
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
import pandas as pd

# 箱型图
def box(title='探索性数据分析箱型图'):
    matplotlib.use('Agg')  # 不出现画图的框
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 这两行用来显示汉字
    plt.rcParams['axes.unicode_minus'] = False
    sns.boxplot([133,123,899,198,849,180,844])  # 箱线图
    plt.title(title, loc='center')
    sio = BytesIO()
    plt.savefig(sio, format='png', bbox_inches='tight', pad_inches=0.0)
    data = base64.encodebytes(sio.getvalue()).decode()
    src = 'data:image/png;base64,' + str(data)
    # 记得关闭，不然画出来的图是重复的
    plt.close()
    return src

def alsy(stringdata):

    tips = pd.read_csv(StringIO(stringdata), sep=",")
    # tips = pd.read_csv('tips.csv')
    g = sns.PairGrid(tips)
    g.map_diag(sns.distplot)
    g.map_upper(plt.scatter)
    g.map_lower(sns.kdeplot)
    sio = BytesIO()
    plt.savefig(sio, format='png', bbox_inches='tight', pad_inches=0.0)
    data = base64.encodebytes(sio.getvalue()).decode()
    src = 'data:image/png;base64,' + str(data)
    # 记得关闭，不然画出来的图是重复的
    plt.close()
    return src