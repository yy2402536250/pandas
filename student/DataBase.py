# -*- coding: utf-8 -*-
import pandas as pd
from pandas import Series, DataFrame
from sqlalchemy import create_engine


class DB():
    def __init__(self, user='root', pw='', host='localhost', database=''):
        self.db_info = {'user': user,
                   'password': pw,
                   'host': host,
                   'port': 3306,
                   'database': database
                   }
        self.engine = create_engine(
            'mysql+pymysql://%(user)s:%(password)s@%(host)s:%(port)d/%(database)s?charset=utf8' % self.db_info,
            encoding='utf-8')
        self.conn = self.engine.connect()

    def select(self, sql):
        if not sql:
            return 0
        res_obj = self.conn.execute(object_=sql)
        return res_obj
