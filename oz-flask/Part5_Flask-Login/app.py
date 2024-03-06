# Flask 애플리케이션에 Flask-Login을 사용하여 사용자 인증 및 세션 관리를 구현

from flask import Flask
from flask_login import LoginManager
from models import User


## 1. Flask 애플리케이션과 Flask-Login 설정

# 'routes' 모듈을 임포트하기 전에 'app'과 'login_manager' 객체를 생성해야 함
# flask 애플리케이션 생성
app = Flask(__name__)
# session을 위한 비밀키 설정
app.secret_key = 'your_secret_key'

# LoginManager 객체 생성
login_manager = LoginManager()
# 객체 초기화
login_manager.init_app(app)
# 로그인이 필요한 라우트를 지정
login_manager.login_view = 'login'


## 2. 사용자 로딩 함수 설정

# user_id를 기반으로 사용자 객체를 가져옴
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

## 3. 라우트 설정
# 이제 'routes' 모듈을 임포트
from routes import configure_routes
# 라우트 설정 함수를 호출하여 flask 애플리케이션에 라우트를 구성
configure_routes(app)

## 4. API 실행
if __name__ == "__main__":
    app.run(debug=True)