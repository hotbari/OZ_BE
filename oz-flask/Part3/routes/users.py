# 모듈 import
from flask import request, jsonify
from flask.views import MethodView # 메소드 사용 정의해주는 모듈
from flask_smorest import Blueprint
from db import db
from models import User

user_blp = Blueprint('Users','users',description='Operations on users')

@user_blp.route('/')
class Userlist(MethodView):
    def get(self):
        # 모든 사용자 가져오기
        users = User.query.all()
        # 사용자 데이터를 리스트로 변환
        user_data = [ {"id":users.id, "name":users.name,"email":users.email}]
        return jsonify(user_data)
    
    # 새로운 사용자 생성 필요 없는지 확인
    def post(self):
        # 요청된 JSON 데이터 가저오기
        print("요청이 오나요?")
        user_data = request.json
        new_user = User(name=user_data['name'],email=user_data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message":"User created"}),201
    
    
@user_blp.route('/<int:user_id>')
class Users(MethodView):
    def get(self, user_id):
        # 사용자가 존재하지 않으면 404 오류 반환
        user = User.query.get_or_404(user_id)
        return {"name":user.name, 'email':user.email}
    
    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        user_data = request.json
        
        # 사용자 이름, 이메일 업데이트
        user.name = user_data['name']
        user.email = user_data['email']
        
        db.session.commit()
        return {"message":"User updated"}
    
    def delete(self, user_id):
        # 사용자가 존재하지 않으면 404 오류 반환
        user = User.query.get_or_404(user_id)
        # 사용자 삭제
        db.session.delete(user)
        db.session.commit()
        return {"message":"User deleted"}
    
    