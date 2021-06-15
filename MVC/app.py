from flask import Flask, render_template, request
# import graph
import json
# import mytest
import ConMysql

app = Flask(__name__)

'''
@app.route('/', methods=['GET', 'POST'])
def index():
    a = "小寨"
    if request.method == 'POST':
        a = request.form.get('SQ')
        print(a)
        return render_template('index.html', a=a)
    return render_template('index.html', a=a)


@app.route('/data/<string:a>', methods=['GET', 'POST'])
def get_SQdata(a):
    # if request.method == 'POST':
    #     a =request.form.get('SQ')
    #     print(a)
    #     a = "丈八"
    #     print(a)
    #     list, links = mytest.cypshangquan(a)
    #     b = json.dumps({'list': list, 'links': links})
    #     # print(b)
    #     return b
    list, links = mytest.SQAllPOI(a)
    b = json.dumps({'list': list, 'links': links})
    # print(b)
    return b
    #return list,links


@app.route('/TS', methods=['GET', 'POST'])
def iniTS():
    a = "小龙虾"
    if request.method == 'POST':
        a = request.form.get('TS')
        print(a)
        return render_template('TS.html', a=a)
    return render_template('TS.html', a=a)


@app.route('/TSdata/<string:a>', methods=['GET', 'POST'])
def getTS_data(a):
    list, links = mytest.TSAllPOI(a)
    b = json.dumps({'list': list, 'links': links})
    # print(b)
    return b



@app.route('/SQ', methods=['GET', 'POST'])
def get_POIYeardata():
    return render_template('poi.html')


@app.route('/SQdata',methods=['GET', 'POST'])
def poigss():
    SQName, KindName, Knumber = mytest.SQ20()
    b = json.dumps({'SQName': SQName, 'KindName': KindName, 'Knumber': Knumber})
    return b

'''
@app.route('/GDMap', methods=['GET', 'POST'])
def get_GDMap():
    return render_template('GDMap.html')



@app.route('/GDdata', methods=['GET','POST'])
def get_GDdata():
    zen = []
    deng = []
    jian = []
    relizen = []
    relideng =[]
    relijian =[]

    if request.method == 'POST':
        data = request.get_data()
        data = json.loads(data)
        # print("js 传过来的两个参数：")

        myyears = data["years"]
        mykinds = data["kinds"]
        zen, deng, jian, relizen, relideng, relijian = ConMysql.getdata(myyears, mykinds)
        print(zen)
        print(relizen)
    d = json.dumps({'zen': zen, 'deng': deng, 'jian': jian, 'relizen': relizen, 'relideng':relideng, 'relijian':relijian})

    return d




if __name__ == "__main__":
    app.run(debug=True)


