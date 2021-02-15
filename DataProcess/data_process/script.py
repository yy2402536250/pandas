# -*- coding: utf-8 -*-
import pandas as pd
from pandas import Series, DataFrame
from sqlalchemy import create_engine

#学生消费水平数据入库
df = pd.read_csv('/Users/yuxinlei/workspace/practice/python/pandas/DataProcess/data_process/data/stupro.csv',encoding="gbk")
del df['u']
del df['操作员']
df.dropna(axis='columns', thresh=5,inplace=True)
df = pd.concat([df,DataFrame(df['部门'].str.split('/').tolist())], axis=1, join='outer')
df = df.rename(columns={'F25':'身份'})
df = df.rename(columns={0:'年级'})
df = df.rename(columns={1:'专业'})
del df['部门']

db_info = {'user': 'root',
           'password': 'yuxinlei2014',
           'host': 'localhost',
           'port': 3306,
           'database': 'DataProcess'
           }
engine = create_engine('mysql+pymysql://%(user)s:%(password)s@%(host)s:%(port)d/%(database)s?charset=utf8' % db_info, encoding='utf-8')
pd.io.sql.to_sql(df, 'consumption', con=engine, index=False, if_exists='replace')
print(df.head())


#学生图书借阅数据入库

#学生基本信息入库

#学生成绩入库
