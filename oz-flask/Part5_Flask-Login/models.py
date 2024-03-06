# Flask-Login 확장을 사용하여 사용자 인증 및 세션 관리를 구현하는 방법
# UserMixin 클래스를 상속하여 사용자 모델을 정의하고 사용자의 데이터를 관리


from flask_login import UserMixin

# 사용자 데이터
# users 딕셔너리에서 사용자 데이터 관리
# 사용자 이름(admin)이 키
# 해당 사용자의 정보가 값

users = {'admin': {'password': 'pw123'}}

# UserMixin 클래스 상속 -> Flask-Login 확장을 사용하여 사용자 모델을 정의
class User(UserMixin):
    # username을 받아 id 속성에 할당하여 Flask-Login이 사용자 객체를 식별할 수 있음
    def __init__(self, username):
        self.id = username

    # 주어진 user_id에 해당하는 사용자 객체를 반환하고, 그렇지 않으면 None을 반환
    @staticmethod
    def get(user_id):
        if user_id in users:
            return User(user_id)
        return None