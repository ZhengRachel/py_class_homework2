#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'此文件用于从网站爬取任务一（年末总人口数等）所需要的数据并返回'

__author__ = 'Zheng Rachel'

import requests
import time

#用来获取时间戳
def GetTime():
    return int(round(time.time() * 1000))

#用于爬取数据
def GetData():
    #用来自定义头部的
    headers = {}
    #用来传递参数的
    keyvalue = {}
    #目标网址(问号前面的东西)
    url = 'http://data.stats.gov.cn/easyquery.htm'
    #头部的填充
    headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14) ' \
                            'AppleWebKit/605.1.15 (KHTML, like Gecko) ' \
                            'Version/12.0 Safari/605.1.15'
    #参数的填充
    keyvalue['m'] = 'QueryData'
    keyvalue['dbcode'] = 'hgnd'
    keyvalue['rowcode'] = 'zb'
    keyvalue['colcode'] = 'sj'
    keyvalue['wds'] = '[]'
    keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":"A0301"}]'
    keyvalue['k1'] = str(GetTime())
    #建立一个Session
    s = requests.session()
    #在Session基础上进行一次请求
    r = s.post(url, params=keyvalue, headers=headers)
    #打印返回过来的状态码
    # 修改dfwds字段内容
    keyvalue['dfwds'] = '[{"wdcode":"sj","valuecode":"LAST20"}]'
    # 再次进行请求
    r = s.post(url, params=keyvalue, headers=headers)
    # 此时我们就能获取到我们搜索到的数据了
    r_dict = json.loads(r.text)
    return r_dict

#将爬到的数据存在三个dict中并返回
def SaveDataInDict(r_dict):
    all = {}  # 用于存储总人口数
    male = {}  # 用于存储男性人口数
    female = {}  # 用于存储女性人口数
    for i in range(0, 20):
        all[2018 - i] = r_dict['returndata']['datanodes'][i]['data']['data']
        male[2018 - i] = r_dict['returndata']['datanodes'][20 + i]['data']['data']
        female[2018 - i] = r_dict['returndata']['datanodes'][40 + i]['data']['data']
    #print('all', all)
    #print('male', male)
    #print('female', female)
    return all,male,female

if __name__ == '__main__':
    r_dict=GetData()
    population=SaveDataInDict(r_dict)
    print("all",population[0])
    print("male",population[1])
    print("female",population[2])
