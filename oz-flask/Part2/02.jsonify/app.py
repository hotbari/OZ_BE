from flask import Flask, jsonify, request

app = Flask(__name__)


## GET

# 전체 게시글을 불러오는 API
@app.route('/api/v1/feeds', methods=['GET'] )
def show_all_feeds():
    data = {'result':'sucess', 'data':{'feed1':'data1','feed2':'data2'}}

    return data #dict타입이라 jsonify를 사용하지 않아도 Flask에서 읽을 수 있다.

# 특정 게시글 불러오는 API
@app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
def show_one_feed(feed_id):
    print(feed_id)
    data = {'result':'success','data':{'feed1':'data1'}}
    
    return data

## POST

# 게시글 작성 API
@app.route('/api/v1/feeds', methods=['POST'])
def create_one_feed():
    name = request.form['name']
    age = request.form['age']
    print(name, age)
    return(jsonify ({'result':'success'}))


# 데이터 추가 API

datas = [{'items': [{'name':'item1','price':10}]}]

@app.route('/api/v1/datas', methods=['GET'])
def get_datas():
    return {'datas':datas}

@app.route('/api/v1/datas', methods=['POST'])
def create_date():
    request_data = request.get_data()
    
    new_data = {'items':request_data.get('item', [])}
    datas.append(new_data)
    
    return new_data, 201