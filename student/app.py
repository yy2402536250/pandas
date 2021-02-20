from flask import Flask
from flask import request
from DataBase import DB
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/overview/showBoard')
def show_board():
    db = DB(user='root', pw='yuxinlei2014', host='localhost', database='DataProcess')
    # 学生总人数
    sql = "select count(number) as count from student"
    student_count = db.select(sql)
    s_count = student_count.fetchone()[0]
    boardlist = [s_count]
    #本科人数
    sql = "select count(number) as count from student where education='本科'"
    student_count = db.select(sql)
    s_count = student_count.fetchone()[0]
    boardlist.append(s_count)
    # 研究生人数
    boardlist.append(0)

    # 专科人数数
    sql = "select count(number) as count from student where education='专科'"
    student_count = db.select(sql)
    s_count = student_count.fetchone()[0]
    boardlist.append(s_count)

    # 课程总数
    sql = "select count(course_num) as count from course"
    student_count = db.select(sql)
    s_count = student_count.fetchone()[0]
    boardlist.append(s_count)

    # 在库班级总数
    sql = "select count(class) from (select class,count(class)  from student group by class) a"
    student_count = db.select(sql)
    s_count = student_count.fetchone()[0]
    boardlist.append(s_count)
    return json.dumps(boardlist), 200, [("Python", "Flask"), ("Access-Control-Allow-Origin", "*")]


@app.route('/overview/listGrades')
def list_grades():
    db = DB(user='root', pw='yuxinlei2014', host='localhost', database='DataProcess')
    sql = "select grade,count(grade)  as count from student group by grade;"
    student_count = db.select(sql)
    g_count = student_count.fetchall()
    boardlist=[]
    for item in g_count:
        boardlist.append(item['grade'])
    return json.dumps(boardlist), 200, [("Python", "Flask"), ("Access-Control-Allow-Origin", "*")]


@app.route('/overview/sexcount/grade')
def sex_count_grade():
    year = request.args.get('year')

    db = DB(user='root', pw='yuxinlei2014', host='localhost', database='DataProcess')
    if year == '0':
        sql = "select sex,count(sex) count from student group by sex"
    else:
        sql = "select sex,count(sex) count  from student where grade='" + year + "' group by sex"

    student_count = db.select(sql)
    g_count = student_count.fetchall()
    boardlist = {}
    for item in g_count:
        if item['sex'] == '男':
            boardlist['bnum'] = item['count']
        else:
            boardlist['gnum'] = item['count']
    return json.dumps(boardlist), 200, [("Python", "Flask"), ("Access-Control-Allow-Origin", "*")]


@app.route('/overview/nation')
def nation():
    db = DB(user='root', pw='yuxinlei2014', host='localhost', database='DataProcess')
    sql = "select nation,count(nation) count  from student group by nation;"
    student_count = db.select(sql)
    g_count = student_count.fetchall()
    nation_1 = {}
    for item in g_count:
        nation_1[item['nation']] = item['count']
    boardlist = {"0": nation_1}
    return json.dumps(boardlist), 200, [("Python", "Flask"), ("Access-Control-Allow-Origin", "*")]


@app.route('/overview/grades')
def grades():
    db = DB(user='root', pw='yuxinlei2014', host='localhost', database='DataProcess')
    sql = "select grade,count(grade) count  from student group by grade;"
    student_count = db.select(sql)
    g_count = student_count.fetchall()
    boardlist = {}
    for item in g_count:
        boardlist[item['grade']] = item['count']

    return json.dumps(boardlist), 200, [("Python", "Flask"), ("Access-Control-Allow-Origin", "*")]


@app.route('/overview/ps')
def identify():
    db = DB(user='root', pw='yuxinlei2014', host='localhost', database='DataProcess')
    sql = "select identify,grade,number  from student ;"
    student_count = db.select(sql)
    g_count = student_count.fetchall()
    boardlist = []

    for item in g_count:
        identify = {}
        identify['psname'] = item['identify']
        identify['termYear'] = item['grade']
        boardlist.append(identify)
        identify = {}
        identify['psname'] = item['identify']
        identify['termYear'] = '全学院'
        boardlist.append(identify)

    return json.dumps(boardlist), 200, [("Python", "Flask"), ("Access-Control-Allow-Origin", "*")]


@app.route('/overview/stumap')
def stumap():
    db = DB(user='root', pw='yuxinlei2014', host='localhost', database='DataProcess')
    sql = "select substring(homeland,1,2) homeland,count(homeland) count from student group by substring(homeland,1,2);"
    student_count = db.select(sql)
    g_count = student_count.fetchall()
    boardlist = []
    for item in g_count:
        homeland = item['homeland']
        if homeland == "内蒙":
            homeland = "内蒙古"
        elif homeland == "黑龙":
            homeland = "黑龙江"
        map = {"name": homeland, "value": round(item['count'])}
        boardlist.append(map)

    return json.dumps(boardlist), 200, [("Python", "Flask"), ("Access-Control-Allow-Origin", "*")]


@app.route('/overview/allscore')
def stumap():
    db = DB(user='root', pw='yuxinlei2014', host='localhost', database='DataProcess')
    sql = "select substring(homeland,1,2) homeland,count(homeland) count from student group by substring(homeland,1,2);"
    student_count = db.select(sql)
    g_count = student_count.fetchall()
    boardlist = []
    for item in g_count:
        homeland = item['homeland']
        if homeland == "内蒙":
            homeland = "内蒙古"
        elif homeland == "黑龙":
            homeland = "黑龙江"
        map = {"name": homeland, "value": round(item['count'])}
        boardlist.append(map)

    return json.dumps(boardlist), 200, [("Python", "Flask"), ("Access-Control-Allow-Origin", "*")]



if __name__ == '__main__':
    app.run()
