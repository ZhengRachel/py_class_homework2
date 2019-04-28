#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'此文件用于实现向数据库population_task2.db中存储或读取任务二相关数据的操作'

__author__ = 'Zheng Rachel'

import sqlite3
import get_data_task2

class DataBase:
    def __init__(self,dbname):
        try:
            conn=sqlite3.connect(dbname)
            print("Opened database successfully")
            cursor =conn.cursor()
            self.conn=conn
            self.cursor=cursor
        except Exception:
            print("Operation Failed")

    def CreateTable(self,tbname):
            self.cursor.execute('''CREATE TABLE %s
                           (year INT PRIMARY KEY NOT NULL,
                           data INT NOT NULL);''' %(tbname))

    def InsertData(self,tbname,val_year,val_data):
            self.cursor.execute('insert into %s(year,data) values(%d,%d)' %(tbname,val_year,val_data))

    def SelectData(self,tbname):
        self.cursor.execute("select * from %s;" %(tbname))
        data = self.cursor.fetchall()
        return data

    def CloseDatabase(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def DeleteTable(self,tbname):
        self.conn.execute("drop table if exists %s" %(tbname))


def SaveData():

    r_dict=get_data_task2.GetData()
    popu=get_data_task2.SaveDataInDict(r_dict)

    #打开数据库
    db=DataBase('population_task2.db')

    #若表已存在，先删除后重建，避免运行报错
    try:
        db.DeleteTable('ALLPOPU')
        db.DeleteTable('CHILDREN')
        db.DeleteTable('YOUNG')
        db.DeleteTable('OLD')
        print("DELETE DONE")
    except Exception:
        pass

    #建表
    try:
        db.CreateTable('ALLPOPU')
        print("TABLE ALLPOPU IS CREATED SUCCESSFULLY")
    except Exception:
        print("TABLE ALLPOPU TABLES EXIST")
    try:
        db.CreateTable('CHILDREN')
        print("TABLE CHILDREN IS CREATED SUCCESSFULLY")
    except Exception:
        print("TABLE CHLIDREN TABLES EXIST")
    try:
        db.CreateTable('YOUNG')
        print("TABLE YOUNG IS CREATED SUCCESSFULLY")
    except Exception:
        print("TABLE YOUNG TABLES EXIST")
    try:
        db.CreateTable('OLD')
        print("TABLE OLD IS CREATED SUCCESSFULLY")
    except Exception:
        print("TABLE OLD TABLES EXIST")

    #向表中插入数据
    for i in range(0,20):
        db.InsertData('ALLPOPU',2018-i,popu[0][2018-i])
        db.InsertData('CHILDREN', 2018-i, popu[1][2018-i])
        db.InsertData('YOUNG',2018-i,popu[2][2018-i])
        db.InsertData('OLD',2018-i,popu[3][2018-i])
    print("INSERT DONE")

    #提交并关闭数据库
    db.CloseDatabase()

def ReadData():
    db=DataBase('population_task2.db')
    data_all=db.SelectData('ALLPOPU')
    data_children=db.SelectData('CHILDREN')
    data_young=db.SelectData('YOUNG')
    data_old = db.SelectData('OLD')
    db.CloseDatabase()
    return data_all,data_children,data_young,data_old


if __name__ == '__main__':
    SaveData()
    data=ReadData()
    print(data[0])
    print(data[1])
    print(data[2])
    print(data[3])