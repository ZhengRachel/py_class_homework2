#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'此文件用于从网站爬取任务二（人口年龄结构）所需要的数据并返回'

__author__ = 'Zheng Rachel'

import requests
import time
import json

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
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    #参数的填充
    keyvalue['m'] = 'QueryData'
    keyvalue['dbcode'] = 'hgnd'
    keyvalue['rowcode'] = 'zb'
    keyvalue['colcode'] = 'sj'
    keyvalue['wds'] = '[]'
    keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":"A0303"}]'
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
    #print(r.text)
    return r_dict

def SaveDataInDict(r_dict):
    all = {}  # 用于存储总人口数
    children = {}  # 用于0-14岁人口数
    young = {}  # 用于15-64岁人口数
    old={} # 用于存储65岁以上人口数
    for i in range(0, 20):
        all[2018 - i] = r_dict['returndata']['datanodes'][i]['data']['data']
        children[2018 - i] = r_dict['returndata']['datanodes'][20 + i]['data']['data']
        young[2018 - i] = r_dict['returndata']['datanodes'][40 + i]['data']['data']
        old[2018 - i] = r_dict['returndata']['datanodes'][60 + i]['data']['data']
    #print('all', all)
    #print('male', male)
    #print('female', female)
    return all,children,young,old

if __name__ == '__main__':
    r_dict=GetData()
    population=SaveDataInDict(r_dict)
    print("all",population[0])
    print("children",population[1])
    print("young",population[2])
    print("old",population[3])