#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'此文件用于绘制任务二（人口年龄结构）所要求绘制的统计图'

__author__ = 'Zheng Rachel'

import savenread_data_task2
import matplotlib.pyplot as plt

def SketchPlot(year,proportion_children,proportion_young,proportion_old):
    plt.plot(year,proportion_children,color='b',label='Children')
    plt.plot(year,proportion_young,color='r',label='Young')
    plt.plot(year, proportion_old, color='g', label='Old')
    plt.legend()
    plt.xlabel('year')
    plt.ylabel('proportion')
    plt.title('Proportion')
    plt.show()

def SketchPie(structure):
    label = ['0-14 years old','15-64 years old','65 years old and older']
    color = ['b','r','g']
    indic = []
    #将比例最大的予以突出显示
    for val in structure:
        if val == max(structure):
            indic.append(0.1)
        else:
            indic.append(0)
    plt.pie(structure,labels=label,colors=color,startangle=90,shadow=True,explode=tuple(indic),autopct='%2.4f%%')
    plt.title('Sector chart of population structure of 2016')
    plt.show()


if __name__ == '__main__':
    #先保存数据到数据库
    savenread_data_task2.SaveData()
    #再从数据库中读取
    data = savenread_data_task2.ReadData()

    #存储各年数据
    year = []
    children = []
    young = []
    old = []
    for i in range(0, 20):
        year.append(data[0][19 - i][0])
        children.append(data[1][19 - i][1]/data[0][19-i][1])
        young.append(data[2][19 - i][1]/data[0][19-i][1])
        old.append(data[3][19 - i][1]/data[0][19 - i][1])

    # 找出2016年的各项数据，存于structure2016中
    structure2016=[children[17],young[17],old[17]]

    #⼀张折线图 ⼀张折线图展⽰出1999年到2017年三个年龄段人口占总人口比例的变化
    SketchPlot(year,children,young,old)
    #2016年的人口结构扇形图
    SketchPie(structure2016)