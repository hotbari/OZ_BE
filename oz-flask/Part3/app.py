# 모듈 import 
from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy

# db 밑줄 생겨서 pip install db로 해결
from db import db

# models 모듈에서 users.py, board.py import
from models import User, Board

# Flask API 생성
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:010913@localhost/oz'
# 객체가 바뀔 때마다 트래킹 할 것인지 선택 -> 메모리 부하가 심해서 보통 False
app.config['SQLARLCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# bluepring 설정 및 등록
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

from routes.users import user_blp
from routes.board import board_blp

api = Api(app)
api.register_blueprint(user_blp)
api.register_blueprint(board_blp)

from flask import render_template
@app.route('/manage-boards')
def manage_boards():
    return render_template('boards.html')

@app.route('/manage-users')
def manage_users():
    return render_template('users.html')

if __name__ == '__main__':
    # DB에 테이블 생성
    with app.app_context():
        print("여기 실행?")
        db.creat_all()
        
    app.run(debug=True)
