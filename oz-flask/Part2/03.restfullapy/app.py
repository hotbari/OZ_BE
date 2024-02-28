from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    
    ## 특정 아이템 조회
    def get(self,name):
        # 조회하려는 아이템이 있다면
        for item in items:
            if item['name'] == name:
                return item
            
        # 조회하려는 아이템이 없으면
        return {'message':'Item not found'}, 404 
    
    
    ## 새 아이템 추가
    def post(self, name):
        
        # 추가하려는 아이템 이름이 존재하면 해당 문구 리턴
        for item in items: 
            if item['name'] == name:
                return {'message': f'This item is already exists.'}, 400
            
        # 없으면 items 리스트에 append
        data = request.get_json()
        new_item = {'name':name, 'price':data['price']}
        items.append(new_item)
        return items
    
    
    ## 아이템 업데이트
    def put(self, name):
        
        # 업데이트를 위해 데이터를 미리 가져옴
        data = request.get_json()
        
        for item in items:
            if item['name'] == name:
                item['price'] = data['price']
                return item
            
        # 아이템이 없으면 추가됨
        new_item = {'name':name, 'price':data['price']}
        items.append(new_item)
        return new_item

    
    ## 아이템 삭제
    def delete(self, name):
        global items
        
        # 삭제요청한 아이템을 제외한 아이템들만 가져옴
        items = [item for item in items if item['name'] != name]
        return {'message':'Item deleted'}
    
    
api.add_resource(Item, '/item/<string:name>') # url

if __name__ == '__main__':
    app.run(debug=True)