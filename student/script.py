# -*- coding: utf-8 -*-
import pandas as pd
from pandas import Series, DataFrame
from sqlalchemy import create_engine

db_info = {'user': 'root',
           'password': 'yuxinlei2014',
           'host': 'localhost',
           'port': 3306,
           'database': 'DataProcess'
           }
engine = create_engine('mysql+pymysql://%(user)s:%(password)s@%(host)s:%(port)d/%(database)s?charset=utf8' % db_info, encoding='utf-8')


# 学生消费水平数据入库
df = pd.read_csv('/Users/yuxinlei/workspace/practice/python/pandas/DataProcess/data_process/data/stupro.csv',encoding="gbk")
df_consumption = pd.DataFrame(columns=['username','consumption','type','date_created'])
df_consumption['username'] = df['姓名']
df_consumption['consumption'] = df['操作金额']
df_consumption['type'] = df['交易类型']
df_consumption.type[df_consumption['type']=='餐费支出'] = 1
df_consumption.type[df_consumption['type']=='公交支出'] = 2
df_consumption.type[df_consumption['type']=='消费红冲'] = 3
df_consumption['date_created'] = df['操作日期']


df_consumption['username']     = df_consumption['username'].astype(str)
df_consumption['consumption']  = df_consumption['consumption'].astype(float)
df_consumption['type']         = df_consumption['type'].astype(int)
df_consumption['date_created'] = df_consumption['date_created'].astype(str)
df_consumption.duplicated()

pd.io.sql.to_sql(df_consumption, 'consumption', con=engine, index=False, if_exists='replace')
print(df_consumption.head())


#学生图书借阅数据入库
df = pd.read_excel("/Users/yuxinlei/workspace/practice/python/pandas/DataProcess/data_process/data/计算机系图书借阅表_标签.xlsx")
df_book = pd.DataFrame(columns=['book_name','book_type'])

df_book_manage = pd.DataFrame(columns=['number','book_name','date_created'])

df_book['book_name'] = df['题名']
df_book['book_type'] = df['借阅类型（1-专业相关，2-大学英语或英语等级，3-大学数学，4-考研英语数学政治，5-中外文学，6-职业与创业，7-其他）']

df_book_manage['number']       = df['读者条码']
df_book_manage['book_name']    = df['题名']
df_book_manage['date_created'] = df['处理时间']
pd.io.sql.to_sql(df_book, 'book', con=engine, index=False, if_exists='replace')
pd.io.sql.to_sql(df_book_manage, 'book_manage', con=engine, index=False, if_exists='replace')
print(df_book.head())
print(df_book_manage.head())
df_consumption.duplicated()
#学生基本信息入库
df = pd.read_excel("/Users/yuxinlei/workspace/practice/python/pandas/DataProcess/data_process/data/学生基本信息表.xlsx")
df_student = pd.DataFrame(columns=['number','username','sex','nation','grade','homeland','identify','education','major','class','birth','dormitory'])


df_student['number'] = df['学号']
df_student['username'] = df['姓名']
df_student['sex'] = df['性别']
df_student['nation'] = df['民族']
df_student['grade'] = df['年级'][:-1]
df_student['homeland'] = df['籍贯']
df_student['identify'] = df['政治面貌']
df_student['education'] = df['培养层次']
df_student['major'] = df['专业（全称)']
df_student['class'] = df['班级']
df_student['birth'] = df['出生年月']
df_student['dormitory'] = df['宿舍号']
pd.io.sql.to_sql(df_student, 'student', con=engine, index=False, if_exists='replace')
print(df_student.head())
#学生成绩入库
df = pd.read_excel("/Users/yuxinlei/workspace/practice/python/pandas/DataProcess/data_process/data/16级成绩.xlsx")
df_course = pd.DataFrame(columns=['course_num','course_name', 'teacher','credit','check','semester'])
df_score  = pd.DataFrame(columns=['number','course_num', 'score','check_type','conment','year'])

df_course['course_num'] = df['课程号']
df_course['course_name'] = df['课程名']
df_course['teacher'] = df['主讲教师']
df_course['credit'] = df['学分']
df_course['check'] = df['考核方式']
df_course['semester'] = df['学期']

df_score['number'] = df['学号']
df_score['course_num'] = df['课程号']
df_score['score'] = df['总评']
df_score['check_type'] = df['考试性质']
df_score['conment'] = df['备注']
df_score['year'] = df['学年']
df_course.duplicated(['course_num'], keep='last')
df_score.duplicated()
pd.io.sql.to_sql(df_course, 'course', con=engine, index=False, if_exists='replace')
pd.io.sql.to_sql(df_score, 'score', con=engine, index=False, if_exists='replace')
print(df_course.head())
print(df_score.head())


df = pd.read_excel("/Users/yuxinlei/workspace/practice/python/pandas/DataProcess/data_process/data/17级成绩.xlsx")
df_course = pd.DataFrame(columns=['course_num','course_name', 'teacher','credit','check','semester'])
df_score  = pd.DataFrame(columns=['number','course_num', 'score','check_type','conment','year'])

df_course['course_num'] = df['课程号']
df_course['course_name'] = df['课程名']
df_course['teacher'] = df['主讲教师']
df_course['credit'] = df['学分']
df_course['check'] = df['考核方式']
df_course['semester'] = df['学期']

df_score['number'] = df['学号']
df_score['course_num'] = df['课程号']
df_score['score'] = df['总评']
df_score['check_type'] = df['考试性质']
df_score['conment'] = df['备注']
df_score['year'] = df['学年']
df_course.duplicated(['course_num'], keep='last')
df_score.duplicated()
pd.io.sql.to_sql(df_course, 'course', con=engine, index=False, if_exists='append')
pd.io.sql.to_sql(df_score, 'score', con=engine, index=False, if_exists='append')
print(df_course.head())
print(df_score.head())
