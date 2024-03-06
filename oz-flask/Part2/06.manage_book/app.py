## 애플리케이션 설정

# 필요한 모듈 import
from flask import Flask
from flask_smorest import Api
from api import book_blp

app = Flask(__name__)

app.config['API_TITLE'] = 'Book API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.0.2'
app.config['OPENAPI_URL_PREFIX'] = '/'
app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'
app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

# Api 객체 생성
api = Api(app)

# book_blp를 API에 등록
api.register_blueprint(book_blp)

if __name__ == '__main__': # 코드가 직접 실행될 때
    app.run(debug=True)
    