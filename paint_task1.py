#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'此文件用于绘制任务一（年末总人口数等）所要求绘制的统计图'

__author__ = 'Zheng Rachel'

import savenread_data_task1
import matplotlib.pyplot as plt

def SketchBar(year,popu):
    plt.bar(year,popu,color='b',label='Population')
    plt.legend()
    plt.ylim((110000,150000))
    plt.xlabel('year')
    plt.ylabel('population')
    plt.title('Population Unit:10 thousand')
    plt.show()

def SketchPlot(year,proportion_male,proportion_female):
    plt.plot(year,proportion_male,color='b',label='Male')
    plt.plot(year,proportion_female,color='r',label='Female')
    plt.legend()
    plt.xlabel('year')
    plt.ylabel('proportion')
    plt.title('Proportion')
    plt.show()


if __name__ == '__main__':
    savenread_data_task1.SaveData()
    data = savenread_data_task1.ReadData()
    year = []
    population = []
    male = []
    female = []
    for i in range(0, 20):
        year.append(data[0][19 - i][0])
        population.append(data[0][19 - i][1])
        male.append(data[1][19 - i][1]/data[0][19-i][1])
        female.append(data[2][19 - i][1]/data[0][19 - i][1])
    SketchBar(year, population)
    SketchPlot(year,male,female)