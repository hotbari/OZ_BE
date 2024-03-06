from db import db

# db.Model은 SQLAlchemy의 모델 클래스
class User(db.Model):
    # 테이블이름 설정
    __tablename__ = "users"
    
    # 필드 정의
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    
    # Board 클래스와 연결
    # 역참조는 author : User 객체를 통해 boards에 새로운 데이터가 추가되면 Board 객체의 author 속성에도 자동으로 업데이트
    # 데이터 로드할 때 동작(lazy)은 쿼리가 실행될 때만 데이터를 로드하도록 설정(dynamic)
    boards = db.relationship('Board', back_pupulates='author', lazy='dynamic')
    
class Board(db.Model):
    __tablename__ = "boards"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    author = db.relationship('User', back_populates='boards')